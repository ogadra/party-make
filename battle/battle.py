import subprocess

pt1 = "|vanillite|Leppa Berry|Snow Cloak|irondefense,endure,iciclecrash,lightscreen|Impish|252,116,124,0,12,4||31,31,31,31,31,31||50|"
pt2 = "|riolu|Muscle Band|Prankster|attract,drainpunch,dig,detect|Timid|4,0,0,252,0,252||31,0,31,31,31,31||50|"
result = subprocess.run(['node', './bot/.sim-dist/examples/battle-stream-example', pt1, pt2], stdout=subprocess.PIPE, text=True)
data = result.stdout
print(data)
data = data.split('\n')[-2]
print(data)