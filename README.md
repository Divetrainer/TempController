# Temp_Controller

A handheld temperature sensor that will have 2 screens that show ambient(of the base) and the sensor temperature(connected DS18B20) in F

## Rational ##

This project combines all parts of the process for deployment of hardware
### hardware decisions ###
    1. 1x DS18B20 1 wire temperature sensor
    2. 2x 128x32 I2C OLED Screen
    3. 1x Pimoroni Pico LiPo Power SHIM
    4. 1x 13400 3.7V 1.11W LiPo Battery
    5. TC74A0 I2C Temperature Sensor
    6. Adafruit Perma-Proto Half-sized Breadboard PCB
    7. Housing (TBD)

### Software choices ###
    1. MicroPython

This one was tough, I was struggling between using C or C++ via the pi's SDK library but I was unable to parse through the intricacies and implimentation details so I put that aside and went with something that I knew how to work with. I used micropython due to its robust support via documentation and its scalability. I will probably revist this project and do it with C or C++(depending on library/personal availability)

## Deployment ##

The main deployment of this will be personal with little to no usage in a extreme environment. I mainly will be using this to determine temperature for my sons baths and the occasional fun moment while backpacking or overlanding. I will potentially make this car mountable so you can have more temperature readings for inside of your vehicle, but I will probably utilize larger screens with more data representations. 

I might modify the files and use this on a picoW for internal server temperature readings that push to a dashboard in graphana, but that is for a later project most likely. I will want that to be from a usb power source and running 24/7 so care will need to be taken to also validate that the pico and the software are not going to run away and skew any data I would get. 

## Learning Outcomes ##

I will try and add learning outcomes at the end of these projects to help me talk through what I thought was the most important parts. I think the main benefit this project gave me was the ability to search and find quality libraries to utilize and deploy. I am using a modified sd1336 library as the one initially submitted to pypy was not correct. There were errors in the declaring and processing of the rectangular object. I could not isolate the root cause so that block was removed before addition to the pico to prevent run time errors. 

I think I also learned a bit more on syntax and arguably better practices at code organization. I am trying to add comments where needed and let the code, and the consistent naming comment on other parts. In part, I think this project is solidifying what I have been learning and while not utilizing all parts, it is still creating a good base line to build on. 

This is also teaching me that, while I have the equipment, I needed some other pieces that never occured to me as being needed. I picked up some wire and a good pair of self-adjusting wire strippers after struggling for too long on getting things to be neat. I also learned how capable I was by solving issues like using stranded cable in a breadboard(use fine point tweezers after folding the strands in half) not wanting to arc or ruin my project in its infancy really makes you learn the best way to work with what you have! 

## Closing Thoughts ##

(to add when the project is done)
(will also add pictures when it is completed as well)



