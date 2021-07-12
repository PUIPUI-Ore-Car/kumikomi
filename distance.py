#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import subprocess
import requests
import json

# JSONで送る
def postJson ():
    url = "http://localhost:3000/"

    # jsonのデータ
    jsonData = {
        "pui": "pui"
    }

    # POST送信
    response = requests.post(
        url,
        json=jsonData
    )

    return json.loads(response.text)


# HIGH or LOWの時計測
def pulseIn(PIN, start=1, end=0):
    if start==0: end = 1
    t_start = 0
    t_end = 0
    # ECHO_PINがHIGHである時間を計測
    while GPIO.input(PIN) == end:
        t_start = time.time()

    while GPIO.input(PIN) == start:
        t_end = time.time()
    return t_end - t_start

# 距離計測
def calc_distance(TRIG_PIN, ECHO_PIN, v=34000):
    # 連続したかを確認するflg
    flg = False
    while(True):
        # TRIGピンを0.3[s]だけLOW
        GPIO.output(TRIG_PIN, GPIO.LOW)
        time.sleep(0.1)
        # TRIGピンを0.00001[s]だけ出力(超音波発射)
        GPIO.output(TRIG_PIN, True)
        time.sleep(0.00001)
        GPIO.output(TRIG_PIN, False)
        # HIGHの時間計測
        t = pulseIn(ECHO_PIN)
        # 距離[cm] = 音速[cm/s] * 時間[s]/2
        distance = v * t/2
        if(distance < 20):
            if(not flg):
                print("なでられたよ")
                subprocess.call("aplay /home/pi/kumikomi/pui.wav", shell=True)
                flg = True
        else:
            flg = False
            print(distance, "cm")
    # ピン設定解除
    GPIO.cleanup()

# TRIGとECHOのGPIO番号
TRIG_PIN = 14
ECHO_PIN = 15
# ピン番号をGPIOで指定
GPIO.setmode(GPIO.BCM)
# TRIG_PINを出力, ECHO_PINを入力
GPIO.setup(TRIG_PIN,GPIO.OUT)
GPIO.setup(ECHO_PIN,GPIO.IN)
GPIO.setwarnings(False)

# 距離計測(TRIGピン番号, ECHO_PIN番号, 音速[cm/s])
calc_distance(TRIG_PIN, ECHO_PIN, 34000)