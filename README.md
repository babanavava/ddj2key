# ddj2key

よ！Pioneer DJの DDJシリーズのDJコントローラーのパフォーマンスパッドとデックボタンをキーボード入力に変換するプログラム作ったよ！

## 注意事項

このプログラムはDDJ-400でしか動作確認してないから、他の機器では動作するかどうか保証はできかねるよ！

でも多分動くと思うよ！

## 使い方よ！(windows限定よ！)

1. 下のところから[**ddj2key-win.zip**](https://github.com/babanavava/ddj2key/releases/download/v0.0.0/ddj2key-win.zip)をダウンロードするよ！

2. ファイルマネージャーを開きダウンロードした**ddj2key-win.zip**を選択し「**すべて展開**」を選択して、展開するよ！

3. rekordboxなど他のmidiソフトウェアが起動していないかを確認し、DDJシリーズのDJコントローラーを接続するよ！

4. ddj2key-winフォルダ内の**ddj2key.exe**をダブルクリックして「**WindowsによってPCが保護されました**」と出た場合は[詳細情報](https://github.com/babanavava/ddj2key/releases/edit/v0.0.0)をクリックして、**実行**をクリックよ！

5. 現れたウィンドウの"Start"をクリックして、DDJのパフォーマンスパッドを適当に押してメモ帳などに文字が入力されるかを確認するよ！

6. もし入力されなければ ddj2key-winフォルダ内の**pygame_midi_device_detector.exe**を起動するよ！

7. I/O列の**Input**とある行の、NameがDDJ-###となっている行の左端のDevice IDとなる数字を覚えてくれよ！(もし無ければ接続/認識がきちんとされていないか、他のInputとあるDevice IDを総当たりしてみてくださいよ！)

8. ddj2key-win内の**config.ini**をメモ帳などにドラッグアンドドロップしてくれよ！

9. `midi_input_device_id = 1`とあるところの`1`をさっき覚えたDevice IDに変えてくれよ！

10.  もう一度**ddj2key.exe**をダブルクリックして起動するよ！

11. これで文字入力がなされなければ、また`midi_input_device_id`の数字を適当に変えてみてくれよ！これで出来なければもう無理ですわよ！

## windows以外の民よ！

このプログラムは普通のパイソンで作られているので、
```sh
$ git clone https://github.com/babanavava/ddj2key.git
$ cd ddj2key
$ py -m venv .venv
$ . .venv/bin/activate
$ py -m pip install -r requirements.txt
$ py ddj2key.py
```
こんな感じで起動できると思うよ！

windowsでも出来るけどよ！

## configs
プリセットとして5つconfig.iniファイルを作っておいたよ！ddj2key.exeがあるフォルダのconfig.iniを上書きすればすぐに使うことが出来るよ！

それぞれどのような配置か説明するよ！

### leverless
デフォルトの配置で、WASDが格ゲーのレバーレスコントローラーのように配置されている配置だよ！

元々このプログラムはDJコントローラーがスト6に使えるのではないかと思って作られたものだったからこれがデフォルトになってるよ！
![leverless](/configs/leverless(default)/leverless_layout.png)

### WASD
左手部分がWASDを含む通常のQWERTY配列の配置となっていて、キーボードを使ったゲームがやりやすそうな配置だよ！
![WASD](/configs/WASD/WASD_layout.png)

### leverless_arrow
leverlessのWASD部分を矢印キーに置き換えたものだよ！
![leverless_arrow](/configs/leverless_arrow/leverless_arrow_layout.png)

### arrow_right
矢印キーがキーボードと同様の配置で右側にある配置だよ！
![arrow_right](/configs/arrow_right/arrow_right_layout.png)

### arrow_left
WASDのWASD部分を矢印キーで置き換えたような配置だよ！
![arrow_right](/configs/arrow_left/arrow_left_layout.png)

## config.iniは自由よ！
上記のキー配置は全てconfig.iniの中に書かれてるから、それを自由に書き換えて君だけのオリジナル配置を作ることもできるよ！

config.iniファイル内のキーがそれぞれDDJ-400上でどのボタンを指しているのかを示した画像を以下に置いておくよ！これを参考にして作ってみてくれよ！
![ddj_config](/image/ddj_config_layout.png)



## ライセンス
自由に使っていいよ！派生してもっといいアプリ作ってもらってもいいよ！
