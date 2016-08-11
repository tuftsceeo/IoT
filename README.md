# IoT
The Internet of Things project is dedicated to setting various items up on the Internet with new capabilities with 
the ability to tell about themselves and interact as entities with other such items. Specifically here, the EV3 and the Grove Pi.

The purpose of IoT is to give physical devices an online presence. Within two sub-branches of the same goal, the EV3 and GrovePi have been the center of focus. By putting these devices on the Internet of Things, there exists a two-way data stream in which the devices can not only interact with built-in sensors and motors, but can also exchange information to and from the Internet. These devices can now use and create virtual information – taking tactile objects and producing virtual outputs. 


## EV3
The Wifi-enabled EV3 is different than its out-of-the-box counterpart in that it runs a Linux system (Debian) and has a set of wrapper
functions in Python (that I made over the ev3dev wrapper functions) that are called when the appropriate dictionary is given. It is still
compatible with its original sensors and motors but now can also host a web server, grab and produce virtual data, and analyze a whole
new range of data beyond basic sensor values.
