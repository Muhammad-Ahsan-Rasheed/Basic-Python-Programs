# Automation script to check for zoom instance running and if its running then send message to the whatsapp 
# in meeting.

import os
import time
import pyautogui
import pywhatkit
import datetime
import subprocess

# Function to check if zoom is running or not
def check_zoom():
    # Get the process id of zoom
    pid = subprocess.check_output("pgrep zoom", shell=True)
    # If pid is not empty then zoom is running
    if pid:
        return True
    else:
        return False

# Function to send message to whatsapp
def send_message():
    # Get the current time
    now = datetime.datetime.now()
    # Get the current hour
    hour = now.hour
    # Get the current minute
    minute = now.minute
    # Get the current second
    second = now.second
    # Get the current microsecond
    microsecond = now.microsecond
    # Send the message to the whatsapp
    pywhatkit.sendwhatmsg('+923126743467', 'Zoom is running', hour, minute + 1, 10)

# main function
def main():
    # Check if zoom is running or not
    if check_zoom():
        # If zoom is running then send message to the whatsapp
        send_message()
    else:
        # If zoom is not running then print the message
        print("Zoom is not running")

# Call the main function
main()