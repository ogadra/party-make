import random
import numpy as np
import json
from copy import copy

natures = json.load(open('./data/natures.json'))
stasList = ['HP', 'Atk', 'Def', 'SpA', 'SpD', 'Spe']
natureWeight = []

for key, item in natures.items():
    if item['minus'] == 'Atk' or item['minus'] == 'SpA':
        natureWeight.append(3)
    elif item['minus'] == 'Spe':
        natureWeight.append(2)
    else:
        natureWeight.append(1)

def pChoice(epsilon):
    if epsilon > random.random():
        return True
    else:
        return False

def choicePoint(nature, count):
    if nature['name'] == 'Serious':
        points = np.random.choice(stasList, size=count, replace=False)
    elif count == 3:
        prob = np.array([0.125]*6)
        prob[stasList.index(nature['plus'])] = 0.5
        prob[stasList.index(nature['minus'])] = 0
        points = np.random.choice(stasList, size=3, replace=False, p=prob)
    elif count == 5:
        points = copy(stasList)
        points.remove(nature['minus'])

    return points

def EVcalc(pokemon, nature, count):
    w = [0] * 6
    points = choicePoint(nature, count)
    for i in points:
        w[stasList.index(i)] = 1
        pokemon['EVs'][i] = 4
    if nature['plus'] in points:
        w[stasList.index(nature['plus'])] += 1
    
    roopCount = 62 if count == 3 else 61
    for i in range(roopCount):
            incrementPoint = random.choices(stasList, weights=w)[0]
            pokemon['EVs'][incrementPoint] += 8
            if pokemon['EVs'][incrementPoint] == 252:
                w[stasList.index(incrementPoint)] = 0
            else:
                w[stasList.index(incrementPoint)] += 1
    return pokemon

def generate():
    pokemon = {'EVs':{'HP':0, 'Atk':0, 'Def':0, 'SpA':0, 'SpD':0, 'Spe':0}, 'IVs':{'HP':31, 'Atk':31, 'Def':31, 'SpA':31, 'SpD':31, 'Spe':31}}
    
    nature = random.choices(list(natures.keys()),weights=natureWeight)[0]

    # nature = 'bold'
    # nature = 'serious'

    nature = natures[nature]
    pokemon.update(nature)

    if nature['minus'] == 'Atk' or nature['minus'] == 'Spe':
        pokemon['IVs'][nature['minus']] = 0 if random.randrange(3) else 31
    
    if pChoice(0.7):
        # 3points
        if nature['plus'] == 'Spe':
            pokemon['EVs']['Spe'] = 252
            weight = [10, 92, 3, 92, 3, 0]
            weight[stasList.index(nature['minus'])] = 0

            tmp = random.choices(stasList, weights=weight)[0]
            pokemon['EVs'][tmp] = 252
            if pokemon['EVs']['HP'] == 0:
                pokemon['EVs']['HP'] = 4
            elif nature['minus'] != 'SpD':
                pokemon['EVs']['SpD'] = 4
            else:
                pokemon['EVs']['Def'] = 4

        elif nature['plus'] == 'Atk' or nature['plus'] == 'SpA':
            pokemon['EVs'][nature['plus']] = 252
            weight = [49, 0, 1, 0, 1, 49]
            weight[stasList.index(nature['minus'])] = 0
            tmp = random.choices(stasList, weights=weight)[0]
            pokemon['EVs'][tmp] = 252
            if pokemon['EVs']['Spe'] == 0 and nature['minus'] == 'Spe':
                pokemon['EVs']['Spe'] = 4
            elif pokemon['EVs']['HP'] == 0:
                pokemon['EVs']['HP'] = 4
            else:
                pokemon['EVs']['SpD'] = 4
        else:
            points = choicePoint(nature, 3)
            for i in points[:2]:
                pokemon['EVs'][i] = 252
            pokemon['EVs'][points[-1]] = 4

    else:
        count = 3 if pChoice(0.7) else 5
        pokemon = EVcalc(pokemon, nature, count)

        # 5points
        pass
    return pokemon

def showdownpt():
    stats = generate()
    returnstr = stats['name']
    returnstr += '|'
    returnstr += ','.join(map(str,list((stats['EVs'].values()))))
    returnstr += '||'
    returnstr += ','.join(map(str,list((stats['IVs'].values()))))

    return returnstr


if __name__ == '__main__':
    pokemon = generate()
    pokemon = showdownpt()


    # print(sum(generate()['EVs'].values()))

    # for i in range(100000):
    #     tmp = generate()
    #     if sum(tmp['EVs'].values()) != 508:
    #         print(tmp)