from battle import bruteforce
from ga import gaModule
import time 
import random
import numpy as np

if __name__ == '__main__':
    path = './train_data02/'
    dataSet = open(path + 'default.txt').read().split('\n')
    speciesCnt = 20
    opponent = [dataSet[i*20] for i in range(speciesCnt)]


    for i in range(500):
        gaData = open(path + 'generate' + str(i).zfill(3) + '.txt').read().split('\n')
        battleData = gaData[0:360]
        selected = []
        for j in random.sample(range(15,80), k=5):
            battleData.extend(gaData[j*24: (j+1)*24])
            selected.append(j)
        selected.sort(reverse=True)
        for j in selected:
            gaData[j*24:(j+1)*24] = []

        gaData[0:360] = []
        evalList = list()

        #battle function
        for j in range(speciesCnt):
            evalData = bruteforce.bruteforce(battleData[j*24:(j+1)*24], opponent)
            evalList.extend(evalData)
        
        pokeScore = dict()
        pokeList = list()
        for poke in evalList:
            data = poke.split('|')
            if data[1] in pokeScore:
                pokeScore[data[1]] += int(data[0])
            else:
                pokeScore[data[1]] = int(data[0])
            pokeList.append(data)

        pokeScore = sorted(pokeScore.items(), key=lambda x: x[1], reverse=True)
        # sort only pokemon species

        pokeData = list()
        for i in pokeScore:
            spe = [j for j in pokeList if j[1] == i[0]]
            spe = sorted(spe, key=lambda x: float(x[0]), reverse=True)
            spe = ['|'.join(j) for j in spe]
            pokeData.extend(spe)
        # sort from species and mu

        pokeData.extend(gaData)
        
        with open(path + 'evalution' + str(i).zfill(3) + '.txt', 'w') as f:
            f.write('\n'.join(pokeData))
        # save evalution data

        nextGeneration = list()
        for j in range(speciesCnt):
            nextGeneration.extend(gaModule.ga(pokeData[j*24:(j+1)*24], 8))
        
        nextGeneration.extend(gaData)
        with open(path + 'generate' + str(i+1).zfill(3) + '.txt', 'w') as f:
            f.write('\n'.join(nextGeneration))