# ddj2key

よ！Pioneer DJの DDJシリーズのDJコントローラーのパフォーマンスパッドとデックボタンをキーボード入力に変換するプログラム作ったよ！

## 注意事項よ！

このプログラムはDDJ-400でしか動作確認してないから、他の機器では動作するかどうか保証はできかねるよ！

でもDDJシリーズなら多分動くと思うよ！

それと、rekordboxなど対象のMIDIデバイスを使用するソフトウェアは同時に使用できないから注意よ！

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

このプログラムは普通のパイソンで作られているので、パイソンとギットを入れてから
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

## configsよ！
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

## config.iniの説明よ！
上記のキー配置は全てconfig.iniの中に書かれてるから、それを自由に書き換えて君だけのオリジナル配置を作ることもできるよ！

### miscセクションの説明よ！
- `midi_input_device_id`キーは、pygame.midiモジュールでのデバイスIDでどのデバイスを使用するかを決めるものだよ！(デフォルトは`1`よ！)
- `pad_all`キーは`pad_all`セクション`pad_all_shift`セクションのボタン配置をDDJのHotCueやBeatLoopモードなど全てのモードにおいて適応させるものだよ！`0`にするとその他のモード名のセクションごとに配置を決めることが出来るようになるよ！(デフォルトは`1`よ！)
- `all_space`キーは`1`にするとこのプログラムで割り当て可能などのボタンを押してもSPACEキーが入力されるようになるよ！(デフォルトは`0`よ！)

### マッピングよ！
config.iniファイル内の`misc`以外のセクションのキーがそれぞれDDJ-400上でどのボタンを指しているのかを示した画像を以下に置いておくよ！これを参考にして作ってみてくれよ！
![ddj_config](/image/ddj_config_layout.png)
`deck`セクションは`D4L`、`D4R`を除いた、`D1L`から`D11R`まで割り当てることが出来、`deck_shift`セクションはshiftを押した状態の`deck`セクションのボタン配置なので、shiftボタン本人である`D11L`、`D11R`は割り当てられないよ！

勘の良い読者ならお分かりだと思うが、モード名のセクションや`pad_all`セクションの名前の末尾に'_shift'とついているのはshiftを押した状態のそのモードのボタンを割り当てれるよ！

#### D4LとD4Rが無い理由
[DDJ-400 MIDI-compatible software – AlphaTheta Help Center](https://support.pioneerdj.com/hc/ja/articles/4405094309657-DDJ-400-MIDI-compatible-software)👈そもそもこのリンクの[MIDIメッセージ一覧](https://www.pioneerdj.com/-/media/pioneerdj/software-info/controller/ddj-400/ddj-400_midi_message_list_j1.pdf)に準拠してボタン名は決めていますよ！

`D4L`、`D4R`がないのはその中でにボタンじゃなかったためなくなりましたよ

## ライセンスよ！
自由に使っていいよ！派生してもっといいアプリ作ってもらってもいいよ！

## クレジットよ！
- [DDJ-400](https://www.pioneerdj.com/ja-jp/product/controller/archive/ddj-400/black/overview/) (https://www.pioneerdj.com/ja-jp/product/controller/archive/ddj-400/black/overview/)

