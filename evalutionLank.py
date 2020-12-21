path = './train_data01/'
fileName = '/evaluation009.txt'
pokes = []
for i in range(16):
    pokes.extend(open(path + str(i).zfill(3) + fileName).read().split('\n'))

pokeScore = dict()
pokeList = list()
# pokeList is list of pokemonData

for poke in pokes:
    data = poke.split('|')
    if data[1] in pokeScore:
        pokeScore[data[1]] += float(data[0])
    else:
        pokeScore[data[1]] = float(data[0])
    pokeList.append(data)

pokeScore = sorted(pokeScore.items(), key=lambda x: x[1], reverse=True)
with open(path + 'ranking.txt', 'w') as f:
    for i in pokeScore:
        f.write(i[0])
        f.write('\n')



pokeData = list()
for i in pokeScore:
    spe = [j for j in pokeList if j[1] == i[0]]
    spe = sorted(spe, key=lambda x: float(x[0]), reverse=True)
    spe = ['|'.join(j) for j in spe]
    pokeData.extend(spe)
# sort from species and mu

with open(path + 'result.txt', 'w') as f:
    f.write('\n'.join(pokeData))


from others import pokemonTr
with open(path + 'resultJP.txt', 'w') as f:
    
    for i in pokeScore:
        f.write(pokemonTr.translate(i[0]))
        f.write('\n')