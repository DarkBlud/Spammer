#import library
from itertools import count
import platform
import pyautogui as pg 
import time 
import os
# os.system("pip install -r requirements.txt && clear")

system = platform.system() 

def windows():
    #Warning 
    os.system("color 0C && cls") 
    print("Important ;; Do not change the page until the program finish")
    input("Press Any thing to continue ...")
    os.system("color 02 && cls")  
    #Get Data


    counter = int(input("Enter count of message  : "))
    msg = input("Enter your message : ")

    #Action


    os.system("start Terminal.py")
    time.sleep(10)
    for i in range(counter): 
        pg.write(msg)
        pg.press("Enter")
    os.system("cls")
    windows()

def linux():
    os.system('clear')
    os.system("pip install -r requirements.txt && clear") 
    os.system('clear')  
    print("Important ;; Do not change the page until the proggrame finish")
    input("Press Any thing to continue ...")
    os.system("clear")
    counter = int(input("Enter count of message  : "))
    msg = input("Enter your message : ")
    os.system("gnome-terminal -- python Terminal.py")
    time.sleep(10)
    for i in range(counter): 
        pg.write(msg)
        pg.press("Enter")
    os.system('clear')
    linux()


if system == "Linux":
    linux()
elif system == "Windows":
    windows()
else:
    print("This program can't run on your system \n Please use Windows or Linux <3")
#IG : dark._.blud
#Github : DarkBlud
