from battle import TrueSkillModule
from ga import gaModule
import time 
import numpy as np

target = list(range(37))
matchCount = 24

for i in target:
    path = './train_data/' + str(i).zfill(3) + '/'
    print('set:',i)
    # pokemons = open(path + 'generate000.txt').read().split('\n')
    for j in range(10):
        s = time.time()
        pokemons = TrueSkillModule.evalBattle(path + 'generate' + str(j).zfill(3) + '.txt', matchCount)
        with open(path + 'evaluation' + str(j).zfill(3) + '.txt', 'w') as f:
            f.write('\n'.join(pokemons))
        nextGeneration = list()
        for i in range(5):
            nextGeneration.extend(gaModule.ga(pokemons[i*20:(i+1)*20], 10))
        
        print(*nextGeneration, sep='\n')
        with open(path + 'generate' + str(j+1).zfill(3) + '.txt', 'w') as f:
            f.write('\n'.join(nextGeneration))

        print('roop:',j, time.time()-s)
        exit()
