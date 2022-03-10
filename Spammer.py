#import library


from itertools import count
import pyautogui as pg 
import time 
import os
os.system("pip install -r requirements.txt && cls")

#Warning 
os.system("color 0C") 
print("Important ;; Do not change the page until the proggrame finish")
input("Press Any thing to continue ...")
os.system("color 02") 
#Get Data


counter = int(input("Enter count of message  : "))
msg = input("Enter your message : ")

#Action


os.system("start C:/Users/DarkBlud/Desktop/spamm/Terminal.py")
time.sleep(10)
for i in range(counter): 
    pg.write(msg)
    pg.press("Enter")

#IG : dark._.blud
#Github : DarkBlud
