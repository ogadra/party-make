# abilities can be confirm in pokedex.json
import json
from numpy import random

with open('./data/pokedex.json', encoding='utf-8') as f:
    pokedex = json.load(f)

def selectability(pokemon):
    abilityList = list(pokedex[pokemon]['abilities'].values())
    return random.choice(abilityList)


if __name__ == "__main__":
    print(selectability('pikachu'))