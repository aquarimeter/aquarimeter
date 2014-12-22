#!/usr/bin/env python
import time
import os
import glob
import time
import RPi.GPIO as GPIO
import picamera
import json
import requests
GPIO.setmode(GPIO.BCM)
DEBUG = 1

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')


base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

auth_token = "whatever auth_token taken intial setup"
class aquarium(object):

    def send_readings(self, ph, temp):
        reading_data = {"auth_token":"HR6747C1iUM4XSRqKSsp",
                        "reading": {"ph":ph,
                                    "temperature":temp}}
        send_read = json.dumps(reading_data)
        url = "url of site"
        sent_data = requests.post(url, send_read)
        
        
        
    #for reading from DS18B20 temperature connected to GPIO4
    def read_temp_raw(self):
        f = open(device_file, 'r')
        lines = f.readlines()
        f.close()
        return lines


    # read SPI data from MCP3008 chip, 8 possible adc's (0 thru 7)
    def readadc(self,adcnum, clockpin, mosipin, misopin, cspin):
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

    #takes picture
    def takePic(self):
        with picamera.PiCamera() as camera:
            camera.capture('/home/pi/Desktop/image.jpg')
        
    #checks if anyhing is a good distance away to take a picture
    def moveSens(self):
        pir_pot = readadc(pir_adc, SPICLK, SPIMOSI, SPIMISO, SPICS)
        if pir_pot >150 and pir_pot < 650:
            takePic()

    #reads current ph
    def readPh(self):
        ph_pot = readadc(ph_adc, SPICLK, SPIMOSI, SPIMISO, SPICS)
        ph_value = ph_pot*5/1024*3.5
        return ph_value

    #read temperature
    def read_Temp(self):
        lines = self.read_temp_raw()
        while lines[0].strip()[-3:] != 'YES':
                time.sleep(0.2)
                lines = read_temp_raw()
            
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            temp_c = float(temp_string) / 1000.0
            temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_f
    
    # turn h bridge to heat
    def heat_On(self):
        GPIO.output(A1, GPIO.HIGH)
        GPIO.output(A2, GPIO.LOW)
        GPIO.output(A3, GPIO.HIGH)
        GPIO.output(A4, GPIO.LOW)

    # turn h bridge to cool
    def cool_On(self):
        GPIO.output(A1, GPIO.LOW)
        GPIO.output(A2, GPIO.HIGH)
        GPIO.output(A3, GPIO.LOW)
        GPIO.output(A4, GPIO.HIGH)

    #turn off any heating and cooling
    def peltio_Off(self):
        GPIO.output(A1, GPIO.LOW)
        GPIO.output(A2, GPIO.LOW)
        GPIO.output(A3, GPIO.LOW)
        GPIO.output(A4, GPIO.LOW)
    
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

A1 = 17
A2 = 27
A3 = 14
A4 = 15

#set pins up for output for bridge
GPIO.setup(A1,GPIO.OUT)
GPIO.setup(A2,GPIO.OUT)
GPIO.setup(A3,GPIO.OUT)
GPIO.setup(A4,GPIO.OUT)


#set up values
ph_adc = 2;
pir_adc = 1;
ideal_temp = 75;
max_temp = 80;
min_temp = 70;
heat = False;
cool = False;
aqua = aquarium()
while True:
        # read the analog pin for ph 
        ph_value = aqua.readPh()

        #read the analog pin for pir
        aqua.moveSens()      

        #read temp
        temp_f = aqua.read_temp()
        aqua.send_readings(ph_value, temp_f)
        if temp_f < min_temp:
            heat = True
            #turn h bridge to heat
            aqua.heat_On()
        elif temp_f > max_temp:
            cool = True
            #turn h bridge to cool
            aqua.cool_On()
        elif heat and temp_f > ideal_temp:
            heat = False
            #turn off heating
            aqua.peltio_Off()
        elif cool and temp_f < ideal_temp:
            cool = False
            #turn off cooling
            aqua.peltio_Off()
        # hang out and do nothing for a half second
        time.sleep(.1)
