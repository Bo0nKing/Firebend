import time
import board
import busio
import adafruit_adxl34x
import RPi.GPIO as GPIO
from time import sleep


flameTime = 250; #how long the flame lasts, in ms
i2c = busio.I2C(board.SCL, board.SDA)
accelerometer = adafruit_adxl34x.ADXL345(i2c)
solenoid = 18
spark = 31


# Just open up the valve for the butane and spark it for duration set by flameTime
def fire(time):

    GPIO.output(solenoid, GPIO.HIGH)
    GPIO.output(spark, GPIO.HIGH)
    time.sleep(flameTime)
    GPIO.output(solenoid, GPIO.LOW)
    GPIO.output(spark, GPIO.LOW)


def setup():
    # Make sure accelerometer is working
    print('Testing accelerometer, current reading:' + accelerometer.acceleration) 
    #accelerometer.range('0b11')
    accelerometer.enable_motion_detection(threshold=18)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(solenoid, GPIO.IN)
    GPIO.setup(spark, GPIO.IN)

def loop():

    while True:
        print("Current Accelerometer values: %f %f %f"%accelerometer.acceleration)

        print("Motion detected: %s"%accelerometer.events['motion'])
        if accelerometer.events['motion'] == True:
            fire()

        time.sleep(0.5)


