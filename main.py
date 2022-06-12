import random
from math import trunc
from random import randint
import time
import keyboard

guessSeconds = 0



def titleScreen():
    choice = input("How well is your perception of time? 1) Go")
    if choice == "1":
        press()


def press():
    global guessSeconds
    guessSeconds = randint(4, 12)
    print("-------------------------------------------------------------------")
    print("Don't press W until " + str(guessSeconds) + " seconds has passed")
    playerCount = 0
    timeStart = time.time()
    ispress = False
    while not ispress:
        if keyboard.is_pressed('w'):
            ispress = True

    timeEnd = time.time()

    timeSpent = timeEnd - timeStart
    timeConvertToMakePretty(timeSpent)


def timeConvertToMakePretty(time):
    global guessSeconds
    diff = abs(guessSeconds - round(time, 2))
    print("-------------------------------------------------------------------")
    print("You were " + str(diff) + " seconds off. You stopped at " + str(round(time, 2)) + " seconds")
    print("-------------------------------------------------------------------")
    titleScreen()


titleScreen()
