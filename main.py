## Divetrainer


from machine import Pin, I2C, SPI
from time import sleep
import onewire, ds18x20
from ssd1306 import SSD1306_I2C

#LED
led = Pin("LED", Pin.OUT)

#ambient temp sensor
scl_p21 = Pin(21, Pin.IN)
sda_p20 = Pin(20, Pin.IN)

screen_scl_p2 = Pin(1, Pin.IN)
screen_sda_p1 = Pin(0, Pin.IN)

i2c = I2C(0, scl=scl_p21, sda=sda_p20, freq=100000)
temp_address = 0x48

#ambient_temp_screen_i2c = I2C(0, scl=screen_scl_p2, sda=screen_sda_p1, freq=400000)
#ambient_sensor_oled = SSD1306_I2C(128, 32, ambient_temp_screen_i2c, addr=0x3C)

#probe temp sensor 

ow_pin = Pin(12)
sensor = ds18x20.DS18X20(onewire.OneWire(ow_pin))

scl_p11 = Pin(11, Pin.IN)
sda_p10 = Pin(10, Pin.IN)

probe_temp_screen_i2c = I2C(1, scl=scl_p11, sda=sda_p10, freq=400000)
probe_sensor_oled = SSD1306_I2C(128, 32, probe_temp_screen_i2c, addr=0x3C)

probe_sensor_oled.poweron()
probe_sensor_oled.contrast(0)


#ambient_sensor_oled.poweron()
#ambient_sensor_oled.contrast(0)

roms = sensor.scan()
sensor_recorded_temp = 0
amb_temp = 0

# add proper catch to turn off lights/screens when interupted
while (True):
    
    sensor.convert_temp()
    sleep(.750)
    
    for rom in roms:
        led.toggle()
        temp_f = (sensor.read_temp(rom) * 1.8) + 32
        
        if temp_f != sensor_recorded_temp:
            probe_sensor_oled.fill(0)
            probe_sensor_oled.text('Probe Temp(F):', 0,0)
            probe_sensor_oled.text("{:.2f}".format(temp_f),0,20)
            probe_sensor_oled.show()
            
        sensor_recorded_temp = temp_f
    
    temp_data_byte = i2c.readfrom(temp_address, 1, False)
    temp_data_c = int.from_bytes(temp_data_byte, "big")
    temp_data_f = (temp_data_c * 1.8) + 32
    
#    if temp_data_f != amb_temp:
#            ambient_sensor_oled.fill(0)
#            ambient_sensor_oled.text('Ambient temperature: ', 0,0)
#            ambient_sensor_oled.text("{:.1f}".format(temp_data_f),0,20)
#            ambient_sensor_oled.show()
    
#    amb_temp = temp_data_f

    led.toggle()

