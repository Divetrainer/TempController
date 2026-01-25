## Divetrainer

from machine import Pin, I2C
from time import sleep
import onewire, ds18x20 #probe sensor library
from ssd1306 import SSD1306_I2C #screen management

led = Pin("LED", Pin.OUT)

#probe temp sensor
ow_pin = Pin(12)
sensor = ds18x20.DS18X20(onewire.OneWire(ow_pin))

scl_p11 = Pin(11, Pin.IN)
sda_p10 = Pin(10, Pin.IN)


#I2C intialize
probe_temp_screen_i2c = I2C(1, scl=scl_p11, sda=sda_p10, freq=400000)
probe_sensor_oled = SSD1306_I2C(128, 32, probe_temp_screen_i2c, addr=0x3C)

#oled power
probe_sensor_oled.poweron()
probe_sensor_oled.contrast(0)

roms = sensor.scan()
sensor_recorded_temp = 0

#TODO adjust area here for more control with buttons?

while (True):

    sensor.convert_temp()
    sleep(1)
    for rom in roms:
        led.toggle()
        temp_f = (sensor.read_temp(rom) * 1.8) + 32

        if temp_f != sensor_recorded_temp:
            probe_sensor_oled.fill(0)
            probe_sensor_oled.text('Probe Temp(F):', 0,0)
            probe_sensor_oled.text("{:.2f}".format(temp_f),0,20)
            probe_sensor_oled.show()

        sensor_recorded_temp = temp_f

    led.toggle()

