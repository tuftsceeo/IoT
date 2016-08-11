# IoT
The Internet of Things project is dedicated to setting various items up on the Internet with new capabilities with 
the ability to tell about themselves and interact as entities with other such items. Specifically here, the EV3 and the Grove Pi.

(add in general info about each device here)

## EV3
The Wifi-enabled EV3 is different than its out-of-the-box counterpart in that it runs a Linux system (Debian) and has a set of wrapper
functions in Python (that I made over the ev3dev wrapper functions) that are called when the appropriate dictionary is given. It is still
compatible with its original sensors and motors but now can also host a web server, grab and produce virtual data, and analyze a whole
new range of data beyond basic sensor values.
