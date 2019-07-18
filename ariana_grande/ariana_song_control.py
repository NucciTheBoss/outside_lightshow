# Main file where relays are controlled, each sub_section of relay is
# handled as a seperate task, and music is controlled in the main
# app, relay_controller.py

import RPi.GPIO as gp
import threading
import time
import relay_functions as rf


gp.setmode(gp.BCM)
gp.setwarnings(False)


pinList = [2, 3, 4, 17, 27, 22, 10, 9,
           23, 24, 25, 8, 7, 1, 12, 16]


# Pin groups for each music element
beatList = [2, 3, 4]
voiceList = [17, 27, 22]
melodyList = [10, 9]
tempoList = [23, 24, 25, 8, 7, 1]
rhythmList = [12, 16]

rf.pinSetup(pinList)

arianaSongs = ["bang_bang.mp3", "breathin.mp3", "into_you.mp3",
               "no_tears_left_to_cry.mp3", "one_last_time.mp3",
               "problem.mp3", "side_to_side.mp3"]

# Function for beat relays
def arianaBeat(song):
    if song == arianaSongs[0]:
        pass

    elif song == arianaSongs[1]:
        pass

    elif song == arianaSongs[2]:
        pass

    elif song == arianaSongs[3]:
        pass

    elif song == arianaSongs[4]:
        pass

    elif song == arianaSongs[5]:
        pass

    else:
        pass


def arianaVoice(song):
    if song == arianaSongs[0]:
        pass

    elif song == arianaSongs[1]:
        pass

    elif song == arianaSongs[2]:
        pass

    elif song == arianaSongs[3]:
        pass

    elif song == arianaSongs[4]:
        pass

    elif song == arianaSongs[5]:
        pass

    else:
        pass


def arianaMelody(song):
    if song == arianaSongs[0]:
        pass

    elif song == arianaSongs[1]:
        pass

    elif song == arianaSongs[2]:
        pass

    elif song == arianaSongs[3]:
        pass

    elif song == arianaSongs[4]:
        pass

    elif song == arianaSongs[5]:
        pass

    else:
        pass


def arianaTempo(song):
    if song == arianaSongs[0]:
        pass

    elif song == arianaSongs[1]:
        pass

    elif song == arianaSongs[2]:
        pass

    elif song == arianaSongs[3]:
        pass

    elif song == arianaSongs[4]:
        pass

    elif song == arianaSongs[5]:
        pass

    else:
        pass


def arianaRhythm(song):
    if song == arianaSongs[0]:
        pass

    elif song == arianaSongs[1]:
        pass

    elif song == arianaSongs[2]:
        pass

    elif song == arianaSongs[3]:
        pass

    elif song == arianaSongs[4]:
        pass

    elif song == arianaSongs[5]:
        pass

    else:
        pass

# Main function for playing choreographed songs
def playArianaSong(song):
    # Song is queued up from main program
    if song == arianaSongs[0]:
        pass

    elif song == arianaSongs[1]:
        pass

    elif song == arianaSongs[2]:
        pass

    elif song == arianaSongs[3]:
        pass

    elif song == arianaSongs[4]:
        pass

    elif song == arianaSongs[5]:
        pass

    else:
        pass
