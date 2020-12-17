from battle import TrueSkillModule
from ga import gaModule
import time 

pokemon = 'abra'
for i in range(100):
    s = time.time()
    TrueSkillModule.evalBattle(pokemon)
    gaModule.ga(pokemon)
    print('')
    print('roop:',i, s-time.time())