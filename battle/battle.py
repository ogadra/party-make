import subprocess
from time import time
import multiprocessing
import sys, os
sys.path += [os.path.dirname(os.path.dirname(__file__))]
from makePT import makePokemon

pt1 = '|darumakagalar|Liechi Berry|Hustle|hammerarm,icefang,fireblast,focuspunch|Hasty|84,124,0,76,132,92||31,31,31,31,31,31||50|'
pt2 = '|darumakagalar|Liechi Berry|Hustle|hammerarm,icefang,fireblast,focuspunch|Hasty|84,124,0,76,132,92||31,31,31,31,31,31||50|'

def battle():
    result = subprocess.run(['node', './bot/.sim-dist/examples/battle-stream-example', pt1, pt2], stdout=subprocess.PIPE, text=True)


if __name__ == "__main__":
    # pt1s = list()
    print(makePokemon.makeParties())

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