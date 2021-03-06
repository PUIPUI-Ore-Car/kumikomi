# coding: UTF-8
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import sys
import random
import subprocess
import time
import ipget

# WIFiのSSIDを取得

def get_ssid():
    cmd = 'iwconfig wlan0|grep ESSID'
    r = subprocess.run(cmd, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)\
        .stdout.decode().rstrip()
    idx = r.find('ESSID:')
    return r[idx + 7:-1]


message = ["イエ～イ 見てるぅ～？", "僕は君のことをずっと見てるよ", "ねぇ、じおん食べに行かない？", "天上天下唯我独尊", "PUI PUI!!", "ぷい！ぷい！ぷい！", "ププイ！", "なあ、なでてくれよ。", "きゅっぷい！", "どこでもいっしょだよ！", "ﾌﾟｲﾌﾟｲﾌﾟｲﾌﾟｲﾌﾟｲﾌﾟｲ"]
i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, addr=0x3c)
# ip= sys.argv 
ip= ipget.ipget()

# Clear display.
oled.fill(0)
oled.show()

print(ip.ipaddr("wlan0"))

# Create blank image for drawing.
flg = True
while(True):
    image = Image.new("1", (oled.width, oled.height))
    draw = ImageDraw.Draw(image)


    font = ImageFont.truetype("/home/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc", 12)
    font2 = ImageFont.truetype("/home/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc", 10)

    # Draw the text
    if(flg):
        draw.text((0, 0), message[random.randrange(10)], font=font2, fill=255)
        flg = False
    else:
        draw.text((0, 0), "SSID: "+get_ssid(), font=font2, fill=255)
        flg = True

    draw.text((0, 17), "IP:"+ip.ipaddr("wlan0"), font=font, fill=255)

    # Display image
    oled.image(image)
    oled.show()

    time.sleep(3)