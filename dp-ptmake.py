import sys
import os
import re
import time 
import random
from math import log

def calcScore(x):
    return 0.8/(1+10**(3.5-int(x)))

def addPokemon(arg1, arg2):
    ans = [1 - (1 - arg1[i]) * (1 - arg2[i]) for i in range(80)]
    return ans, sum(ans)

def calcPoke(poke):
    poke[1:] = [calcScore(i) for i in poke[1:]]
    return poke

if __name__ == "__main__":
    dpTable = [[[[],[0]*80] for j in range(6)] for i in range(81)]
    
    #data processing to sigmoid value
    #do()
    pokeData = open('./train_data03/FtFvalue.txt').read().split('\n')

    pokeName = pokeData[0].split(',')
    pokeData = [i.split(',') for i in pokeData][1:]
    pokeData = [calcPoke(i) for i in pokeData]
    
    for i in range(1,81):
        dpTable[i][0][0] = [i]
        dpTable[i][0][1] = pokeData[i-1][1:]

    #dp
    for i in range(1,81):
        for j in range(1,6):
            #about dp[i][j] ... i th pokemon and j pokemons
            #plus pokemon

            for k in range(i):
                data1, plus = addPokemon(dpTable[k][j-1][1], pokeData[i-1][1:])
                if k == 0:
                    tmpMax = plus
                    tmpData = data1
                    tmpPoke = k
                elif plus > tmpMax:
                    # print('lag')
                    tmpMax = plus
                    tmpData = data1
                    tmpPoke = k
            dpTable[i][j][0] = dpTable[tmpPoke][j-1][0] + [i]
            dpTable[i][j][1] = tmpData
            # print(dpTable[i][j][0])

        print('\r%d' % (i), end='')
    # print(type(dpTable))
    with open('./train_data03/dpPt.txt', 'w') as f:
        f.write('\n'.join(map(str,dpTable)))
        # f.write('\n')
    dpTable = [i[-1] for i in dpTable]

    with open('./train_data03/dpPt-6.txt', 'w') as f:
        f.write('\n'.join(map(str,dpTable)))

    tmp = 0
    data = []
    for i in dpTable:
        if tmp < sum(i[1]):
            tmp = sum(i[1])
            data = i[0]
    print(tmp, data)
    for i in data:
        print(pokeName[i])