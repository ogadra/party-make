__Japanese__ / [English](./README.md)

## インストールとテスト

フォルダparty-makeで以下のコードを実行してください。

```cd bot
npm install
python -m pip install trueskill
python -m pip install numpy 
(or conda install numpy (Anaconda環境のPythonを利用している場合、numpyはcondaでインストール推奨です。))
```

party-makeフォルダに戻り、
```
python battle/battle.py
```
を実行すると自動対戦が行われます。

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
