import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setup(18, gpio.OUT)

while TRUE:
    gpio.output(18, gpio.HIGH)
    pascode = raw_input("What is pi?: ")

    if pascode == "Awesome":
        gpio.output(18, gpio.LOW)
        time.sleep(4)

    else:
        gpio.output(18, gpio.HIGH)
        print("Wrong Password!")
        
