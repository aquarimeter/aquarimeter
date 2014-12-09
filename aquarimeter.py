#!/usr/bin/env python
import time
import os
import glob
import time
import RPi.GPIO as GPIO
import picamera
GPIO.setmode(GPIO.BCM)
DEBUG = 1

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')


base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
#for reading from DS18B20 temperature connected to GPIO4
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines


# read SPI data from MCP3008 chip, 8 possible adc's (0 thru 7)
def readadc(adcnum, clockpin, mosipin, misopin, cspin):
        if ((adcnum > 7) or (adcnum < 0)):
                return -1
        GPIO.output(cspin, True)
 
        GPIO.output(clockpin, False)  # start clock low
        GPIO.output(cspin, False)     # bring CS low
 
        commandout = adcnum
        commandout |= 0x18  # start bit + single-ended bit
        commandout <<= 3    # we only need to send 5 bits here
        for i in range(5):
                if (commandout & 0x80):
                        GPIO.output(mosipin, True)
                else:
                        GPIO.output(mosipin, False)
                commandout <<= 1
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)
 
        adcout = 0
        # read in one empty bit, one null bit and 10 ADC bits
        for i in range(12):
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)
                adcout <<= 1
                if (GPIO.input(misopin)):
                        adcout |= 0x1
 
        GPIO.output(cspin, True)
        
        adcout >>= 1       # first bit is 'null' so drop it
        return adcout
 

# SPI port on the ADC to the Cobbler
SPICLK = 18
SPIMISO = 23
SPIMOSI = 24
SPICS = 25
 
# set up the SPI interface pins
GPIO.setup(SPIMOSI, GPIO.OUT)
GPIO.setup(SPIMISO, GPIO.IN)
GPIO.setup(SPICLK, GPIO.OUT)
GPIO.setup(SPICS, GPIO.OUT)
 
#set up gpio pin for h bridge
EN12 = 2
A1 = 17
A2 = 27
EN34 = 3
A3 = 10
A4 = 9

#set pins up for output for bridge
GPIO.setup(EN12,GPIO.OUT)
GPIO.setup(A1,GPIO.OUT)
GPIO.setup(A2,GPIO.OUT)
GPIO.setup(EN34,GPIO.OUT)
GPIO.setup(A3,GPIO.OUT)
GPIO.setup(A4,GPIO.OUT)

#set up h bridge to turn on 
GPIO.output(EN12, GPIO.HIGH)
GPIO.output(EN34, GPIO.HIGH)
#set up values
ph_adc = 0;
pir_adc = 1;
ideal_temp = 75;
max_temp = 80;
min_temp = 70;
heat = False;
cool = False;

while True:

        print(read_temp())
        
        # read the analog pin for ph 
        ph_pot = readadc(ph_adc, SPICLK, SPIMOSI, SPIMISO, SPICS)
        ph_value = ph_pot*5/1024*3.5

        #read the analog pin for pir
        pir_pot = readadc(pir_adc, SPICLK, SPIMOSI, SPIMISO, SPICS)
        if pir_pot >150 and pir_pot < 650:
            #maybe if funtion for time to make sure not a lot of pictures is taken and overload pi
            with picamera.PiCamera() as camera:
                    camera.capture('/home/pi/Desktop/image.jpg')
            
        

        #read temp
        lines = read_temp_raw()
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = read_temp_raw()
            
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            temp_c = float(temp_string) / 1000.0
            temp_f = temp_c * 9.0 / 5.0 + 32.0
            
        if temp_f < min_temp:
            heat = True
            #turn h bridge to heat
            GPIO.output(A1, GPIO.HIGH)
            GPIO.output(A2, GPIO.LOW)
            GPIO.output(A3, GPIO.HIGH)
            GPIO.output(A4, GPIO.LOW)
        elif temp_f > max_temp:
            cool = True
            #turn h bridge to cool
            GPIO.output(A1, GPIO.LOW)
            GPIO.output(A2, GPIO.HIGH)
            GPIO.output(A3, GPIO.LOW)
            GPIO.output(A4, GPIO.HIGH)
        elif heat and temp_f > ideal_temp:
            heat = False
            #turn off heating
            GPIO.output(A1, GPIO.LOW)
            GPIO.output(A2, GPIO.LOW)
            GPIO.output(A3, GPIO.LOW)
            GPIO.output(A4, GPIO.LOW)
        elif cool and temp_f < ideal_temp:
            cool = False
            #turn off cooling
            GPIO.output(A1, GPIO.LOW)
            GPIO.output(A2, GPIO.LOW)
            GPIO.output(A3, GPIO.LOW)
            GPIO.output(A4, GPIO.LOW)

        # hang out and do nothing for a half second
        time.sleep(.1)
