import RPi.GPIO as gpio
import time
import os
gpio.setmode(gpio.BCM)
gpio.setup(17, gpio.OUT)

gpio.output(17, gpio.HIGH)
time.sleep(10)
gpio.output(17, gpio.LOW)
time.sleep(5)
#os.system("sudo shutdown -h now")
