import random
import numpy as np
import json

natures = json.load(open('../data/natures.json'))
stasList = ['HP', 'Atk', 'Def', 'SpA', 'SpD', 'Spe']

def pChoice(epsilon):
    if epsilon > random.random():
        return True
    else:
        return False

def choicePoint(nature, count):
    if count == 3:
        if nature['name'] == 'Serious':
            points = np.random.choice(stasList, size=3, replace=False)

        else:
            prob = np.array([0.1]*6)
            prob[stasList.index(nature['plus'])] = 0.5
            points = np.random.choice(stasList, size=3, replace=False, p=prob)
    else:
        points = []
        pass
    return points

def generate():
    pokemon = {'EVs':{'HP':0, 'Atk':0, 'Def':0, 'SpA':0, 'SpD':0, 'Spe':0}, 'IVs':{'HP':31, 'Atk':31, 'Def':31, 'SpA':31, 'SpD':31, 'Spe':31}}
    
    nature = random.choice(list(natures.keys()))

    # nature = 'bold'
    # nature = 'serious'

    nature = natures[nature]
    pokemon.update(nature)

    if nature['minus'] == 'Atk' or nature['minus'] == 'Spe':
        pokemon['IVs'][nature['minus']] = 0 if random.randrange(2) else 31


    if pChoice(0.1):
        if nature['plus'] == 'Spe':
            pokemon['EVs']['Spe'] = 252
            tmp = random.choices(stasList, weights=[10, 92, 3, 92, 3, 0])[0]
            pokemon['EVs'][tmp] = 252
            if pokemon['EVs']['HP'] == 0:
                pokemon['EVs']['HP'] = 4
            else:
                pokemon['EVs']['SpD'] = 4

        elif nature['plus'] == 'Atk' or nature['plus'] == 'SpA':
            pokemon['EVs'][nature['plus']] = 252
            tmp = random.choices(stasList, weights=[49, 0, 1, 0, 1, 49])[0]
            pokemon['EVs'][tmp] = 252

            if pokemon['EVs']['Spe'] == 0:
                pokemon['EVs']['Spe'] = 4
            else:
                pokemon['EVs']['HP'] = 4
        else:
            points = choicePoint(nature, 3)
            for i in points[:2]:
                pokemon['EVs'][i] = 252
            pokemon['EVs'][points[-1]] = 4

    else:
        w = [0]*6
        points = choicePoint(nature, 3)
        
        for i in points:
            w[stasList.index(i)] = 1
            pokemon['EVs'][i] = 4

        if nature['plus'] in points:
            w[stasList.index(nature['plus'])] += 1
        
        for i in range(62):
            incrementPoint = random.choices(stasList, weights=w)[0]
            pokemon['EVs'][incrementPoint] += 8
            if pokemon['EVs'][incrementPoint] == 252:
                w[stasList.index(incrementPoint)] = 0
            else:
                w[stasList.index(incrementPoint)] += 1
    
    return pokemon

if __name__ == '__main__':
    pokemon = generate()

    # print(sum(generate()['EVs'].values()))