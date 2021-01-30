[English](./README.md) / __日本語__

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
を実行すると自動対戦が行われます。対戦ログが英語で表示されます。

技選択は、様々な可能性を探索してより良いものを選ぶアルゴリズムで行っています。
[詳細はこちら。](https://shingaryu.hatenablog.com/entry/2020/02/03/002226)

技選択の探索に用いる時間を指定する箇所は

./bot/.sim-dist/tools/ にある

random-player-ai.js の 1114行目を編集してください。

デフォルトは300ミリ秒です。

学習を行うには、nodeモジュールの以下の箇所をコメントアウトしてから行ってください。
./bot/node_modules/nedb/lib/ にある

datastore.js の 76行目 ~ 78行目
```
   if (this.autoload) { this.loadDatabase(options.onload || function (err) {
     if (err) { throw err; }
   }); }
```
をコメントアウトしてください。

学習するには
```
python ga-eval-somepoke.py
```
を実行します。

## setting

ダイマックスを利用する場合は

bot/.sim-dist/tools/bots/ にある

minimaxbot.js の 283行目
```
useDynamax = false
```
を`true`に書き換えてください。

このアルゴリズムではダイマックスを対戦開始直後に使ってしまうため、あまり良く学習できません。そのためデフォルトでは`false`になっています。