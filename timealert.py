import time
import RPi.GPIO as GPIO
from espeak import espeak
espeak.set_parameter(15,True)
speek=espeak.synth
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)
GPIO.setwarnings(False)
open('alartalm.txt','w').close()

while True:
    
    aa=open('alartalm.txt','r').read()
    c=[]
    c.append(aa)
    d=c[0].split()
    aaaaaaaa=0
    z=[]
    for i in range(len(d)):
        z.append(d[aaaaaaaa].rstrip('s'))
        aaaaaaaa+=1
        
    while 'hour' in z or 'minute' in z or 'second' in z:
        try:
            aa=open('alartalm.txt','r').read()
            c=[]
            c.append(aa)
            d=c[0].split()
            aaaaaaaa=0
            z=[]
            for i in range(len(d)):
                z.append(d[aaaaaaaa].rstrip('s'))
                aaaaaaaa+=1
            if 'hour'in z:
                test=int(z[z.index('hour')-1])
            if 'minute'in z:
                test1=int(z[z.index('minute')-1])
            if 'second'in z:
                test2=int(z[z.index('second')-1])
            if 'hour'in z or 'minute'in z or 'second'in z:
                speek('succesfully set alert')
            if 'hour'in z :
                speek('succesfully set alert')
                for i in range((int(z[z.index('hour')-1])*3600)):
                    time.sleep(1)
                    aa=open('alartalm.txt','r').read()
        
                    if not '700007' in aa:
                        break
            
            
            if 'minute' in z:
                for i in range((int(z[z.index('minute')-1])*60)):
                    time.sleep(1)
                    aa=open('alartalm.txt','r').read()
            
                    if not '700007' in aa:
                        break
    
            if 'second' in z:
                for i in range((int(z[z.index('second')-1]))):
                    time.sleep(1)
                    aa=open('alartalm.txt','r').read()
                
                    if not '700007' in aa:
                        break
            if '700007' in aa:  
                for i in range(120):
                    
                    GPIO.output(13,1)
                    time.sleep(0.5)
                    aa=open('alartalm.txt','r').read()
                    if not '700007' in aa:
                        break
            open('alartalm.txt','w').close()
            GPIO.output(13,0)
            break
        except ValueError:
            print 'error'
            open('alartalm.txt','w').close()
            time.sleep(0.5)
            speek('alert failled to sat please retry')
        
            
                

