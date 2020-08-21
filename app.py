from flask import Flask, render_template, Response, jsonify
from flask_cors import CORS
import cv2

app = Flask(__name__)
CORS(app)
camera = cv2.VideoCapture(0)  # use 0 for web camera
"""In this variable the camera that gets used by CV2 gets defined"""

cam_status = "ok"
room= "1"
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
    data = {'room': room,'cam_status': cam_status}
    return jsonify(data)


@app.route('/')
def index():
    """Home page for the Video Page"""
    return render_template('index.html', kamer_nummer=room)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
