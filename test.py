#importujeme potrebne kniznice
import machine
import time
#import network
#import socket
#od lava: 

pins = [16,5,4,0,2,14,12]
Pin1 = machine.Pin(16,machine.Pin.IN)
Pin2 = machine.Pin(5,machine.Pin.IN)
Pin3 = machine.Pin(4,machine.Pin.IN)
Pin4 = machine.Pin(0,machine.Pin.IN)
Pin5 = machine.Pin(2,machine.Pin.IN)
Pin6 = machine.Pin(14,machine.Pin.IN)
Pin7 = machine.Pin(12,machine.Pin.IN)
for i in range(len(pins)):
    pins[i] = machine.Pin(pins[i], machine.Pin.IN)
pwmPin = machine.PWM(machine.Pin(13), freq = 50)
#coefficient ktorym musime vynasobit servo aby sa premenilo na PWM hdonotu

coefficient = 0.457
print(coefficient)


sensorPins = [Pin1,Pin2,Pin3,Pin4,Pin5,Pin6,Pin7]
sensorHodnoty = [0,0,0,0,0,0,0,0]
#funkcia ktora dava umiesnenie lopty od 0 do 180
def getFirePos():
    #premene ktore nam pomouzu vypocitat poziciu 
    sucet = 0
    sensorPocet = 0
    #cyklus ktory iteruje cez hodnoty senzorov a snima ci vidia plamen
    for i in range(len(sensorHodnoty)):
        if(sensorHodnoty[i]):
            sensorPocet += 1
            sucet += (i*100)
    #matematika:
    if sensorPocet:
        poziciaLopty = (sucet/sensorPocet) / (((len(sensorHodnoty)*1000) - 1000) /180)*10
    else:
        poziciaLopty = -1
    return poziciaLopty
#funkcia ktora updatuje hodnoty sensorov
def getSensorVals():
    for i in range(len(sensorPins)):
        sensorHodnoty[i] = not(sensorPins[i].value())
    print("wazaa")

def switch(pin):
    pin.value(not pin.value())
    print("aza")
#hybe servom do hociktoreho stupna
def moveServoToDeg(stupen):
    #Konvertujeme stupne do PWM hodnot pre servo
    #Konvertujeme stupne do PWM hodnot pre servo
    pwmHodnota = int((stupen * coefficient) + 30)
    pwmPin.duty(pwmHodnota)
    print(pwmHodnota)
    return pwmHodnota
fen = machine.Pin(15, machine.Pin.OUT)
pos = 0
while True:
    getSensorVals()
    pozicia = int(getFirePos())
    if(pozicia != -1):
        fen.value(1)
        if(pozicia > pos):
            pos += 1
        elif(pozicia < pos):
            pos -= 1
    else:
         fen.value(0)
    moveServoToDeg(pos)
   



        
        
