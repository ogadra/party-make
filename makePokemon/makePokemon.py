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

    for i in range(6):
        pokemon = dict()
        pokemon['name'] = random.choice(pokemons)
        pokemon['item'] = item.selectItem(pokemon['name'])
        pokemon['ability'] = ability.selectability(pokemon['name'])
        pokemon['stats'] = stats.generate()
        pokemon['moves'] = move.selectMove(pokemon['name'])

        print(pokedex[pokemon['name']]['name'] + ' @ ' + pokemon['item'])
        print('Ability: ' + pokemon['ability'])
        print('EVs: ', end='')
        print(returnValues(pokemon['stats']['EVs']))
        print(pokemon['stats']['name'], 'Nature')
        print(returnValues(pokemon['stats']['IVs']))
        for i in pokemon['moves']:
            print('- ' + i)
        
        print()