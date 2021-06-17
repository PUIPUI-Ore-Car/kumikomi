# -*- coding: utf-8 -*-

import smbus
import math
from time import sleep
# from playsound import playsound
import subprocess

DEV_ADDR = 0x68

# ACCEL_XOUT = 0x3b
# ACCEL_YOUT = 0x3d
# ACCEL_ZOUT = 0x3f

#おそらくこちらが本来のAccel
ACCEL_XOUT = 0x43
ACCEL_YOUT = 0x45
ACCEL_ZOUT = 0x47

TEMP_OUT = 0x41
# GYRO_XOUT = 0x43
# GYRO_YOUT = 0x45
# GYRO_ZOUT = 0x47

PWR_MGMT_1 = 0x6b
PWR_MGMT_2 = 0x6c

bus = smbus.SMBus(1)
bus.write_byte_data(DEV_ADDR, PWR_MGMT_1, 0)

def read_word(adr):
    high = bus.read_byte_data(DEV_ADDR, adr)
    low = bus.read_byte_data(DEV_ADDR, adr+1)
    val = (high << 8) + low
    return val

def read_word_sensor(adr):
    val = read_word(adr)
    if (val >= 0x8000):  return -((65535 - val) + 1)
    else:  return val

def get_temp():
    temp = read_word_sensor(TEMP_OUT)
    x = temp / 340 + 36.53      # data sheet(register map)記載の計算式.
    return x

def getGyro():
    x = read_word_sensor(GYRO_XOUT)/ 131.0
    y = read_word_sensor(GYRO_YOUT)/ 131.0
    z = read_word_sensor(GYRO_ZOUT)/ 131.0
    return [x, y, z]


def getAccel(selector):
    if(selector == "x"):
        return read_word_sensor(ACCEL_XOUT)/ 16384.0
    elif(selector == "y"):
        return read_word_sensor(ACCEL_YOUT)/ 16384.0
    elif(selector == "z"):
        return read_word_sensor(ACCEL_ZOUT)/ 16384.0


# ax, ay, az = getAccel()

sspx=0

while 1:
    sleep(0.1)

    ax= getAccel("x")
    ay= getAccel("y")
    az= getAccel("z")
    
    #クソ雑に速度を求めていくよ
    acc_fl = float(ax)
    spx_fl = acc_fl * 0.05
    sspx += spx_fl

    #if ax > 0.5 or ax < -0.5 or ay > 0.5 or ay < -0.5 or az > 0.5 or az < -0.5 :
    if sspx > 1 or sspx < -1 :
        print ('音が出たよ！')
        # playsound("pui.mp3")
        subprocess.call("aplay ~/kumikomi/pui.wav", shell=True)

    print ('{0:4.3f}' .format(sspx))
    # print ('{0:4.3f}\t{0:4.3f}\t{0:4.3f}' .format(ax, ay, az))
