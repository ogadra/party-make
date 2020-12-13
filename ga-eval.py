from battle import TrueSkillModule
from ga import gaModule

pokemon = 'abra'
for i in range(100):
    TrueSkillModule.evalBattle(pokemon)
    gaModule.ga(pokemon)