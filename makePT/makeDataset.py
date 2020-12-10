# No.1 argv is how many pokemons and No.2 argv is which pokemon data do i use

from modules import item
from modules import ability
from modules import move
from modules import stats

from numpy import random
import json
import time
import sys
import os

def makeParties(cnt=1):
    # format = "NICKNAME|SPECIES|ITEM|ABILITY|MOVES|NATURE|EVS|GENDER|IVS|SHINY|LEVEL|HAPPINESS,POKEBALL,HIDDENPOWERTYPE"
    party = str()

    for i in range(cnt):
        pokemon = [''] * 9
        pokemon[1] = random.choice(pokemons)

        pokemon[2] = item.selectItem(pokemon[1])
        pokemon[3] = ability.selectability(pokemon[1])
        # pokemon[4] = stats.generate()
        pokemon[4] = move.selectMove(pokemon[1])
        pokemon[5] = stats.showdownpt()
        pokemon[7] = 50
        pokemon = list(map(str, pokemon))
        party += '|'.join(pokemon)
        if not i == cnt - 1:
            party += ']'
        else:
            pass
    return party



if __name__ == "__main__":
    pokemons = open('./data/delibird-single-eng.txt').read().split('\n')
    dataset = []

    if len(sys.argv) > 1:
        cnt = int(sys.argv[1])
        if len(sys.argv) > 2:
            savedir = './pokemons/' + str(sys.argv[2]) + '/'
    else:
        cnt = 1



    for i in range(cnt):
        pokemon = [''] * 9
        if len(sys.argv) <= 2:
            pokemon[1] = random.choice(pokemons)
        else:
            pokemon[1] = str(sys.argv[2])

        pokemon[2] = item.selectItem(pokemon[1])
        pokemon[3] = ability.selectability(pokemon[1])
        pokemon[4] = move.selectMove(pokemon[1])
        pokemon[5] = stats.showdownpt()
        pokemon[7] = 50
        # print(*pokemon, sep='|',end='')
        dataset.append('|'.join(list(map(str,pokemon))))
    

    num = sum(os.path.isfile(os.path.join(savedir, name)) for name in os.listdir(savedir))
    with open (savedir + str(num).zfill(4) + '.txt', 'w') as f:
        for i in dataset:
            f.write(i)
            f.write('\n')
    
