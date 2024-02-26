# learn_opencv
OpenCVの学習を行うリポジトリ。やりたいことを見つけたら随時追加する

## 環境
Windows11
Python:3.12
OpenCV:4.9.0.80

## 準備
### Pythonのインストール
 - Pythonダウンロードリンクから使用したいバージョンのPythonを指定してダウンロードしてインストール
https://pythonlinks.python.jp/ja/index.html

環境変数を設定する項目にチェックすると自分で環境変数を設定しなくても済むのでチェックするのがおすすめ


#### OpenCVのインストール

opencv-pythonをpipインストールする
```
$ pip install opencv-python
```
opencv-contrib-pythonをpipインストールする
opencv-contrib-pythonはOpenCVの機能を拡張することができる
```
$ pip install opencv-contrib-python
```

#### カスケード分類器
https://github.com/opencv/opencv/tree/master/data/haarcascades

### ディレクトリ
#### cat_face
猫の顔を認識するコードを置くディレクトリ
使用するカスケード分類器
 - https://github.com/opencv/opencv/tree/master/data/haarcascades/haarcascade_frontalcatface_extended.xml
 - https://github.com/wellflat/cat-fancier/blob/master/detector/models/cat/cascade.xml

 ### 参考元
  - https://github.com/se-lina/drone_tello
  - https://rest-term.com/archives/3131/
