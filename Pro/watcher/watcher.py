from flask import Flask, render_template, url_for, Response
from scanner import Scanner

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/help')
def help():
    return render_template('help.html')


@app.route('/live')
def live():
    return render_template('live.html')


def gen(scanner):
    while True:
        frame = scanner.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(Scanner()), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(debug=False)
