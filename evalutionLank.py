path = './train_data00/'
fileName = '/evaluation009.txt'
pokes = []
for i in range(37):
    pokes.extend(open(path + str(i).zfill(3) + fileName).read().split('\n'))

pokeScore = dict()
pokeList = list()
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
    exit()


pokeData = list()
for i in pokeScore:
    spe = [j for j in pokeList if j[1] == i[0]]
    spe = sorted(spe, key=lambda x: float(x[0]), reverse=True)
    spe = ['|'.join(j) for j in spe]
    pokeData.extend(spe)

with open(path + 'result.txt', 'w') as f:
    f.write('\n'.join(pokeData))