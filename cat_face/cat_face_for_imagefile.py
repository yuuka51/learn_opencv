#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import sys
import cv2
import os

def detect(imagefilename, cascadefilename):
    srcimg = cv2.imread(imagefilename)
    if srcimg is None:
        print('cannot load image')
        sys.exit(-1)
    dstimg = srcimg.copy()
    cascade = cv2.CascadeClassifier(cascadefilename)
    if cascade.empty():
        print('cannnot load cascade file')
        sys.exit(-1)
    objects = cascade.detectMultiScale(srcimg, 1.1, 3)
    for (x, y, w, h) in objects:
        print(x, y, w, h)
        cv2.rectangle(dstimg, (x, y), (x + w, y + h), (0, 0, 255), 2)
        # cat faceという緑色の文字をrectangleの下に描画させる
        # cv2.putText(dstimg, 'cat face', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        # cat faceという赤色の文字をrectangleの上に描画させる
        cv2.putText(dstimg, 'cat face', (x, y+h+10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    return dstimg

if __name__ == '__main__':
    # image_folder内の複数の画像を読み取る
    for filename in os.listdir('猫画像が入っているディレクトリ'):
        print(filename)
        result = detect('猫画像が入っているディレクトリ' + filename, 'cascade.xmlのパス')
        cv2.imwrite(f"result_{filename}".format(filename), result)