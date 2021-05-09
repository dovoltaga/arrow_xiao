# arrow_xiao

Seeeduino XIAOをコントローラーに使用し、
CircuitPythonでファームウエアを記述したカーソルキーだけのキーボードです。

## データ

| ファームウエア | main.py        |
| プレートデータ | arrow_case.pdf |

PCBはsu120を使用しました。

## 回路図

XIAOの各GPIOピンとキーマトリックスのrow,colは下記のように接続します。

```
       col0    col1    col2
        = D4    = D5    = D6
             +------+
row0         |      |
 = D2        |  UP  |
             |      |
      +------+------+-------+
row1  |      |      |       |
 = D3 | LEFT | DOWN | RIGHT |
      |      |      |       |
      +------+------+-------+
```

## ファームウエア

公式のドキュメント(https://wiki.seeedstudio.com/jp/Seeeduino-XIAO-CircuitPython/)を参考に
CircuitPythonのブートローダーをXIAOにインストールしてください。

HIDデバイスとして使用するためにライブラリーをCircuitPythonのサイト(https://circuitpython.org/libraries)からダウンロードして,
adafruit_hidフォルダごとXIAOのlibフォルダへコピーしてください。

このリポジトリのmain.pyをXIAOにコピーしてください。

## 動作について

どれかキーを押している間はXIAOの黄色のLEDが点灯します。

３つのキーを同時押しした場合は20秒ごとにカーソルが自動的に上下、下上、左右、右左に動作します、どれかキーを押し続けていれば止まります。
