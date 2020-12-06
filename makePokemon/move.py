import json
import re
from numpy import random
import time

moves = json.load(open('../data/learnsets.json'))

def selectMove(pokemon):
    ableMoves = [i for i, val in moves[pokemon]['learnset'].items() if [j for j in val if re.match('8\w*', j)]]
    selectedMoves = random.choice(ableMoves, 4)
    return selectedMoves

if __name__ == '__main__':
    # moves = selectMove('nidoranm')
    for i in range(500):
        print(selectMove('nidoranm'))
        time.sleep(0.1)