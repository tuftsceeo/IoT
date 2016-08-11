First Time?
--------------

Setting up an EV3 with Linux opens up many new features on the EV3 but you'll probably find that many of the terminal commands, 
libraries, and packages you want have to be installed. This makes sense as it's the way Linux likes to work but that doesn't mean 
it's quick or simple to find the right terminal commands. So here is a walkthrough.

1. **Gather the following supplies/materials:** 
  - an EV3 kit with an EV3 brick and sensors
  - a microSD chip with at least 8(?)GB space (16GB+ ensures you shouldn't run out of space quickly when you update your Linux system 
  and install new library packages)
  - a WIFI dongle (Canakit's WIFI dongle is supposed to work wonderfully with Linux systems - 
  https://www.amazon.com/CanaKit-Raspberry-Wireless-Adapter-Dongle/dp/B00GFAN498); 
  
2. **Next, download the ev3dev EV3 Linux system.** It is Debian-based and has language bindings for Node.js, C++ and Python so you can 
program in all three or in any of those of your choice. For this walkthrough, I will be using Python. Here is the github 
link: https://github.com/ev3dev/ev3dev/releases . Find the most current ev3dev Jessie Linux version (at the time of this writing, 
the most current released version is ev3dev-jessie-2015-12-30). Download the first ZIP file, open and transfer the contents onto 
the microSD card. 

Follow this tutorial for setting up for microSD card: http://www.ev3dev.org/docs/getting-started/

3. **Have your EV3 turned off. Now plug the microSD card into the SD card slot** on the side of your ev3. Try turning on your ev3. When
your ev3 boots, it should now be running Jessie (linux) and Monobrick. Note that the interface will look different from the default 
LEGO interface. As well, the battery in the corner will not tell you a percentage. Rather it is a general range. You should keep an 
eye out for when the battery reaches 6.##. This means it will die soon (when it reaches 5 and it does so fairly quickly). A full 
battery should be around 8.##.

4. **Plug in your WIFI dongle into the USB slot** on the side of the brick to add WIFI searching and connecting capabilities to your brick. This can be removed and plugged in with your ev3 on.

  Now for a few notes about the interface:
  
    1. The first line should say 'File Browser.' This will allow you to click through the files stored on your ev3. Note: This is not 
    ALL files (not from root). It's all files and folders in your 'home' directory and beyond. You can run a program from 
    clicking on it on the brick. But it's a bit finicky so I recommend that you instead use a terminal command.
    
    2. 'Device Browser' is your second option. This lets you choose to see ports, sensors, and motors by category and look at all 
    objects of those kinds currently active (as in plugged in) on the brick. If you select a specific sensor or motor, you can track 
    its current value from the EV3 brick window, as well as its port/address and its name.
    
    3. 'Wireless and Networks' is self-explanatory. You can click the category of connection you want (Bluetooth, Wi-Fi) and select 
    another device or network. You can have both a WIFI and a Bluetooth connection at the same time but Bluetooth supposedly drains
    battery faster than WIFI so be careful to watch the battery if you do. You can also turn your brick 'Offline' if you want, though
    that isn't helpful until I figure out how to run installed programs by clicking on the brick.
    
    4. You probably won't end up using Roberta Lab. That was a new feature added as of the most recent major update on the os system 
    and I haven't looked into its abilities. If you do, let me know and we can update this point.

To progress further, you will need a internet connection. If your network requires device approval you must provide the appropriate
information (like MAC address) to your wireless network. To get your brick's new (unchanging) MAC address from your Wifi dongle, go to
the wireless network of your choice, connect and click down in that network's menu to ENET. Click on this option and click down until
you see 'MAC address' followed by a combination of letters and numbers like this:
    A1:23:4B:5C:67 (this is an example)

5. **Update, Upgrade**
    Once you've installed the system you'll want to update and upgrade all packages on your os system that have newer versions. You 
  should do this every time you want to install a library or other package to make sure that you can use all newer packages. To 
  download anything or update/upgrade anything your brick must be connected to a WIFI network.
  
  Update finds the newest version of all packages while upgrade installs these new versions so it's simple to do update first, then 
  upgrade.

  To do anything with your brick, you must ssh into your brick with the following information.
  - Username: robot
  - Password: maker (This is also the password you will need for using 'sudo'.)
  
  Or in other words, open a termina window, type 'ssh robot@yourRobot'sIP' and when prompted for a password, type 'maker', then press
  the Enter key. Your password will likely not show up on your terminal screen for security reasons but it is still there if you've
  typed it.
  
  To update type in the following line in your terminal:
  - sudo apt-get update
  
  Now type this line to upgrade:
  - sudo apt-get upgrade
  
  This usually takes at least two hours for the first upgrade and will take longer the older your system is compared to the newest 
  version. You may have to run this upgrade command multiple times (and it's a good idea to) until there is nothing left to update. 
  This is because some packages can only be set up if other packages are upgraded and set up first so running the command multiple 
  times should catch that.
  
  Now that your brick's system is up-to-date, you can install some new libraries. The following are the terminal commands for some 
  very helpful libraries you will likely need. It's a good idea to install them now as then you'll have them when you need them. 
  Please type these in order as some downloads depend on the earlier ones. (sudo gives you 'super-user' access to download which you 
  can't always do as a regular user)
  
  - sudo apt-get install apt-utils
  - sudo apt-get install curl
  - sudo curl https://bootstrap.pypa.io/get-pip.py | python 
  	- If that doesn't work and you receive a 'permission denied' error, try this command instead: sudo apt-get install python-pip

  If you see error messages about perl locale (see below) type in the commands below this box into your terminal:
```
  perl: warning: Setting locale failed.
  perl: warning: Please check that your locale settings:
	  LANGUAGE = (unset),
	  LC_ALL = (unset),
	  LANG = "en_US.utf8"
    are supported and installed on your system.
  perl: warning: Falling back to the standard locale ("C").
```
  -  LANGUAGE=en_US.UTF-8
  -  LANG=en_US.UTF-8
  -  LC_ALL=en_US.UTF-8
  -  sudo locale-gen en_US.UTF-8 
     -  This command should show you your current system configuration. All setting values should be 'en_US.UTF-8' (one or two 
	might be blank).
  -  dpkg-reconfigure locales 
     -  Wait and this command will give you a pop up that allows you to set your system confiuration. Choose 'en_US.UTF-8' in the first menu and 'none' in the second menu. Press enter to submit your choice.
  -  sudo locale-gen en_US.UTF-8
     -  Now it should show your updated system configuration.
  -  Thanks to these set commands from https://www.thomas-krenn.com/en/wiki/Perl_warning_Setting_locale_failed_in_Debian .

Some other potentially helpful packages are below:
  - sudo apt-get install locate (Allows you to 'find' any package you have installed or know if one is not installed)

A recent, thorough list of functions for this system can be found here:
  https://media.readthedocs.org/pdf/python-ev3dev/latest/python-ev3dev.pdf

If you use vim to edit you are all set but if you use emacs you will have to install it. Use the following command to install emacs:
  - sudo apt-get install emacs
  
  Emacs is a pretty big download (289 mB) so it will take a while.
  From: http://www.thegeekstuff.com/2010/07/install-emacs-editor-on-linux/?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+TheGeekStuff+(The+Geek+Stuff)

Yay! You're good to go! While you will likely need to install other libraries as your add features to your robot, your EV3 is now all
set to be coded in Python. Great job!

What are the ev3dev Python function names?
--------------
For a full list of ev3dev Python language binding function names, you can check out the below link.
http://ev3dev-lang-python-1.readthedocs.io/en/restruct-docs/index.html

I also recommend looking at ev3dev.org, the main site for the ev3dev system as they have some tutorials and an explanation of most
of the functions for all EV3 sensors and motors.

If you want to use wrapper functions rather than learning to use the ev3dev functions (A project Ethan wanted for the future), or
if you want to see how to call many of these functions in Python, you can check out the wrapper functions in EV3JSON.py in the Event
Server file, where I have a fairly comprehensive set of wrapper functions for most sensor and motor capabilities. 

You'll see there that while some things you would call are functions, others are values you can or will likely want to update, so if
you get an object error, it's a value you have to set, not a function you can call.

Looking to set up a web server?
--------------
Check out the following link for a guide to set up a flask (python) web server on your EV3. However instead of using a physical 
interface with buttons, you can type commands in the terminal while ssh'ed into the EV3.
https://www.raspberrypi.org/learning/python-web-server-with-flask/worksheet/ 

This project is funded by the LEGO Education division of the LEGO Group.
--------------
