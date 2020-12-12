from battle import TrueSkillModule
from ga import gaModule

pokemon = 'garchomp'
for i in range(100):
    TrueSkillModule.evalBattle(pokemon)
    gaModule.ga(pokemon)