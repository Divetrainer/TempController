## one wire example
## https://docs.micropython.org/en/latest/esp8266/tutorial/onewire.html

from machine import Pin, I2C
from time import sleep
import onewire, ds18x20

ow_pin = Pin(12)
led = Pin("LED", Pin.OUT)
#onewire object
sensor = ds18x20.DS18X20(onewire.OneWire(ow_pin))

roms = sensor.scan()
rec_temp = 0

while (True):
    
    sensor.convert_temp()
    sleep(.750)
    
    for rom in roms:
        led.toggle()
        temp_f = (sensor.read_temp(rom) * 1.8) + 32
        
        if temp_f != rec_temp:
            print('temperatures:', end=' ')
            print("{:.1f}".format(temp_f), end=' ')
            print()
        
        rec_temp = temp_f
        led.toggle()

