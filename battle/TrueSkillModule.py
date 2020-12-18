import trueskill
# from time import time, sleep
from multiprocessing import Process, Manager, Pool, cpu_count
import sys
import os
import re
import subprocess
import random

def battle(evalData, p1, p2):
    print('\r%d' % len(evalData), end='')
    pt1 = dataSet[p1]
    pt2 = dataSet[p2]
    proc = subprocess.run(['node', './bot/.sim-dist/examples/battle-stream-example',pt1, pt2], stdout=subprocess.PIPE, text=True)
    battleData = proc.stdout.split('\n')
    try:
        result = str([i for i in battleData if re.match('\|win\|Bot \d',i)][0])
    except:
        print(battleData)
        

    if result == '|win|Bot 1':
        evalData.append([p1,p2])
    else:
        evalData.append([p2,p1])
    
def wrapper(args):
    return battle(*args)


def evalBattle(path, matchCount=18):
    global dataSet
    dataSet = open(path).read().split('\n')
    random.shuffle(dataSet)
    cnt = len(dataSet)
    manager = Manager()
    evalData = manager.list()

    que = []

    for i in range(cnt):
        for j in range(matchCount//2):
            if i + j == cnt - 1:
                break
            que.append([evalData, i, i+j+1])

        if i < matchCount//2:
            for j in range(matchCount//2 - i):
                que.append([evalData, i, cnt-j-1])

    # s = time()
    core = cpu_count()


    p = Pool(core)
    p.map(wrapper, que)

    # print((time()-s)/(matchCount * cnt // 2))
    # print(time()-s)

    env = trueskill.TrueSkill(beta=5,draw_probability=0)
    players = [env.create_rating()] * cnt
    for i in evalData:
        players[i[0]], players[i[1]] = trueskill.rate_1vs1(players[i[0]], players[i[1]])
    
    mulist = [mu.mu for mu in players]
    dataSet = [str(mu) + poke for mu,poke in zip(mulist, dataSet)]
    dataSet = [i.split('|') for i in dataSet]
    dataSet = sorted(dataSet, key = lambda x:(x[1], x[0]), reverse=True)
    dataSet = ['|'.join(i) for i in dataSet]

    return dataSet
    
