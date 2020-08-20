#!/bin/python3
# a simple script for using the tactile buttons on the TFT
import signal
import RPi.GPIO as GPIO
import time
import subprocess
import os


GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP) # SOS Status
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Camera Status
"""Setup the GPIO Pins with their Internal pullups and set them in read mode"""

#  Main Loop
status = 1
p=subprocess.Popen("python3 /home/pi/cam/app.py", shell=True, preexec_fn=os.setsid)
try:
    while 1:
        if GPIO.input(27) == False and status == 1:
            os.killpg(p.pid, signal.SIGTERM) #Kill The camera stream
            p = subprocess.Popen("python3 /home/pi/cam/off.py", shell=True,
                                 preexec_fn=os.setsid) #Start the new page with offline status
            status = 0
            time.sleep(1)
        elif GPIO.input(27) == False and status == 0:
            os.killpg(p.pid, signal.SIGTERM)  # Kill The camera stream
            p = subprocess.Popen("python3 /home/pi/cam/app.py", shell=True,
                                 preexec_fn=os.setsid)  # Start the new page with offline status
            status = 1
            time.sleep(1)
        elif GPIO.input(13) == False and status != 2:
            os.killpg(p.pid, signal.SIGTERM)  # Kill The camera stream
            p = subprocess.Popen("python3 /home/pi/cam/sos.py", shell=True,
                                 preexec_fn=os.setsid)  # Start the new page with offline status
            status = 2
            time.sleep(1)
        elif GPIO.input(13) == False and status == 2:
            os.killpg(p.pid, signal.SIGTERM)  # Kill The SOS stream
            p = subprocess.Popen("python3 /home/pi/cam/app.py", shell=True,
                                 preexec_fn=os.setsid)  # Start the new page with camera
            status = 1
            time.sleep(1)
except KeyboardInterrupt:
    os.killpg(p.pid, signal.SIGTERM)