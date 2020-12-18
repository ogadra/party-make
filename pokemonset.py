from battle import TrueSkillModule
from ga import gaModule
import time 
import numpy as np

pokemons = open('./data/delibird-single-eng.txt').read().split('\n')

ignore = ['cosmog', 'ditto', 'pikachu']
for i in ignore:
    pokemons.remove(i)

np.random.shuffle(pokemons)
pokemons = np.array(pokemons).reshape(-1,5).tolist()

with open ('./train_data/pokemonset.txt', 'w') as f:
    # f.write('\n'.join(pokemons))
    for i in pokemons:
        f.write(','.join(i))
        f.write('\n')