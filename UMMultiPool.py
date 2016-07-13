# Useless Machine Multi-Threading
# purp: to unpress a lever with a mechanical, motor-powered arm whenever the user presses it; uses pool from multiprocessing library
# last updated: by J.F on July 13, '16 to add comments
# created by: Juliana Furgala

from ev3dev import *
import ev3dev.ev3 as ev3
from multiprocessing import Pool
import time

ts_curr = True
ts2_curr = True


def interpret_command(info):
    m = ev3.LargeMotor('outA')
    ts = ev3.TouchSensor('in1')
    ts2 = ev3.TouchSensor('in4')

    global ts_curr # 1st touch sensor, attached to lever; last saved state
    global ts2_curr  # 2nd touch sensor, reliant on to arm; last saved state

    sm, sep, port = info.partition(":")

    if sm == 'TOUCH':
        if port == 'in1':  # port
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

        if port == 'in4':
            # if the arm is not resting, return to resting position
            while ts.value() == 1 and ts2.value() == 0:
                m.run_forever(duty_cycle_sp=-30)


def main():

    tm_start = time.time()
    tm = 8 # run for 8 seconds from when you start

    sensors = ['TOUCH:in1', 'TOUCH:in4'] # tell it what sensors you have (what_kind:where)

    # make a pool to handle multi-processing
    p = Pool()

    while time.time() < tm_start + tm:
#        for item in sensors:
#            interpret_command(item)
        results = p.map(interpret_command, sensors) # call interpret_command for each sensor in sensors (as in mathematical mapping)

    p.close()
    p.join()

    # to get time of specific actions, call it after each action in while loop with the commented out code, lines 52-53 instead of line 54
    print('Took {}'.format(time.time() - tm)) # time should be approximately 8 seconds, time is in... I think milliseconds


main()
