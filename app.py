from flask import Flask, render_template, Response, jsonify
import cv2
import json

app = Flask(__name__)

camera = cv2.VideoCapture(0)  # use 0 for web camera
"""In this variable the camera that gets used by CV2 gets defined"""

status = 1
"""This variable defines how the page will load"""


def gen_frames():  # generate frame by frame from camera
    while True:
        # Capture frame-by-frame
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/status')
def status():
    """Returns an JSON response that contains the content of the data Dict"""
    data = {'status': status}
    response = app.response_class(response=json.dumps(data),
                                  status=200,
                                  mimetype='application/json')
    return response()


@app.route('/')
def index():
    """Home page for the Video Page"""
    return render_template('index.html', kamer_nummer="1")


if __name__ == '__main__':
    app.run(host='0.0.0.0')
