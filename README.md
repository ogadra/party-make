__English__ / [日本語](./README-ja.md)

## install and test

You must use Python >= 3.8.

in ./party-make
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

## setting
Dymax setting -> in bot/.sim-dist/tools/bots/minimaxbot.js 283
```
useDynamax = false
```
