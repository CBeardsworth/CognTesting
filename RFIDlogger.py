import time
import datetime
import logging
import os
import serial
from threading import Thread
import datetime

os.chdir("/home/pi/Peck/PIGPIO/")
os.system("sudo pigpiod")

ser = serial.Serial()

#rfidPort = "/dev/ttyAMA0" #rpis onboard serial port
rfidPort = "/dev/ttyS0" #new serial port
ser = serial.Serial()
ser.baudrate = 9600 # rate at which info is transfered. e.g. 9600 bits per second (identical to baudrate/bits per second)
ser.port = rfidPort
ser.timeout = 0.2 # Timeout before 

def readTag():
    '''
    This function starts an infinite loop that constantly scans for rfid tags.
    '''
    print 'attempting to read tags'
    global ID # Allows ID to be used as a variable ouside this function
    
    ser.open() # opens serial port
    rfidTime = None
    ID = None

    while True: # starts loop
        
        rfidData = ser.readline().strip() #reads line and removes whitespace chars with strip()
        if rfidTime != None :

            if (datetime.datetime.now() - rfidTime).seconds > 30: # if bird not detected within 30 seconds ID changes to None to reduce error. 

                ID = None
        
        if len(rfidData) > 0: #if there is data available...

            ID = rfidData # ... stores the data within the variable ID which is a global variable.
            rfidTime = datetime.datetime.now() #Logged time of visit
            print ID #Prints out ID for testing purposes
        


'''
The next step is to start each infinite loop going continuously
'''

t1 = Thread(target = readTag) # Set readTag as a thread 
t1.start() #Start readTag thread

