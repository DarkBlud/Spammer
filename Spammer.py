#import library
pip install -r "requirements.txt"

from itertools import count
import pyautogui as pg 
import time 
import os

#Get Data


counter = int(input("Please Enter count of spamming message :) ( Do not open any other page just stay on that page you want ) : "))
msg = input("Enter your message : ")

#Action


os.system("start C:/Users/DarkBlud/Desktop/spamm/Terminal.py")
time.sleep(10)
for i in range(counter): 
    pg.write(msg)
    pg.press("Enter")

#IG : dark._.blud
#Github : DarkBlud
