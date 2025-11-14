## one wire example
## https://docs.micropython.org/en/latest/esp8266/tutorial/onewire.html

from machine import Pin, I2C
from time import sleep
import onewire, ds18x20

ow_pin = Pin(12)

#onewire object
sensor = ds18x20.DS18X20(onewire.OneWire(ow_pin))

while (True):
    print('temperatures:', end=' ')
    sensor.convert_temp()
    sleep(.750)

    print()

    sleep(2)

