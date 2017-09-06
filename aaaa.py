import time
import RPi.GPIO as GPIO
from time import strftime
GPIO.setmode(GPIO.BOARD)
from espeak import espeak
espeak.set_parameter(15,True)
speek=espeak.synth
GPIO.setup(13, GPIO.OUT)
open('1212.txt','w').close()

while True:
    
    aa=open('1212.txt','r').read()
    c=[]
    c.append(aa)
    d=c[0].split()
    aaaaaaaa=0
    z=[]
    for i in range(len(d)):
        z.append(d[aaaaaaaa].rstrip('s'))
        aaaaaaaa+=1
    while 'hour' in z and 'minute' in z:
        try:
            
            c=[]
            aa=open('1212.txt','r').read()
            c.append(aa)
            d=c[0].split()
            aaaaaaaa=0
            z=[]
    
           
            for i in range(len(d)):
                z.append(d[aaaaaaaa].rstrip('s'))
                aaaaaaaa+=1
            print len(z)
            if not len(z)==0:
                test=int(z[z.index('hour')-1])
                est1=int(z[z.index('minute')-1])
                if not 'a' in z or not 'm' in z :
                    if not 'p' in z or not 'm' in z:
                        if not 'a.m.' in z:
                            if not 'p.m.' in z:
                                if  not 'a.m' in z:
                                    if  not 'p.m' in z:  
                                        if  not 'am' in z:
                                            if not 'pm' in z:
                                                int('a')
                                         


            if not len(z)==0:
                b=[]
                b.append(z[z.index('hour')-1])
                b.append(z[z.index('minute')-1])
                if 'a' in z and 'm' in z:
                    b.append('AM')
                if 'p' in z and 'm' in z:
                    b.append('PM')
                if 'a.m.' in z:
                    b.append('AM')
                if 'p.m.' in z:
                    b.append('PM')
                if 'a.m' in z:
                    b.append('AM')
                if 'p.m' in z:
                    b.append('PM')
                if 'am' in z:
                    b.append('AM')
                if 'pm' in z:
                    b.append('PM')

            a=[]
            aa=strftime('%I').lstrip('0')
            ab=strftime('%M').lstrip('0')
            a.append(aa)
            a.append(ab)
            a.append(strftime('%p'))
            print b
            print a
            if a==b:
                for i in range(200):
                    GPIO.output(13,1)
                    GPIO.setwarnings(False)
                    time.sleep(0.5)
                    aa=open('1212.txt','r').read()
                    if not 'hour' in aa:
                        break
                open('1212.txt','w').close()
                GPIO.output(13,0)
        except ValueError:
            print 'error'
            open('1212.txt','w').close()
            time.sleep(0.5)
            speek('alarm failled to sat please retry')
        

                
