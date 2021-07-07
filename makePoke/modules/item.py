import json
from numpy import random

itemlist = open('./data/available-item.txt').read().split('\n')
itemlist.remove('thickclub')
with open('./data/items.json', 'r') as f:
    items = json.load(f)

def pChoice(epsilon):
    if epsilon > random.rand():
        return True
    else:
        return False

def selectItem(pokemon=False):
    if pokemon == 'cubone':
        if pChoice(0.6):
            return 'thickclub'
        else:
            pass
    return items[random.choice(itemlist)]['name']

if __name__ == '__main__':
    tmp = selectItem()
    print(tmp)
    print(type(tmp))
    # print(items[tmp]['name'])