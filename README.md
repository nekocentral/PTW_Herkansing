## Room monitoring with Flask, Open-CV and Raspberry Pi GPIO
```python
pip3 install -r requirements.txt
sudo apt-get install libopencv-dev python3-opencv
```
### Run Server
```python
python3 app.py
```
### GPIO Used
GPIO 13 will trigger SOS status  
GPIO 27 Will trigger camera status  
Status of the GPIO will be available on /status for external monitoring

![Raspberry GPIO Pinout](https://pythonprogramming.net/static/images/rpi/raspberry_pi_gpio-shutdown-pins.png)

 ## Credit
 Learn More about Streaming with flask
 - https://blog.miguelgrinberg.com/post/video-streaming-with-flask
 
 Raspberry Pi GPIO Image
  - https://pythonprogramming.net/gpio-raspberry-pi-tutorials/
