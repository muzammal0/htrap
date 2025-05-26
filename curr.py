import time
import board
import busio
from adafruit_ina219 import INA219

# Create I2C bus
i2c_bus = busio.I2C(board.SCL, board.SDA)

# Create INA219 instance (no need to call configure)
ina = INA219(i2c_bus)

# Read loop
while True:
    bus_voltage = ina.bus_voltage            # Voltage on V- (load side)
    shunt_voltage = ina.shunt_voltage        # Voltage across the shunt resistor
    current = ina.current                    # Current in milliamps
    power = ina.power                        # Power in milliwatts

    print(f"Bus Voltage:    {bus_voltage:.3f} V")
    print(f"Shunt Voltage:  {shunt_voltage:.3f} V")
    print(f"Current:        {current:.3f} mA")
    print(f"Power:          {power:.3f} mW")
    print("")

    time.sleep(1)
