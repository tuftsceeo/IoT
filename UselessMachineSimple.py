# Useless Machine

from ev3dev import *
import ev3dev.ev3 as ev3
import time

m = ev3.LargeMotor('outA')

ts = ev3.TouchSensor('in1')
ts2 = ev3.TouchSensor('in4')

print ts.driver_name
print ts.address
print ts.mode
print ts.num_values
#print ts.units
print ts.modes

print " "

print m.driver_name
print m.address
print m.commands
print m.duty_cycle
print m.position
#print m.max_speed

go = True

while go == True:
	print m.state
	while ts.value() == True:
		m.stop()
		continue # do nothing
	while ts.value() == False:
		m.run_forever(duty_cycle_sp = 60)
		continue
	while ts2.value() == False:
		m.run_forever(duty_cycle_sp = -30)
		continue
	