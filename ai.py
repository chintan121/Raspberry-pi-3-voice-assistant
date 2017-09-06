# -*- coding: utf-8 -*-
from selenium import webdriver
from espeak import espeak
import requests
from bs4 import BeautifulSoup
import RPi.GPIO as GPIO
import dht11
import time
from time import strftime
import vlc
from selenium.webdriver.chrome.options import Options
import os
import random


rdp = os.listdir('./song')
open('song.txt','w').close()
ffff=[item.lower() for item in rdp]
for qqq in ffff:
    open('song.txt','a').write(qqq+'\n')
open('songs.txt','w').close()
for qqq in rdp:
    open('songs.txt','a').write(qqq+'\n')
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)


GPIO.setup(40, GPIO.OUT)
p = GPIO.PWM(40,50)
p.start(12.5)
time.sleep(0.5)
p.stop
GPIO.cleanup(40)
Instance = vlc.Instance()
player = Instance.media_player_new()
espeak.set_parameter(15,True)
speek=espeak.synth
chrome_options = Options()
chrome_options.add_argument("--use-fake-ui-for-media-stream")
a = webdriver.Chrome(executable_path="/usr/lib/chromium-browser/chromedriver", chrome_options=chrome_options)
a.get('https://www.google.com/intl/en/chrome/demos/speech.html')
a.find_element_by_id("div_start").click()
GPIO.setwarnings(False)
GPIO.output(13,1)
time.sleep(0.1)
GPIO.output(13,0)
time.sleep(0.1)
GPIO.output(13,1)
time.sleep(0.2)
GPIO.output(13,0)


                                                                              
def spe():
    b = a.find_element_by_id('results')
    d=b.text.split()
    e=[str(x) for x in d] 
    z=map(lambda x: x.lower(),e)
    au=a.find_element_by_id("info_speak_now").get_attribute("style")
    aau=a.find_element_by_id("info").get_attribute("style")
    if au=='display: none;':
        a.find_element_by_id("div_start").click()
    if aau=='visibility: hidden;':
        a.find_element_by_id("div_start").click()
    
    return z
aaaa=1
while True:
    z=spe()
    print spe()
    if len(z)>2:
        a.find_element_by_id("div_start").click()
        a.find_element_by_id("div_start").click()
       
    if 'raspberry' in z[-2:]:
        
            a.find_element_by_id("div_start").click()
            a.find_element_by_id("div_start").click()
            
            if aaaa==1:
                speek('what\'s my order')
            
            
            GPIO.output(13,1)
            time.sleep(0.1)
            GPIO.output(13,0)
            time.sleep(0.1)
            GPIO.output(13,1)
            time.sleep(0.2)
            GPIO.output(13,0)
            
            
            j=0
            while j==0:
                z=spe()
                print spe()
                print 'in loop'
                if 'led' in z and 'on' in z and not 'raspberry' in z[-2:]:
                    if GPIO.input(12)==1:
                        speek('L E D is already on')
                    else:
                        speek('L E D turned on')
                    GPIO.output(12,1)
                    time.sleep(0.1)
                    j+=1
                    a.find_element_by_id("div_start").click()
                    a.find_element_by_id("div_start").click()
                if 'led' in z and 'off' in z and not 'raspberry' in z[-2:]:
                    if GPIO.input(12)==0:
                        speek('L E D is already off')
                    else:
                        speek('L E D turned off')
                    GPIO.output(12,0)
                    time.sleep(0.1)
                    j+=1
                    a.find_element_by_id("div_start").click()
                    a.find_element_by_id("div_start").click()
                if 'security' in z and 'on' in z and not 'raspberry' in z[-2:]:
                    fboo=open('10.txt','r')
                    secc= fboo.read()
                    if '1' in secc:
                        speek('security is already on')
                    else:
                        speek('security turned on')
                    open('10.txt','w').write('1')
                    j+=1
                    a.find_element_by_id("div_start").click()
                    a.find_element_by_id("div_start").click()
                if 'security' in z and 'code' in z and '999' in z and 'off' in z and not 'raspberry' in z[-2:]:
                    fboo=open('10.txt','r')
                    secc= fboo.read()
                    if '0' in secc:
                        speek('security is already off')
                    else:
                        speek('security turned off')
                    open('10.txt','w').write('0')
                    j+=1
                    a.find_element_by_id("div_start").click()
                    a.find_element_by_id("div_start").click()
                if 'play' in z and 'song' in z and not 'raspberry' in z[-2:]:
                   
                    r=0
                    fuk=0
                    for iiiii in rdp:
                        songnames=open('song.txt','r').readlines()[r].split()
                        print songnames
                        if not set(songnames)&set(z[1:-1]) == set([]):
                            speek('playing' 'song')
                            print 00
                            time.sleep(1.5)#                           location of song
                            player.set_media(Instance.media_new_path('/home/pi/Desktop/project/song/'+open('songs.txt','r').readlines()[r].rstrip()))
                            player.play()
                            aaaa=0
                            fuk=+1
                            break
                        r+=1
                    if fuk==0:
                        speek('no song found')
                        
                    j+=1
                    a.find_element_by_id("div_start").click()
                    a.find_element_by_id("div_start").click()
                if 'random' in z and 'song' in z and not 'raspberry' in z[-2:]:
                    speek('playing random song')
                    time.sleep(1.5)#                            location of song
                    player.set_media(Instance.media_new_path('/home/pi/Desktop/project/song/'+(random.choice(rdp))))
                    player.play()
                    aaaa=0
                    j+=1
                    a.find_element_by_id("div_start").click()
                    a.find_element_by_id("div_start").click()
                
                if 'stop' in z and 'song' in z and not 'raspberry' in z[-2:]:
                    player.stop()
                    aaaa=1
                    j+=1
                    a.find_element_by_id("div_start").click()
                    a.find_element_by_id("div_start").click()
                if 'pause' in z and 'song' in z and not 'raspberry' in z[-2:]:
                    player.pause()
                    aaaa=1
                    j+=1
                    a.find_element_by_id("div_start").click()
                    a.find_element_by_id("div_start").click()
                if 'resume' in z and 'song' in z and not 'raspberry' in z[-2:]:
                    player.play()
                    aaaa=0
                    j+=1
                    a.find_element_by_id("div_start").click()
                    a.find_element_by_id("div_start").click()
                if 'set' in z and 'volume' in z and 'high' in z and not 'raspberry' in z[-2:]:
    
                    player.audio_set_volume(120)
                    j+=1
                    a.find_element_by_id("div_start").click()
                    a.find_element_by_id("div_start").click()
                if 'set' in z and 'volume' in z and 'medium' in z and not 'raspberry' in z[-2:]:
    
                    player.audio_set_volume(60)
                    j+=1
                    a.find_element_by_id("div_start").click()
                    a.find_element_by_id("div_start").click()
                if 'set' in z and 'volume' in z and 'low' in z and not 'raspberry' in z[-2:]:
    
                    player.audio_set_volume(40)
                    j+=1
                    a.find_element_by_id("div_start").click()
                    a.find_element_by_id("div_start").click()

                if 'date'in z and "what\'s" in z and not 'raspberry' in z[-2:]:
                    date= strftime("%d")
                    month= strftime("%m")
                    year= strftime("%Y")
                    dayaa=strftime("%A")
                    showw=[]
                    showw.append(date)
                    showw.append(month)
                    showw.append(year)
                    showw.append(dayaa)
                    ffffff=[]
                    for i in range(4):
                         aaaaa=showw[i].lstrip('0')
                         ffffff.append(aaaaa)
                    mon=['january',' february ','march ','april ','may ','june',' july ','august ','september',' october',' november ','december']
                                       
                    
                    speek('todays date is '+ffffff[0]+''+mon[int(ffffff[1])-1]+','+ffffff[2]+" "+ffffff[3])
                    print 'todays date is '+ffffff[0]+''+mon[int(ffffff[1])-1]+','+ffffff[2]+" "+ffffff[3]
                    j+=1
                    
                    a.find_element_by_id("div_start").click()
                    a.find_element_by_id("div_start").click()
                    
                if "time" in z and "what\'s" in z and not 'raspberry' in z[-2:]:
                    hour = strftime('%I')
                    minit=strftime('%M')
                    ampm=strftime('%p')
                    showww=[]
                    showww.append(hour)
                    showww.append(minit)
                    showww.append(ampm)
                    ffff=[]
                    for i in range(3):
                         aaaqq=showww[i].lstrip('0')
                         ffff.append(aaaqq)

                    speek('time is'+ffff[0]+'  Hours    ,and'+ffff[1]+'   minites   '+'   '+ffff[2])
                    j+=1
                    a.find_element_by_id("div_start").click()
                    a.find_element_by_id("div_start").click()
                if 'joke' in z and 'say' in z and not 'raspberry' in z[-2:]:
                    speek('collecting joke')
                    espeak.set_parameter(7,True)
                    time.sleep(1)
                    All=[]
                    for i in range(1,281):
                        All.append(i)
                    aall= (random.choice(All))
                    print aall
                    ap=aall*3
                    aj=aall*3+1
                    saas=open('joke.txt','r').readlines()[ap]
                    daad=open('joke.txt','r').readlines()[aj]
                    speek(saas)
                    print saas
                    time.sleep(4)
                    speek(daad)
                    print daad
                    espeak.set_parameter(15,True)
                    j+=1
                    a.find_element_by_id("div_start").click()
                    a.find_element_by_id("div_start").click()
                if 'set' in z and 'alert' in z and not 'raspberry' in z[-2:]:
                    open('alartalm.txt','w').close()
                    for i in range(len(z)):
                        open('alartalm.txt','a').write(z[i]+' ')
                    open('alartalm.txt','a').write('700007'+' ')
                    
                    
                    j+=1
                    a.find_element_by_id("div_start").click()
                    a.find_element_by_id("div_start").click()
                if 'stop' in z and 'alert' in z and not 'raspberry' in z[-2:]:
                    open('alartalm.txt','w').close()
                    j+=1
                    speek('alert stoped')
                    a.find_element_by_id("div_start").click()
                    a.find_element_by_id("div_start").click()
                if 'stop' in z and 'alarm' in z  and not 'raspberry' in z[-2:]:
                    open('1212.txt','w').close()
                    j+=1
                    speek('alarm canceled')
                    a.find_element_by_id("div_start").click()
                    a.find_element_by_id("div_start").click()

                if 'set' in z and 'alarm' in z and not 'raspberry' in z[-2:]:
                    open('1212.txt','w').close()
                    for i in range(len(z)):
                        open('1212.txt','a').write(z[i]+' ')
                    j+=1
                    a.find_element_by_id("div_start").click()
                    a.find_element_by_id("div_start").click()
                if 'what\'s' in z and 'temperature' in z and not 'raspberry' in z[-2:]:
                    instance = dht11.DHT11(pin=7)
                    result = instance.read()
                    time.sleep(0.5)
                    if result.is_valid():
                        speek('Temprature is %d degree celsius' % result.temperature)
                    j+=1
                    a.find_element_by_id("div_start").click()
                    a.find_element_by_id("div_start").click()
                if 'what\'s' in z and 'humidity' in z and not 'raspberry' in z[-2:]:
                    instance = dht11.DHT11(pin=7)
                    result = instance.read()
                    time.sleep(0.5)
                    if result.is_valid():
                        speek('Humidity is %d percent' % result.humidity)
                    j+=1
                    a.find_element_by_id("div_start").click()
                    a.find_element_by_id("div_start").click()
                if 'door' in z and 'code' in z and '989' in z and not 'raspberry' in z[-2:]:
                    speek('door unlocked')
                    GPIO.setup(40, GPIO.OUT)
                    p = GPIO.PWM(40,50)
                    p.start(2.5)
                    time.sleep(1)
                    GPIO.cleanup(40)
                    time.sleep(8)
                    GPIO.setup(40, GPIO.OUT)
                    p = GPIO.PWM(40,50)
                    p.start(12)
                    time.sleep(1)
                    p.stop()
                    GPIO.cleanup(40)
                    
                    j+=1
                    a.find_element_by_id("div_start").click()
                    a.find_element_by_id("div_start").click()

                if 'update' in z and 'news' in z and not 'raspberry' in z[-2:]:
                    open('file.txt','w').close()
                    
                    soup = BeautifulSoup(requests.get("http://timesofindia.indiatimes.com/home/headlines").text,"html5lib")
                    j=0
                    try:
                        for i in range(60):
                            res = soup.findAll("span", {"class": "w_tle"})[j].text
                            j+=1
                            print res
                            open('file.txt','a').write(res.encode('utf-8')+'\n')
                            
                    except IndexError:
                        j+=1
                        a.find_element_by_id("div_start").click()
                        a.find_element_by_id("div_start").click()
                    speek('successfully updated news')
                    jjj=0
                    j+=1
                    a.find_element_by_id("div_start").click()
                    a.find_element_by_id("div_start").click()
                    
                if 'repeat' in z and 'news' in z and not 'raspberry' in z[-2:]:
                    
                    jjj-=3
                    if jjj<2:
                        speek('no news are been said')
                    for i in range(3):
                        speek(open('file.txt','r').readlines()[jjj])
                        jjj+=1
                        time.sleep(4)
                    j+=1
                    a.find_element_by_id("div_start").click()
                    a.find_element_by_id("div_start").click()
                    
                if 'news' in z and 'say' in z and not 'raspberry' in z[-2:]:
            
                    for i in range(3):
                        speek(open('file.txt','r').readlines()[jjj])
                        jjj+=1
                        time.sleep(6)
                    
                    j+=1
                    a.find_element_by_id("div_start").click()
                    a.find_element_by_id("div_start").click()

                if 'weather' in z and not 'raspberry' in z[-2:]:
                    speek('collecting data')
                    time.sleep(3)
                    open('fhhhh.txt','w').close()
                    # change location but dont change site
                    soup=BeautifulSoup(requests.get("https://www.timeanddate.com/weather/india/jamnagar/ext",'lxml').content)

                    for aapp in soup.find_all('tr',limit=9):
                        for suuu in aapp.find_all('td',limit=5):
                             print suuu.text
                             open('fhhhh.txt','a').write(suuu.text.encode('utf8')+'\n')
                    

                    dayys=0
                    if strftime("%a")=='Sun':
                        ss=dayys
                        mm=dayys+5
                        tt=dayys+10
                        ww=dayys+15
                        hh=dayys+20
                        ff=dayys+25
                        aa=dayys+30
                    if strftime("%a")=='Mon':
                        ss=dayys+30
                        mm=dayys
                        tt=dayys+5
                        ww=dayys+10
                        hh=dayys+15
                        ff=dayys+20
                        aa=dayys+25
                    if strftime("%a")=='Tue':
                        ss=dayys+25
                        mm=dayys+30
                        tt=dayys
                        ww=dayys+5
                        hh=dayys+10
                        ff=dayys+15
                        aa=dayys+20
                    if strftime("%a")=='Wed':
                        ss=dayys+20
                        mm=dayys+25
                        tt=dayys+30
                        ww=dayys
                        hh=dayys+5
                        ff=dayys+10
                        aa=dayys+15
                    if strftime("%a")=='Thu':
                        ss=dayys+15
                        mm=dayys+20
                        tt=dayys+25
                        ww=dayys+30
                        hh=dayys
                        ff=dayys+5
                        aa=dayys+10
                    if strftime("%a")=='Fri':
                        ss=dayys+10
                        mm=dayys+15
                        tt=dayys+20
                        ww=dayys+25
                        hh=dayys+30
                        ff=dayys
                        aa=dayys+5
                    if strftime("%a")=='Sat':
                        ss=dayys+5
                        mm=dayys+10
                        tt=dayys+15
                        ww=dayys+20
                        hh=dayys+25
                        ff=dayys+30
                        aa=dayys
                    if 'sunday' in z or 'sunday\'s' in z:
                        speek('weather will be ' +open('fhhhh.txt','r').readlines()[ss+2])
                        speek('temprature will be '+ open('fhhhh.txt','r').readlines()[ss+1].replace('/','to'))
                        speek('and wind will be' +open('fhhhh.txt','r').readlines()[ss+4].replace('km/h','kilometer per hour'))
                        j+=1
                        a.find_element_by_id("div_start").click()
                        a.find_element_by_id("div_start").click()
                    if 'monday' in z or 'monday\'s' in z:
                        speek('weather will be ' +open('fhhhh.txt','r').readlines()[mm+2])
                        speek('temprature will be '+ open('fhhhh.txt','r').readlines()[mm+1].replace('/','to'))
                        speek('and wind will be ' +open('fhhhh.txt','r').readlines()[mm+4].replace('km/h','kilometer per hour'))
                        j+=1
                        a.find_element_by_id("div_start").click()
                        a.find_element_by_id("div_start").click()
                        
                    if 'tuesday' in z or 'tuesday\'s' in z :
                        speek('weather will be ' +open('fhhhh.txt','r').readlines()[tt+2])
                        speek('temprature will be '+ open('fhhhh.txt','r').readlines()[tt+1].replace('/','to'))
                        speek('and wind will be ' +open('fhhhh.txt','r').readlines()[tt+4].replace('km/h','kilometer per hour'))
                        j+=1
                        a.find_element_by_id("div_start").click()
                        a.find_element_by_id("div_start").click()
                    if 'wednesday' in z or 'wednesday\'s' in z:
                        speek('weather will be ' +open('fhhhh.txt','r').readlines()[ww+2])
                        speek('temprature will be '+ open('fhhhh.txt','r').readlines()[ww+1].replace('/','to'))
                        speek('and wind will be ' +open('fhhhh.txt','r').readlines()[ww+4].replace('km/h','kilometer per hour'))
                        j+=1
                        a.find_element_by_id("div_start").click()
                        a.find_element_by_id("div_start").click()
                    if 'thursday' in z or 'thursday\'s' in z:
                        speek('weather will be ' +open('fhhhh.txt','r').readlines()[hh+2])
                        speek('temprature will be '+ open('fhhhh.txt','r').readlines()[hh+1].replace('/','to'))
                        speek('and wind will be ' +open('fhhhh.txt','r').readlines()[hh+4].replace('km/h','kilometer per hour'))
                        j+=1
                        a.find_element_by_id("div_start").click()
                        a.find_element_by_id("div_start").click()
                    if 'friday' in z or 'friday\'s' in z:
                        speek('weather will be ' +open('fhhhh.txt','r').readlines()[ff+2])
                        speek('temprature will be '+ open('fhhhh.txt','r').readlines()[ff+1].replace('/','to'))
                        speek('and wind will be ' +open('fhhhh.txt','r').readlines()[ff+4].replace('km/h','kilometer per hour'))
                        j+=1
                        a.find_element_by_id("div_start").click()
                        a.find_element_by_id("div_start").click()
                    if 'saturday' in z or 'saturday\'s' in z:
                        speek('weather will be. ' +open('fhhhh.txt','r').readlines()[aa+2])
                        speek('temprature will be. '+ open('fhhhh.txt','r').readlines()[aa+1].replace('/','to'))
                        speek('and wind will be. ' +open('fhhhh.txt','r').readlines()[aa+4].replace('km/h','kilometer per hour'))
                        j+=1
                        a.find_element_by_id("div_start").click()
                        a.find_element_by_id("div_start").click()
                    if 'today' in z or 'today\'s' in z:
                        speek('weather will be ' +open('fhhhh.txt','r').readlines()[2])
                        speek('temprature will be '+ open('fhhhh.txt','r').readlines()[1].replace('/','to'))
                        speek('and wind will be' +open('fhhhh.txt','r').readlines()[4].replace('km/h','kilometer per hour'))
                        j+=1
                        a.find_element_by_id("div_start").click()
                        a.find_element_by_id("div_start").click()
        
                    if 'tomorrow' in z or 'tommorow\'s' in z:
                        speek('weather will be ' +open('fhhhh.txt','r').readlines()[5+2])
                        speek('temprature will be '+ open('fhhhh.txt','r').readlines()[5+1].replace('/','to'))
                        speek('and wind will be ' +open('fhhhh.txt','r').readlines()[5+4].replace('km/h','kilometer per hour'))
                        j+=1
                        a.find_element_by_id("div_start").click()
                        a.find_element_by_id("div_start").click()

                
                if 'clean' in z and 'note' in z and not 'raspberry' in z[-2:]:
                    
                    if open('note.txt','r').read()=='':
                        speek('notes are alredy cleared')
                    elif z[z.index('note')-1].isdigit():
                        speek('note number'+z[z.index('note')-1]+'is been cleaned')
                        ioi=open('note.txt','r').readlines()
                                
                        ioi.remove(ioi[int(z[z.index('note')-1])-1])
                        print ioi
                        open('note.txt','w').close()
                        for oio in ioi:
                            open('note.txt','a').write(oio)
                    else:
                        open('note.txt','w').close()
                        speek('notes cleared')
                    j+=1
            
                    a.find_element_by_id("div_start").click()
                    a.find_element_by_id("div_start").click()
                
                if 'note' in z and 'save' in z and not 'raspberry' in z[-2:]:
                    speek('nate saved')
                    aas1=0
                    a12=z[z.index('note')+1:z.index('save')]
                    

                    for a20 in range(len(a12)):
                            open('note.txt','a').write(a12[aas1]+' ')
                            aas1+=1
                    open('note.txt','a').write('\n') 
                    j+=1
                    a.find_element_by_id("div_start").click()
                    a.find_element_by_id("div_start").click()
                    
                if 'note' in z and 'open' in z and not 'raspberry' in z[-2:]:
                    if open('note.txt','r').read()=='':
                        speek('not note found')
                    else:
                        alxk=open('note.txt','r').readlines()
                        qlx=1
                        for gfh in alxk:
                            speek(str(qlx))
                            time.sleep(0.8)
                            speek(gfh.rstrip('\n'))
                            time.sleep(0.8)

                            qlx+=1
                    j+=1
            
                    a.find_element_by_id("div_start").click()
                    a.find_element_by_id("div_start").click()
                
