import random
import json

natures = json.load(open('../data/natures.json'))

pokemon = {'EVs':{'HP':0, 'Atk':0, 'Def':0, 'SpA':0, 'SpD':0, 'Spe':0}, 'IVs':{'HP':31, 'Atk':31, 'Def':31, 'SpA':31, 'SpD':31, 'Spe':31}}
nature = random.choice(list(natures.keys()))

# nature = 'bold'
nature = natures[nature]

if nature['minus'] == 'Atk' or nature['minus'] == 'Spe':
    pokemon['IVs'][nature['minus']] = 0 if random.randrange(2) else 31


print(pokemon)

