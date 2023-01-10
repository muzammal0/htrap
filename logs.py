#!/usr/bin/env python
from ina219 import INA219
from ina219 import DeviceRangeError
from time import sleep
import time
from urllib.request import urlopen

SHUNT_OHMS = 0.1

volts = 0


def read():
    ina = INA219(SHUNT_OHMS)
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
    while(True):
        current_time = time.ctime()
        volts = read()
        print(volts)
        f = open("logs.txt", "a+")
        f.write(current_time + " "+str(volts)+"\n")
        f.close()
        time.sleep(1)

