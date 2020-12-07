import json
import random

itemlist = open('./data/delibird-item-eng.txt').read().split('\n')
itemlist.remove('thickclub')
# with open('./data/items.json', 'r') as f:
#     items = json.load(f)

def pChoice(epsilon):
    if epsilon > random.random():
        return True
    else:
        return False

def selectItem(pokemon=False):
    if pokemon == 'cubone':
        if pChoice(0.6):
            return 'thickclub'
        else:
            pass
    return random.choice(itemlist)

if __name__ == '__main__':
    selectItem()