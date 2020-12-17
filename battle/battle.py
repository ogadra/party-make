import subprocess
from time import time
import multiprocessing
import sys
import os
import re
sys.path += [os.path.dirname(os.path.dirname(__file__))]
from makePT import makePokemon

def battle(pt1, pt2):
    # result = subprocess.run(['node', './bot/.sim-dist/examples/battle-stream-example', pt1, pt2], stdout=subprocess.PIPE, text=True)
    proc = subprocess.run(['node', './bot/.sim-dist/examples/battle-stream-example', pt1, pt2], stdout=subprocess.PIPE, text=True)
    battleData = proc.stdout.split('\n')
    flag = False
    for i in battleData:
        print(i)
        if 'error' in i:
            flag = True
    if flag:
        exit()

    result = [i for i in battleData if re.match('\|win\|Bot \d',i)]
    # result = proc.stdout.split('\n')[-2]
    result = str(result)[0]
    return result


if __name__ == "__main__":
    # pt1s = list()
    # print(makePokemon.makeParties())
    pt1 = '|charizard||Blaze|curse,solarbeam|Serious|||||50|'
    # pt1 = '|charizard||Blaze|curse|Serious|||||50|'
    pt2 = '|blissey|Assault Vest|Narural Care|aromatherapy|Serious|||||50|'

    battle(pt1, pt2)
    # for i in range(1000):
    #     battle(makePokemon.makeParties(), makePokemon.makeParties())


# print(data)