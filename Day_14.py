#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 09:45:51 2020

@author: venky

Modules needed
psutil(python system and process utilities): It is a cross-platform for retrieving information on running processes and system utilization in python
pip install psutil
plyer: Plyer module is used to access the features of the hardware. This module does not comes built-in with Python. We need to install it externally. To install this module type the below command in the terminal.
pip install plyer
Approach:

Step 1) Import the notification class from the plyer module

from plyer import notification
Step 2) After that you just need to call the notify method of this class.

Syntax: notify(title=”, message=”, app_name=”, app_icon=”, timeout=10, ticker=”, toast=False)

Parameters:

title (str) – Title of the notification
message (str) – Message of the notification
app_name (str) – Name of the app launching this notification
app_icon (str) – Icon to be displayed along with the message
timeout (int) – time to display the message for, defaults to 10
ticker (str) – text to display on status bar as the notification arrives
toast (bool) – simple Android message instead of full notification
Step 3) Add the sleep function to show that notification again.

    """
import psutil 
from plyer import notification 
import time 


battery = psutil.sensors_battery() 

# from psutil we will import the 
# sensors_battery class and with 
# that we have the battery remaining 
while(True): 
	percent = battery.percent 
	
	notification.notify( 
		title="Battery Percentage", 
		message=str(percent)+"% Battery remaining", 
		timeout=10
	) 
	
	# after every 60 mins it will show the 
	# battery percentage 
	time.sleep(60*60) 
	
	continue


"""

import psutil 
from plyer import notification 
import time 
  
  
battery = psutil.sensors_battery() 
  
# from psutil we will import the  
# sensors_battery class and with 
# that we have the battery remaining 
def Notification():
    percent = battery.percent 
      
    notification.notify( 
        title="Battery Percentage", 
        message=str(percent)+"% Battery remaining", 
        timeout=10
    ) 
      
    # after every 60 mins it will show the 
    # battery percentage 
    time.sleep(60*30) 
    

if __name__ == '__main__': 
    Notification() 
    
"""    