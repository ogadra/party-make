import subprocess
from time import time
import multiprocessing
import sys
import os
import re
sys.path += [os.path.dirname(os.path.dirname(__file__))]
from makePT import makePokemon

def battle(pt1, pt2):
    print(pt1)
    print(pt2)
    # result = subprocess.run(['node', './bot/.sim-dist/examples/battle-stream-example', pt1, pt2], stdout=subprocess.PIPE, text=True)
    proc = subprocess.run(['node', './bot/.sim-dist/examples/battle-stream-example', pt1, pt2], stdout=subprocess.PIPE, text=True)
    battleData = proc.stdout.split('\n')
    flag = False
    for i in battleData:
        print(i)

    result = [i for i in battleData if re.match('\|win\|Bot \d',i)]
    result = str(result)[0]
    return result


if __name__ == "__main__":
    battle(makePokemon.makeParties(),makePokemon.makeParties())