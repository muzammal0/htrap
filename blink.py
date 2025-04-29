from gpiozero import LED
from time import sleep

led = LED(27)  # Use GPIO pin 17 for the LED

while True:
    led.on()    # LED on
    sleep(1)    # Wait for 1 second
    led.off()   # LED off
    sleep(1)    # Wait for 1 second
