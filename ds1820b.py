## Divetrainer


from machine import Pin, I2C, SPI
from time import sleep
import onewire, ds18x20
from ssd1306 import SSD1306_I2C

#pin values
led = Pin("LED", Pin.OUT)
ow_pin = Pin(12)
scl_p21 = Pin(21, Pin.IN)
sda_p20 = Pin(20, Pin.IN)
scl_p11 = Pin(11, Pin.IN)
sda_p10 = Pin(10, Pin.IN)



screen_i2c = I2C(1, scl=scl_p11, sda=sda_p10, freq=400000)


oled = SSD1306_I2C(128, 32, screen_i2c, addr=0x3C)



i2c = I2C(0, scl=scl_p21, sda=sda_p20, freq=100000)
temp_address = 0x48

oled.poweron()
oled.contrast(0)


#onewire object
sensor = ds18x20.DS18X20(onewire.OneWire(ow_pin))


roms = sensor.scan()
sensor_recorded_temp = 0
amb_temp = 0
while (True):
    
    sensor.convert_temp()
    sleep(.750)
    
    for rom in roms:
        led.toggle()
        temp_f = (sensor.read_temp(rom) * 1.8) + 32
        
        if temp_f != sensor_recorded_temp:
            oled.fill(0)
            oled.text('Sensor temp:', 0,0)
            oled.text("{:}".format(temp_f),0,20)
            oled.show()
            print()
        sensor_recorded_temp = temp_f
    
    temp_data_byte = i2c.readfrom(temp_address, 1, False)
    temp_data_c = int.from_bytes(temp_data_byte, "big")
    temp_data_f = (temp_data_c * 1.8) + 32
    
    if temp_data_f != amb_temp:
        print("Ambient temperature:", "{:.1f}".format(temp_data_f), " F")
        print()
    
    amb_temp = temp_data_f

    led.toggle()

oled.poweroff()