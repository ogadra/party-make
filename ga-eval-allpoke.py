from battle import TrueSkillModule
from ga import gaModule
import time 
import numpy as np
import os


if __name__ == '__main__':

    path = './train_data02'
    tmp = ''
    path = [path + i for i in ['_latias/', '_zekrom/', '/']]
    pokemons = []
    for directory in path:
        num = 0
        while os.path.isfile(directory + 'evalution' + str(num).zfill(3) + '.txt'):
            num += 1
        num -= 1
        tmp = open(directory + 'evalution' + str(num).zfill(3) + '.txt').read().split('\n')
        for i in range(len(tmp)//24):
            pokemons.extend(tmp[i*24:i*24+8])
    matchCount = 144

    path = './train_data03/pokemons.txt'
    # with open(path, 'w')as f:
    #     f.write('\n'.join(pokemons))
    open(path, 'w').write('\n'.join(pokemons))

    pokemons = TrueSkillModule.evalBattle(path, matchCount)
    with open('./train_data03/evalution.txt', 'w') as f:
        f.write('\n'.join(pokemons))