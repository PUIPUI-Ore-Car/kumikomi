# coding: utf-8
import RPi.GPIO as GPIO
import time
import datetime
import os
import subprocess

## ポートの初期化（人感センサの準備）
PORT = 25
GPIO.setmode(GPIO.BCM)
GPIO.setup(PORT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

## 保存ディレクトリの設定
SAVEDIR = './Pictures/'
if not os.path.isdir(SAVEDIR):
    os.makedirs(SAVEDIR)


## 関数：人感センサが反応したときのイベント処理
def sensor_detected(channel):
    print('*** ALERT *** 侵入異常発生')

    # # 撮影（raspistillコマンドの外部呼び出し）
    # now = datetime.datetime.now()
    # filename = os.path.join(SAVEDIR, 'Image_' + now.strftime('%Y%m%d_%H%M%S') + '.jpg')
    # cmd = 'raspistill -o ' + filename + ' -t 2000 -w 1024 -h 768'
    # subprocess.call(cmd, shell=True)

    # print('画像を保存しました - Filename: ' + filename)

    # # 警報音を鳴動（python buzzerコマンドの外部呼び出し）
    # cmd = "python bouhan-buzzer.py alert &"
    # subprocess.call(cmd, shell=True)

    # # 警報発生後10秒間の待機
    # time.sleep(10)
    # cmd = "python bouhan-buzzer.py beep1"
    # subprocess.call(cmd, shell=True)

    # print('監視を再開します')
    time.sleep(1)


## イベントの定義
GPIO.add_event_detect(PORT, GPIO.RISING, callback=sensor_detected, bouncetime=200)

## メインループ
try:
    print('監視をスタートします (CTRL+Cで終了)')
    while True:  # 永遠にループ
        time.sleep(1)
except KeyboardInterrupt:  # CTRL+Cを押した場合
    print('')
    print('正常終了')

## 終了
GPIO.remove_event_detect(PORT)  # 定義したイベントを削除
GPIO.cleanup()