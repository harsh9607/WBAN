# WBAN
Wireless Body Area Network Simulation via Network programming

Institute : NITRR 

All rights reserved to the Authors

Authors : Harsh Pathak , Vipul Bajaj , N pooja

Instuctor : Dr. Manu Vardhan 

Language used : Python 

**Build instructions** 

**LINUX** 

**Chances are your Distro already came with Python2**

Cross check by opening terminal and typing python and hit enter 

**1) Installing python if not already on your system** 

For debain based distros (Ubuntu and mint) you can easily install Python 2 with the following commands:


*$ sudo apt-get update*


*$ sudo apt-get install python2.7*

**MAKE SURE  YOU RUN THESE 2 Commands (FOR INSTALLING PIP AND PYCRYPTO)** 

*$ sudo apt install python-pip*


*$ pip install pycrypto* 



**2)Checking that python  was successfully installed** 


To cross check if Python  was successfully installed Open your terminal and enter 

*$ python*       

and it will show you the version and other details.

**3) Running the project**
   
*3a) Download the project and unzip it* 

*3b)Open 2 terminals , first one for the PServer.py and second one for Sensor.py*

*3c)change the directory to where your have  unzipped the project in both the terminals*
 
 **INTERPRETING THE SCRIPTS**
 
 **Terminal_One $ python PServer.py**
      
 **Terminal_two $ python Sensor.py**

**WINDOWS** 

**1)DOWNLOAD AND INSTALL PYTHON 2.7**

**2)SETUP THE PATH VARIABLE**

   Open Control Panel, then System
   
   Click 'Advanced system settings' on the left
   
   Click the 'Environment Variables' button

   Just add  C:\Python27; 

**3)DOWNLOAD AND INSTALL PIP** 

   NOTE : To use pip you must add the C:\Python27\Scripts;  into your path variables.
   
   To cross check if the installation was sucessful , Open CMD and type pip and hit enter.
  
**4) INSTALLING PYCRPTO LIBRARY** 

   cmd Terminal >pip install pyCrypto 
   
   Just in case it doesnt work type you can try 
   
   cmd Terminal > pip install pycryptodome

**5)CHANGE DIRECTORY TO WHERE YOU SCRIPT IS**

**6)OPEN CMD AND TYPE**

*C:\Desktop > python PServer.py*

*C:\Desktop > python Sensor.py*
