import json
import re
from numpy import random
import time

moves = json.load(open('./data/learnsets.json'))

def selectMove(pokemon):
    ableMoves = [i for i, val in moves[pokemon]['learnset'].items() if [j for j in val if re.match('8\w*', j)]]
    selectedMoves = list(random.choice(ableMoves, 4, replace=False))
    return selectedMoves

if __name__ == '__main__':
    # moves = selectMove('nidoranm')
    for i in range(50000):
        tmp = selectMove('wooper')
        if len(set(tmp)) != 4:
            print(tmp)
        # time.sleep(0.5)