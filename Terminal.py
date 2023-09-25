#import part


import os
import time
import platform 

#set var
system = platform.system()

def windows():
    cmd = os.system
    cmd("title Terminal")
    cmd("color 0C")
    x = 10

    #Action


    for i in range(10):
        print(f"Time remain : {x}")
        time.sleep(1)
        x += -1
        cmd("cls")
        cmd('exit')
    

def linux():
    ter = os.system 
    ter("clear")
    timer = 10 
    for i in range(10):
        print(f"Time remain : {timer}")
        time.sleep(1)
        timer += -1 
        ter('clear')
        ter('exit')
    

if system == "Windows" : 
    windows()
elif system == "Linux" : 
    linux()
else : 
        print("This program can't run on your system \n Please use Windows or Linux <3")


#Ig : dark._.blud
#Github : DarkBlud
