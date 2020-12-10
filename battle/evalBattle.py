from time import time
from multiprocessing import Process, Manager, Pool
import sys
import os
import re
import subprocess

pokemon = 'abra'
dataSet = open('./pokemons/' + pokemon + '/0000.txt').read().split('\n')


def battle(evalData, p1, p2):
    pt1 = dataSet[p1]
    pt2 = dataSet[p2]
    proc = subprocess.run(['node', './bot/.sim-dist/examples/battle-stream-example',pt1, pt2], stdout=subprocess.PIPE, text=True)
    battleData = proc.stdout.split('\n')
    result = str([i for i in battleData if re.match('\|win\|Bot \d',i)][0])
    battleData = proc.stdout.split('\n')

    if result == '|win|Bot 1':
        evalData[p1] += 1
    else:
        evalData[p2] += 1
    
def wrapper(args):
    return battle(*args)


if __name__ == "__main__":

    cnt = len(dataSet)
    manager = Manager()
    evalData = manager.list([0]*cnt)

    p = Pool(12)
    que = [[evalData,i,i+j+1] for i in range(cnt-1) for j in range(cnt-i-1)]
    
    s = time()

    p.map(wrapper, que)


    print(sum(evalData) , (cnt * (cnt - 1)) // 2)
    print(time()-s)
    print((time()-s)/(cnt*(cnt-1)//2))

    result = [str(i)+ ' ' +poke for i,poke in sorted(zip(evalData, dataSet), reverse=True)]

    savedir = './pokemons/abra/'
    num = sum(os.path.isfile(os.path.join(savedir, name)) for name in os.listdir(savedir))
    with open (savedir + str(num).zfill(4) + '.txt', 'w') as f:
        for i in result:
            f.write(i)
            f.write('\n')
    
