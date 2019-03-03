# CircuitPython Demo - USB/Serial echo

import board
import busio
import digitalio
import time
import adafruit_rfm9x
from adafruit_onewire.bus import OneWireBus
from adafruit_ds18x20 import DS18X20

ow_bus = OneWireBus(board.D10)

ds18 = DS18X20(ow_bus, ow_bus.scan()[0])

# lora radio
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = digitalio.DigitalInOut(board.RFM9X_CS)
reset = digitalio.DigitalInOut(board.RFM9X_RST)
rfm9x = adafruit_rfm9x.RFM9x(spi, cs, reset, 915.0)

# led
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

index = 0

while True:
    
    temp_str='{0:0.3f}'.format(ds18.temperature)   
    rfm9x.send(temp_str)
    print(temp_str)
    
    led.value = False
    time.sleep(.1)
    led.value = True
    time.sleep(.1)
