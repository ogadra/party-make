from battle import TrueSkillModule
from ga import gaModule
from makePT import makePokemon
import time 
import numpy as np

pokemons = open('./train_data/pokemonset.txt').read().split('\n')
pokemons = [i.split(',') for i in pokemons]

for i,poke in enumerate(pokemons):
    path = './train_data/' + str(i).zfill(3) + '/'
    dataset = list()
    poke.sort()
    for j in poke:
        dataset += makePokemon.makeDataset(j,20)
    with open(path + 'generate000.txt', 'w') as f:
        f.write('\n'.join(dataset))
    print(*dataset, sep='\n')