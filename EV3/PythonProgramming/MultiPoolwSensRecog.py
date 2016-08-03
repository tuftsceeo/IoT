# Useless Machine Multiprocessing with Sensor Recognition
# purp: to unpress a lever with a mechanical, motor-powered arm whenever the user presses it; includes sensor detection 
#   and autopopulation of a list of sensors to check
# last updated: by J.F on July 25, '16 to add comments
# created by: Juliana Furgala

from ev3dev import *
import ev3dev.ev3 as ev3
from multiprocessing import Pool
import os
import time
# import tweepy

ts_curr = True
ts2_curr = True


class Sensor():
    def __init__(self, driver_name, address):
        self.driver_name = driver_name
        self.address = address


class Motor():
    def __init__(self, driver_name, address):
        self.driver_name = driver_name
        self.address = address


def interpret_command(info):
    m = ev3.LargeMotor('outA')
    ts = ev3.TouchSensor('in1')
    ts2 = ev3.TouchSensor('in4')

    global ts_curr # 1st touch sensor, attached to lever; last saved state
    global ts2_curr  # 2nd touch sensor, reliant on to arm; last saved state

    sm = info.driver_name
    port = info.address

    if sm == ['lego-ev3-touch']:
        if port == ['in1']:  # port/address
            # if lever is not pressed, stop
            if ts_curr == False and ts.value() == 1:
                ts_curr = True
            while ts_curr == True and ts.value() == 1:
                m.stop()

            # if lever is pressed, 'unpress' the button with the arm
            if ts_curr == True and ts.value() == 0:
                 ts_curr = False
            while ts_curr == False and ts.value() == 0:
                 m.run_forever(duty_cycle_sp=60)

        if port == ['in4']:
             # if the arm is not resting, return to resting position
             while ts.value() == 1 and ts2.value() == 0:
                 m.run_forever(duty_cycle_sp=-30)

#    if port == ['in4']:
#        if ts2.value() == 1:
#            sendTweet()


# information for this demo function and code outline came from an online tutorial at:
# nodotcom.org/python-twitter-tutorial.html
# def sendTweet():
#     def get_api(cfg):
#         auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
#         auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
#         return tweepy.API(auth)
#
#     cfg = {
#         "consumer_key" : "JoSQnthNuxFuNDANF7gLKHAhg",
#         "consumer_secret" : "Hu0ShH3pU5Ejxp2HR6njwxRjVDVoKrp34G4vt9RF4pq5Tn7Yv7",
#         "access_token" : "4386651495-uBBJfHnhegqqZE6XFPC8eYre8CZtTJYBkTo3hVy",
#         "access_token_secret" : "dZPNiJpxiz6gaKg4GBPVoxudfWulo5bunvgGEdvOHNaJK"
#     }
#
#     api = get_api(cfg)
#     tweet = "Is it ironic?" # your message
#     status = api.update_status(status=tweet)
#    print status


def searchPorts(typeToCheck):
    if typeToCheck == "Sensor":  # if you want to check sensors
        dir = os.listdir('/sys/class/lego-sensor')
    if typeToCheck == "Motor":  # if you want to check for motors
        dir = os.listdir('/sys/class/tacho-motor')
    elif typeToCheck is not "Sensor" and typeToCheck is not "Motor": # if you want something else...
        return # no

    lst = []  # a list of sensor/motor structs, initially empty

    for item in dir:  # for all files and directories in lego-sensor folder, aka sensors by order plugged in (0,1,...)
        try:
            if typeToCheck == "Sensor":  # if you want to check for sensors
                # make a list of info to find about the sensor
                find = ['driver_name', 'address']
                i = 0
                for x in find: # for each info piece you want open the file and read the value
                    with open('/sys/class/lego-sensor/'+item+'/'+x) as infoFile:
                        find[i] = [line.rstrip('\n') for line in infoFile]
                        #print find[i]
                        i = i + 1
                mysens = Sensor(find[0], find[1])
                lst.append(mysens)

            if typeToCheck == "Motor":
                # make a list of info to find about the motor
                find = ['driver_name', 'address']
                i = 0
                for x in find: # for each info piece you want open the file and read the value
                    with open('/sys/class/tacho-motor/'+item+'/'+x) as infoFile:
                        find[i] = [line.rstrip('\n') for line in infoFile]
                        #print find[i]
                        i = i + 1
                mymot = Motor(find[0], find[1])
                lst.append(mymot)

        except IOError:
            print "You don't have a " + typeToCheck + " plugged in here. Check to see if everything is plugged in."

    return lst


def main():

    tm_start = time.time()
    tm = 20

    p = Pool()

    sensors = searchPorts("Sensor")
    for item in sensors:
        print 'You have a ' + str(item.driver_name) + ' plugged in at port ' + str(item.address)
    motors = searchPorts("Motor")
    for item in motors:
        print 'You have a ' + str(item.driver_name) + ' plugged in at port ' + str(item.address)

    while time.time() < tm_start + tm:
#        for item in sensors:
#            interpret_command(item)
         results = p.map(interpret_command, sensors)

    p.close()
    p.join()

    print('Took {}'.format(time.time() - tm))


main()
