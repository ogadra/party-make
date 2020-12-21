# from time import time, sleep
from multiprocessing import Process, Manager, Pool, cpu_count
import sys
import os
import re
import subprocess

def battle(i, pt1, opponents):
    wincnt = 0
    for pt2 in opponents:
        if pt1.split('|')[1] == pt2.split('|')[1] and pt1.split('|')[1] == 'ditto':
            if pt1.split('|')[6].split(',')[0] > pt2.split('|')[6].split(',')[0]:
                wincnt += 1
        proc = subprocess.run(['node', './bot/.sim-dist/examples/battle-stream-example',pt1, pt2], stdout=subprocess.PIPE, text=True)
        battleData = proc.stdout.split('\n')
        try:
            result = str([i for i in battleData if re.match('\|win\|Bot \d',i)][0])
        except:
            print(battleData)
        if result == '|win|Bot 1':
            wincnt += 1
    return wincnt

    
def wrapper(args):
    return battle(*args)

def bruteforce(path1, path2):
    dataSet = path1
    cnt = len(dataSet)
    
    opponent = path2
    # manager = Manager()
    # evalData = manager.list()
    
    evalData = [0] * cnt
    que = [[i, dataSet[i], opponent] for i in range(cnt)]
    # s = time()
    core = cpu_count()
    p = Pool(core)
    evalData = p.map(wrapper, que)
    # print((time()-s)/(matchCount * cnt // 2))
    # print(time()-s)

    dataSet = [str(i) + poke for i,poke in zip(evalData, dataSet)]
    dataSet = [i.split('|') for i in dataSet]
    # for i in range(len(dataSet)):
    #     dataSet[i][0] = float(dataSet[i][0])

    dataSet = sorted(dataSet, key = lambda x:(x[1], float(x[0])), reverse=True)

    # for i in range(len(dataSet)):
    #     dataSet[i][0] = str(dataSet[i][0])

    dataSet = ['|'.join(i) for i in dataSet]

    return dataSet
