#!/usr/bin/env python
from ina219 import INA219
from ina219 import DeviceRangeError
from time import sleep
from urllib.request import urlopen
SHUNT_OHMS = 0.1
devID = "&field7=%s"
baseURL = 'https://api.thingspeak.com/update?api_key=CRN8E0OVGUKR0N90'
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

     volts = read()
     sleep(1)
     print(volts)
     f = urlopen(baseURL + devID % (volts))
     f.close()
