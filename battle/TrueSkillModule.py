import trueskill
from time import time, sleep
from multiprocessing import Process, Manager, Pool
import sys
import os
import re
import subprocess

def battle(evalData, p1, p2):
    pt1 = dataSet[p1]
    pt2 = dataSet[p2]
    proc = subprocess.run(['node', './bot/.sim-dist/examples/battle-stream-example',pt1, pt2], stdout=subprocess.PIPE, text=True)
    battleData = proc.stdout.split('\n')
    result = str([i for i in battleData if re.match('\|win\|Bot \d',i)][0])
    battleData = proc.stdout.split('\n')

    if result == '|win|Bot 1':
        evalData.append([p1,p2])
    else:
        evalData.append([p2,p1])
    
def wrapper(args):
    return battle(*args)


def evalBattle(pokemon):
    savedir = './pokemons/' + pokemon + '/' 
    global dataSet
    num = sum(os.path.isfile(os.path.join(savedir, name)) for name in os.listdir(savedir))

    readfile = savedir + str(num-1).zfill(4) + '.txt'
    with open(readfile, 'r') as f:
        dataSet = f.read().split('\n')



    cnt = len(dataSet)
    manager = Manager()
    evalData = manager.list()

    
    que = []
    matchCount = 24

    for i in range(cnt):
        for j in range(matchCount//2):
            if i + j == cnt - 1:
                break
            que.append([evalData, i, i+j+1])

        if i < matchCount//2:
            for j in range(matchCount//2 - i):
                que.append([evalData, i, cnt-j-1])

    s = time()
    p = Pool(12)
    p.map(wrapper, que)

    print((time()-s)/(matchCount * cnt // 2))
    print(time()-s)

    env = trueskill.TrueSkill(beta=5,draw_probability=0)
    players = [env.create_rating()] * cnt
    for i in evalData:
        players[i[0]], players[i[1]] = trueskill.rate_1vs1(players[i[0]], players[i[1]])
    
    mulist = [mu.mu for mu in players]
    result = [str(i)+ ' ' +poke for i,poke in sorted(zip(mulist, dataSet), reverse=True)]

    writefile = savedir + str(num).zfill(4) + '.txt'

    with open (writefile, 'w') as f:
        f.write('\n'.join(result))
        
    
