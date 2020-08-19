import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
cam_status= 1

while 1:
    if GPIO.input(13) == False and cam_status == 1:
        cam_status = 0
        print(1)
        time.sleep(1)
    elif GPIO.input(13) == False and cam_status == 0:
        cam_status = 1
        print(2)
        time.sleep(1)
    elif GPIO.input(27) == False and cam_status != 2:
        cam_status = 2
        print(3)
        time.sleep(1)
    elif GPIO.input(27) == False and cam_status == 2:
        cam_status = 1
        print(4)
        time.sleep(1)