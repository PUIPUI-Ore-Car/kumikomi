import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import sys

i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, addr=0x3c)
ip= sys.argv 

# Clear display.
oled.fill(0)
oled.show()

# Create blank image for drawing.
image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)


font = ImageFont.truetype("..../usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc", 13)
font2 = ImageFont.truetype("..../usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc", 10)

# Draw the text
draw.text((0, 0), "うんち！w", font=font, fill=255)
draw.text((0, 17), "IPアドレス："+ip[1], font=font2, fill=255)

# Display image
oled.image(image)
oled.show()