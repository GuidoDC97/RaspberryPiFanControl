from gpiozero import DigitalOutputDevice
from time import sleep 
import os

FILE_TEMP = '/sys/class/thermal/thermal_zone0/temp'

ON_TEMP = 60
OFF_TEMP = 55
GPIO_PIN = 21
POLLING_INTERVAL = 5


def check_temp():
    with open(FILE_TEMP) as f:
        temp = int(f.read())/1000
    print(temp)
    return temp

def fan_control():
    fan = DigitalOutputDevice(GPIO_PIN)
    
    while True:
        temp = check_temp()
        
        if temp > ON_TEMP:
            fan.on()
        elif temp < OFF_TEMP:
            fan.off()
        
        sleep(5)

if __name__ == '__main__':
    fan_control()
    
    
	

