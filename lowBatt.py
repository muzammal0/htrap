from ina219 import INA219
from ina219 import DeviceRangeError
from time import sleep
from urllib.request import urlopen
SHUNT_OHMS = 0.0013
MAX_EXPECTED_AMPS = 4
volts = 0

import RPi.GPIO as gpio
import time
import os
gpio.setmode(gpio.BCM)
gpio.setup(17, gpio.OUT)




def read():
    ina = INA219(SHUNT_OHMS,MAX_EXPECTED_AMPS,busnum=1,address=0x40)
    ina.configure()
    volts = ina.voltage()
    print("Bus Voltage: %.3f V" % ina.voltage())
    try:
        print("Bus Current: %.3f mA" % ina.current())
        print("Power: %.3f mW" % ina.power())
        print("Shunt voltage: %.3f mV" % ina.shunt_voltage())
        return volts
    except DeviceRangeError as e:
        # Current out of device range with specified shunt resistor
        print(e)


if __name__ == "__main__":

     volts = read()
     sleep(1)
     if float(volts) < 11:
         print("low voltage")
         time.sleep(500) #wait to send an event
         gpio.output(17, gpio.HIGH)
         time.sleep(10)
         gpio.output(17, gpio.LOW)
         time.sleep(5)
         os.system("sudo shutdown -h now")
     print(volts)
