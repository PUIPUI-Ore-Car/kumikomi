import RPi.GPIO as GPIO
import dht11
import time
import datetime

import json
import requests

def postJson(temp, humidity):
	# 温湿度を送信する
	url = "http://localhost:3000/temperature"

	# jsonのデータ
	jsonData = {
		"temperature": temp,
		"humidity": humidity
	}

	# POST送信
	response = requests.post(
		url,
		json=jsonData
	)

	return json.loads(response.text)



# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# read data using pin 14
instance = dht11.DHT11(pin=18)

try:
	while True:
		result = instance.read()
		if result.is_valid():
			temp = result.temperature
			humidity = result.humidity
			retVal = postJson(temp, humidity)

			print("Last valid input: " + str(datetime.datetime.now()))

			print("Temperature: %-3.1f C" % result.temperature)
			print("Humidity: %-3.1f %%" % result.humidity)

		time.sleep(6)

except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()