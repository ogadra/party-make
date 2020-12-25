import sys
import os
import re
import time 
import random
from math import log

def calcScore(x):
    return 0.8/(1+5**(3-x))


def addPokemon(arg1, arg2):
    ans = [1 - (1 - arg1[i]) * (1 - arg2[i]) for i in range(80)]
    return ans, sum(ans)


if __name__ == "__main__":
    dpTable = [[[[],[0]*80] for j in range(7)] for i in range(81)]
    
    #data processing to sigmoid value
    #do()
    pokeData = open()

    #dp
    for i in range(1,81):
        for j in range(1,7):
            #about dp[i][j] ... i th pokemon and j pokemons
            #plus pokemon

            for k in range(i):
                data1, plus = addPokemon(dpTable[k][j-1][1], pokeData[i-1])
                if k == 0:
                    tmpMax = plus
                    tmpData = data1
                    tmpPoke = k
                elif plus > tmpMax:
                    tmpMax = plus
                    tmpData = data1
                    tmpPoke = k
            dpTable[i][j][0] = dpTable[tmpPoke][j-1][0] + [j]
            dpTable[i][j][1] = tmpData
