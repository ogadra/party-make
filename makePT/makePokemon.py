from .modules import item
from .modules import ability
from .modules import move
from .modules import stats


from numpy import random
import json
import time

def makePokemon(specy):
    # format = "NICKNAME|SPECIES|ITEM|ABILITY|MOVES|NATURE|EVS|GENDER|IVS|SHINY|LEVEL|HAPPINESS,POKEBALL,HIDDENPOWERTYPE"

    pokemon = [''] * 9
    pokemon[1] = specy

    pokemon[2] = item.selectItem(specy)
    pokemon[3] = ability.selectability(specy)
    # pokemon[4] = stats.generate()
    pokemon[4] = move.selectMove(specy)
    pokemon[5] = stats.showdownpt()
    pokemon[7] = 50
    pokemon = list(map(str, pokemon))
    party = '|'.join(pokemon)

    return party

def makeDataset(pokemon, cnt):
    dataset = list()
    for i in range(cnt):
        dataset.append(makePokemon(pokemon))
    return dataset




if __name__ == "__main__":
    

    # format = "NICKNAME|SPECIES|ITEM|ABILITY|MOVES|NATURE|EVS|GENDER|IVS|SHINY|LEVEL|HAPPINESS,POKEBALL,HIDDENPOWERTYPE"
    times = 1
    for i in range(times):
        pokemon = [''] * 9
        pokemon[1] = random.choice(pokemons)

        pokemon[2] = item.selectItem(pokemon[1])
        pokemon[3] = ability.selectability(pokemon[1])
        # pokemon[4] = stats.generate()
        pokemon[4] = move.selectMove(pokemon[1])
        pokemon[5] = stats.showdownpt()
        pokemon[7] = 50
        print(*pokemon, sep='|',end='')
        if not i == times-1:
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