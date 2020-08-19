## Room monitoring with Flask, Open-CV and Raspberry Pi GPIO
```python
pip3 install -r requirements.txt
```
### Run Server
```python
python3 app.py
```
### GPIO Used
GPIO 13 will trigger SOS status
GPIO 27 Will trigger camera status
Status of the GPIO will be available on /status for external monitoring

 ## Credit
 Learn More about Streaming with flask
 - https://blog.miguelgrinberg.com/post/video-streaming-with-flask
