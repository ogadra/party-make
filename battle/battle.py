import subprocess
from time import time
import multiprocessing
import sys
import os
import re
sys.path += [os.path.dirname(os.path.dirname(__file__))]
from makePT import makePokemon

def battle():
    # result = subprocess.run(['node', './bot/.sim-dist/examples/battle-stream-example', pt1, pt2], stdout=subprocess.PIPE, text=True)
    proc = subprocess.run(['node', './bot/.sim-dist/examples/battle-stream-example'], stdout=subprocess.PIPE, text=True)
    battleData = proc.stdout.split('\n')
    result = [i for i in battleData if re.match('\|win\|Bot \d',i)]
    # result = proc.stdout.split('\n')[-2]
    result = str(result[0])
    return result


if __name__ == "__main__":
    # pt1s = list()
    print(makePokemon.makeParties())
    for i in range(1000):
        tmp = battle()
        if tmp == '|win|Bot 1':
            pass
        elif tmp == '|win|Bot 2':
            pass
        else:
            print(tmp)
    # for i in range(100):
    #     pt1s.append(makePokemon.makeParties())
    # pt2s = list()
    # for i in range(100):
    #     pt2s.append(makePokemon.makeParties())
    # data = result.stdout
    # print(data)

    # jobs = []
    # cnt = 1000

    # start = time()
    
    # for i in range(cnt):
    #     p = multiprocessing.Process(target=battle)
    #     jobs.append(p)
    #     p.start()
        
    # p.join()
    # print((time() - start)/cnt)
    # data = data.split('\n')[-2]
# print(data)