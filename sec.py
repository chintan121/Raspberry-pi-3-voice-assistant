#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11, GPIO.IN)
GPIO.setup(38, GPIO.OUT)
while True:
        f=open('10.txt','r')
        a= f.read()
        print "lv1"
        GPIO.output(38,0)
        while '1' in a:
                print 'lv2'
                
                time.sleep(0.1)
                
                if GPIO.input(11) == GPIO.LOW:
                        print '...Movement not detected!'
                else:
                
                        while '1' in a:
                                print 'lv3'
                                a=open('10.txt','r').read()
                                print 'Movement detected!...'
                                GPIO.output(38,1)


