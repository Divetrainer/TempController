from machine import Pin, I2C
from time import sleep

pin = Pin("LED", Pin.OUT)
scl_p21 = Pin(21, Pin.IN)
sda_p20 = Pin(20, Pin.IN)
#data sheet recommends frequency rate from 100kHz 400kHz
i2c = I2C(sda=sda_p20, scl=scl_p21, freq=100000)
#grabbed from pulling hex address from below
temp_address = 0x48

##
##if len(devices) == 0:
##    print("No I2C devices found")
##else:
##    print("I2C device found:", len(devices))
##   for device in devices:
##        print("hex address:", hex(device))

while(True):
    print("*"*15)
    pin.toggle()
    print("Reading Temperature")
    sleep(1)
    temp_data_byte = i2c.readfrom(temp_address, 1, False)
    #print(temp_data_byte)
    pin.toggle()
    temp_data_c = int.from_bytes(temp_data_byte, "big")
    temp_data_f = (temp_data_c * 1.8) + 32
    print("temp:", temp_data_c, " C")
    print("temp:", "{:.1f}".format(temp_data_f), " F")
    sleep(2)
