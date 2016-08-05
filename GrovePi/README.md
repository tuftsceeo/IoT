Grove Pi Documentation

Materials:
- GrovePi Base Kit
- Raspberry Pi2
- WIFI Dongle for Raspberry Pi
- Raspberry Pi Power Supply
- Raspberry Pi Ethernet Cable
- Micro SD Card (Raspbian for robots)
*Dexter Industry Products are highly recommended*

Getting Started with the Grove Pi?
If you are just starting with the GrovePi, here is a step-by-step process to get your GrovePi up and running. 

Setting Up:
1. Attach GrovePi on top of Raspberry Pi - should fit nice and snug.
2. Insert SD card into Raspberry Pi and make sure it clicks
3. Connect a power supply to the Raspberry Pi in the micro USB slot. Two amps is a good amount to start. If you’re not supplying enough energy, you may see problems with your network. If everything is happening successfully, you should see the power light on the side that is solid red with a blinking green, ACT light next to it.
4. Insert ethernet cable into the ethernet port on the Raspberry Pi and plug in the other end to your computer* (or to an external ethernet port). If everything is working well, the two ethernet lights (yellow and green) should appear.
5. You can ssh into your pi on your own computer OR setup a display monitor with keyboard and mouse to continue. *If you don’t have an ethernet port on your own computer, start with a display monitor, keyboard, and mouse.
6. You should see your monitor go through some initial downloads for Raspbian once all connected.
7. Logging onto wifi: click on Wifi Setup on the top left hand corner. Attach a Wifi device to your Raspberry Pi. The space for Adapter in the Setup window should be blank before attaching the wifi dongle; but once in, the adapter name will pop up.
8. Go to Manage Networks tab. Hit Scan. A dialog box of all the available wifi networks will open. Select your desired network. The SSID should be the name of the wifi network. Authentication should be WPA2-Personal(PSK). 
9. Enter your wifi’s password in the PSK space. If no password, leave it blank. Press Add and then Close the scan results. Your desired network should now be listed on the current page.
10. Go to the Current Status tab and the information should automatically fill in. The IP address should take a few seconds to load. Seeing the IP address means you have finally connected over your wifi network. 
11. If the IP address does not appear, you have not connected. Go back to Manage Networks, open up your wifi network and click Edit. Try entering your PSK (password) again. 
12. Now you should be able to successfully ssh onto your own computer! Simply type: ssh pi@IPaddress (for example ssh pi@123.45.67.890)
13. If you’re using Dexter Industry products, the default username is: pi and the default password is: robots1234
14. To confirm that you are connected to wifi, type: ping google.com If you are getting an IP address back, that means it is a successful ping.
15. Press ctrl+c to exit 

Here’s a little video if you’d like to see a full walk-through, step by step:
https://www.youtube.com/watch?v=L0U7GsgMJTI&feature=youtu.be

Change your password if it is still the default password!
When logged in as the pi user, you can change your password with the passwd command. Enter passwd on the command line and hit Enter. You’ll be prompted to enter your current password to authenticate, and then asked for a new password. Hit Enter on completion and you’ll be asked to confirm it. Note that no characters will be displayed while entering your password. Once correctly confirmed, you’ll see a success message and the new password will be in effect immediately. For more information, check out: https://www.raspberrypi.org/documentation/linux/usage/users.md

Using a used Raspberry Pi and SD card? 
Here is a SD Formatter for Mac Download (If you need to reformat your SD card) 
https://www.sdcard.org/downloads/formatter_4/eula_mac/

How to get the Raspberry Pi software to communicate with the GrovePi
The next step is to get the GrovePi communicating with the Raspberry Pi. 
1. Make sure the Raspberry Pi is powered on. Without the GrovePi attached, open a terminal (can SSH on your computer or use terminal on a monitor).
2. Change directories to the Desktop. It is recommended to install the GrovePi software on the Raspberry Pi Desktop. Clone the GrovePi git repository by using the command: 
    cd /home/pi/Desktop
    sudo git clone https://github.com/DexterInd/GrovePi
3. When done downloading, there should be a new folder on the Desktop called GrovePi
4. Go to the Scripts folder in the GrovePi folder.
    cd /home/pi/Desktop/GrovePi/Script
5. Make the install.sh bash script executable. Modify the permissions of the script by entering the following line into the terminal:
    sudo chmod +x install.sh
6. If you type ls -l (that’s two lowercase L’s), the install.sh should now be green. That means it was successfully changed to executable!
7. Now you can start the script. You must be the root user, so make sure to use “sudo”.
    sudo ./install.sh
8. Press Enter when prompted. The script will download packages which are used by the GrovePi. Press y when the terminal prompts and asks for permission to start the download.
9. The Raspberry Pi will automatically restart when the installation is complete. You can stop the reboot process anytime by pressing ctrl+c anytime. However, you must reboot for the update and installation to take effect.
10. Now when the Raspberry Pi is powered down, stack the GrovePi on top. Ensure that the pins are properly connected before powering the Raspberry Pi.
11. Power on the Raspberry Pi. A green light should power up on the GrovePi.
12. To check that the script was correctly installed, check that the Raspberry Pi is able to detect the GrovePi by running the following line on the terminal
    sudo i2cdetect -y 1
    Note: If you have an original raspberry pi (sold before October 2012), the I2C is port 0: sudo i2cdetect -y 0
13. If you can see a “04” in the output, this means the Raspberry Pi is able to detect the GrovePi.
14. To test the GrovePi, connect a Grove LED to port D4 and run the blink example. In the terminal type:
    cd /home/pi/Desktop/GrovePi/Software/Python
    sudo python grove_led_blink.py
If everything is installed correctly and the LED is on the port labeled D4, the LED should start blinking!

For more information and some helpful pictures:
http://www.dexterindustries.com/GrovePi/get-started-with-the-grovepi/setting-software/

Understanding the Grove Ports:
The GrovePi is stacked on top of the Raspberry Pi without the need for any other connections. Communication between the two occurs over the I2C interface. All Grove modules connect to the universal Grove connectors on the GrovePi shield via the universal 4 pin connector cable.

I2C Ports (for sensors like Grove Accelerometer or OLED):
Directly accessible from Raspberry Pi or data can be interpreted by GrovePi and sent to Raspberry Pi

Analog Ports (for reading analog data from sensors like Grove Temperature Sensor):
Accessible from the Raspberry Pi by sending commands to the GrovePi

Digital Ports (for digital input and output, can be used for switches or sensors like Ultrasonic Ranger):
Accessible from the Raspberry Pi by sending commands to the GrovePi

Raspberry Pi Serial (for serial I/O to the Raspberry Pi):
Grove Serial modules can be directly connected and used by the Raspberry Pi

GrovePi Serial (for serial I/O to the GrovePi. Grove Serial modules can be connected, its data interpreted and sent to the RaspberryPi):
Not connected to the Raspberry Pi directly.

For more information about ports: http://www.dexterindustries.com/GrovePi/engineering/port-description/

Raspberry Pi Projects for the Grove Pi Sensors:
There are many good examples using all of the sensors, including: LED blink, LED Fade, Tilt Buzzer, Home Weather Display, Sensor Twitter Feed, Who’s at the Door, Open Wifi Finder, and more obscure projects. 
Find them all here: http://www.dexterindustries.com/GrovePi/projects-for-the-raspberry-pi/

A good example, the Sensor Twitter Feed, reads the current temperature, light, and sound and instantly prints it out as a tweet. Check out this tutorial on how to send a tweet from a python script (uses tweepy import [Dexter tutorial uses twitter import which doesn’t work as well]):
http://nodotcom.org/python-twitter-tutorial.html

You could try the opposite of this project and start with the web: Twitterverse. Turn on an LED every time it detects a specific hashtag posted on Twitter. Check out this website for further information: https://learn.sparkfun.com/tutorials/raspberry-pi-twitter-monitor
 
Connecting an EV3 with an Arduino (which could be copied on a GrovePi)
http://www.dexterindustries.com/howto/connecting-ev3-arduino/

Interested in Building a Python-Powered Web Server with Flask?
Install the lightweight web framework Flask (sudo pip install -U flask-cors) and set up a basic web server with different pages, using Python, HTML, and CSS. Here is a really thorough step-by-step tutorial: https://www.raspberrypi.org/learning/python-web-server-with-flask/worksheet/

What do the GrovePi sensors return? 
LED: 1 - 255 for On and its brightness and 0 for Off
Button: 1 for pressed and 0 for not
Rotary Angle Sensor: 1 - 300 for angle
Light sensor: 0 - 720+. With a finger covering the sensor, value went down to 240. 
Temperature & Humidity Sensor: Returns temperature in Celsius and humidity in RH percentage.
Buzzer: prints out “successful set”, otherwise will buzz!
Sound: anywhere from 0 - 100+
Ultrasonic: returns the distance in centimeters, up to 400 cm away.
Display: prints out “successful set”, and will appear on LCD Backlight
