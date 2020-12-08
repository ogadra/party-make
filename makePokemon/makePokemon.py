import item
import ability
import move
import stats
from numpy import random
import json
import time

def returnValues(vals):
    tmp = [[val, key] for key, val in vals.items()]
    vals = str()
    for i in range(6):
        vals += str(tmp[i][0]) + ' ' + str(tmp[i][1])
        if i != 5:
            vals += ' / '

    return vals

if __name__ == "__main__":
    pokemons = open('./data/delibird-single-eng.txt').read().split('\n')
    with open('./data/pokedex.json') as f:
        pokedex = json.load(f)


    # format = "NICKNAME|SPECIES|ITEM|ABILITY|MOVES|NATURE|EVS|GENDER|IVS|SHINY|LEVEL|HAPPINESS,POKEBALL,HIDDENPOWERTYPE"
    for i in range(6):
        pokemon = [''] * 9
        pokemon[1] = random.choice(pokemons)

        pokemon[2] = item.selectItem(pokemon[1])
        pokemon[3] = ability.selectability(pokemon[1])
        # pokemon[4] = stats.generate()
        pokemon[4] = move.selectMove(pokemon[1])
        pokemon[5] = stats.showdownpt()

        print(*pokemon, sep='|',end='')
        if not i == 5:
            print(']', end='')
        else:
            print()

        # print(pokedex[pokemon['name']]['name'] + ' @ ' + pokemon['item'])
        # print('Ability: ' + pokemon['ability'])
        # print('EVs: ', end='')
        # print(returnValues(pokemon['stats']['EVs']))
        # print(pokemon['stats']['name'], 'Nature')
        # print(returnValues(pokemon['stats']['IVs']))
        # for i in pokemon['moves']:
        #     print('- ' + i)
        
        # print()