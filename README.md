## install and test
```cd bot
npm install
python -m pip install trueskill
python -m pip install numpy 
(or conda install numpy)
```

and in party-make
```
python battle/battle.py
```
to run bot battle test.

select move time -> setting in ./bot/.sim-dist/tools/random-player-ai.js on 1114

learn somepoke

you must be comment out in ./bot/node_modules/nedb/lib/datastore.js on 76 - 78
```
   if (this.autoload) { this.loadDatabase(options.onload || function (err) {
     if (err) { throw err; }
   }); }
```


```
python ga-eval-somepoke.py
```

Dymax setting -> in bot/.sim-dist/tools/random-player-ai.js 203
```
let canPlayerDynamax = false;
```
