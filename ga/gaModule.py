import os
import random
import math
import re
from collections import Counter
from .modules import item
from .modules import ability
from .modules import move
from .modules import stats

def pChoice(epsilon):
    if epsilon > random.random():
        return True
    else:
        return False

def heredity(dna1, dna2, elem, prob):
    if pChoice(prob):
        return dna1[elem] if random.randrange(2) else dna2[elem]
    else:
        return False

def randomChoice(population, weights, ignore='False'):
    if ignore != 'False':
        weights[ignore] = 0
    if sum(weights) > 0:
        return random.choices(population, weights=weights)[0]
    else:
        return False

def heredityMove(dna1, dna2, species):
    moves = dna1.split(',')
    moves.extend(dna2.split(','))
    if len(moves) < 4:
        return ','.join(moves)

    moves = Counter(moves)
    moves, weight = [i for i in moves.keys()], [i for i in moves.values()]
    childMoves = []
    ignore = 'False'
    for i in range(3):
        selectmove = randomChoice(moves, weight, ignore)
        if selectmove:
            childMoves.append(selectmove)
            ignore = moves.index(selectmove)
        else:
            return ','.join(childMoves)
        # print(weight)
    if pChoice(0.1):
        childMoves.append(randomChoice(moves, weight, ignore))
    else:
        randomMove = move.selectMove(species).split(',')
        for i in randomMove:
            if not i in childMoves:
                childMoves.append(i)
                break

    return ','.join(childMoves)

def cross(parent1, parent2):
    dna1 = parent1.split('|')
    dna2 = parent2.split('|')
    species = dna1[1]
    child = ['']*12
    child[1] = species
    child[10] = '50'

    child[2] = i if (i:=heredity(dna1, dna2, 2, 0.5)) else item.selectItem(species)
    child[3] = i if (i:=heredity(dna1, dna2, 3, 0.8)) else ability.selectability(species)
    if pChoice(0.6):
        if random.randrange(2):
            child[5:9] = dna1[5:9]
        else:
            child[5:9] = dna2[5:9]
    else:
        child[5:9] = stats.showdownpt().split('|')
    
    child[4] = heredityMove(dna1[4], dna2[4], species)
    return '|'.join(child)


def ga(parents, parentCnt=25):

    generateCnt = len(parents)
    parents = parents[:parentCnt]
    parents = [re.sub('\d+\.*\d* \|', '|', i, 1) for i in parents]

    children = []

    for i in range(generateCnt // parentCnt):
        weight = [math.sqrt(parentCnt-i) for i in range(parentCnt)]
        parent1 = parents[i]

        for j in range(parentCnt):
            parent2 = randomChoice(parents, weight, i)
            children.append(cross(parent1, parent2))

    return children
    
        