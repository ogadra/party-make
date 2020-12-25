from multiprocessing import Process, Manager, Pool, cpu_count
import sys
import os
import re
import subprocess
import time 
import random
import numpy as np

def battle(pt1, opponents):
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

if __name__ == '__main__':
    path = './train_data03/'
    opponent = open(path + 'extract.txt').read().split('\n')
    speciesCnt = 80
    prop = [opponent[i*5] for i in range(speciesCnt)]
    battleData = list()

    #battle count = 80 * 80 * 5 => 32000 (about 12800s, 3.5h)
    for i in prop:
        print('\r%d' % len(battleData), end='')
        tmp = list()
        que = [[i,opponent[j*5:j*5+5]] for j in range(speciesCnt)]

        core = cpu_count()
        p = Pool(core)
        tmp = p.map(wrapper, que)
        poke = [i.split('|')[1]]
        poke.extend(tmp)
        poke = [str(j) for j in poke]
        battleData.append(poke)
        
        # for test
    
    pokemons = [i.split('|')[1] for i in prop]
    pokemons = ['FtF'] + pokemons
    with open(path + 'FtFvalue.txt', 'w') as f:
        f.write(','.join(pokemons))
        f.write('\n')
        for i in battleData:
            f.write(','.join(i))
            f.write('\n')