# tutorial for set-up found here: https://www.raspberrypi.org/learning/python-web-server-with-flask/worksheet/
from flask import Flask, render_template, request, json
from flask_cors import CORS, cross_origin
from ev3dev import *
import ev3dev.ev3 as ev3
import logging, time

PYTHONIOENCODING = 'utf-8'  # set the language to standard English characters (in case your system isn't)

# m = ev3.LargeMotor('outA')
# ts = ev3.TouchSensor('in1')

app = Flask(__name__)
# basic logging, tells you when you have received a request ('GET'/'POST', etc.)
logging.basicConfig(level=logging.INFO)

# advanced debugging log, to use, uncomment line below
# logging.getLogger('flask_cors').level = logging.DEBUG

# resources = what pages you want to have access allowed to, can be 1 page, in this case is '/' (home page)
# origin = the list of allowed IP addresses to connect, your own is already allowed
# methods = what can the user/person do to the page(s)
CORS(app, resources=r'/*', origin="http://130.64.94.22:8888/", methods=["GET", "POST"])


# Inspiration for methods parameter and if method == format
# https://github.com/distortenterprises/Webinterface
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        JSONinput = request.get_data()

#        print("Command received")
        data = json.loads(JSONinput)
#        print(
#            "status is ", data['status'], " and sm_type is", data['sm_type'], " and port is ", data['port'], " and info is ", data['info'], " and value is ", data['value'])
        requesteddata = str(process_command(data))
        return json.jsonify(httpCode=200, value=requesteddata)

    elif request.method == "GET":
        # return render_template('index.html')
        return "Successful get request"


def process_command(data):
    status = data['status']
    sm_type = data['sm_type']
    
    result = "Not found"
    if status == 'get':
        if sm_type == 'touch':
            result = get_touch(data['port'], data['info'])
        if sm_type == 'large motor':
            result = get_lm(data['port'], data['info'])
    if status == 'set':
        if sm_type == 'large motor':
            set_lm(data['port'], data['info'], data['value'])
        return "successful set"
    return result
    

# get_touch
#   purp: to return the current value from a touch sensor
def get_touch(port, info):
    try:
        if info == 'value':
            return ev3.TouchSensor(port).value()
    except ValueError:
        return "Not found"


# get_lm
#   purp: to return a value/stat from a large motor
def get_lm(port, info):
    try:
        if info == 'position':
            return ev3.LargeMotor(port).position()
    except ValueError:
        return "Not found"


# set_lm
#   purp: to run a function for a large motor with a given value
def set_lm(port, info, value):
    try:
        i = ev3.LargeMotor(port)
        power = int(value)
        if info == 'run_forever':
            i.run_forever(duty_cycle_sp=power)
            time.wait(1)
            # i.run_timed(time_sp = 1000000000, duty_cycle_sp = value)
        if info == 'stop':
            i.stop()
        if info == 'reset':
            i.reset()
    except ValueError:
        return "Not found"


@app.route('/1', methods=["GET", "POST"])
def index1():
    if request.method == "POST":
        if request.form['direction'] == 'forward':
            m.run_forever(duty_cycle_sp=40)
        if request.form['direction'] == 'backward':
            m.run_forever(duty_cycle_sp=-40)
        if request.form['direction'] == 'stop':
            m.stop()
        print("Command received")
        print(request.form['direction'])
        return render_template('index.html')
    if request.method == "GET":
        return render_template('index.html')


@app.errorhandler(400)
def client_error(error):
    app.logger.error('Client Error: %s', error)
    return ('{httpCode: %s}', error)


@app.errorhandler(500)
def internal_server_error(error):
    app.logger.error('Server Error: %s', error)
    return ('{httpCode: %s}', error)
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
