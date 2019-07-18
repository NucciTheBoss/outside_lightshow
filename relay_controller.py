# Will probably be located in programs folder on raspberry pi
# This will be the file that is stored on the pi zero as the controller
# for the mechanical relays that I will be using to power my lights
# There will also be functions in here to help with the communication between
# my two raspberry pis
#
# Author: Jason C. Nucciarone
# Drafted: 7/10/2019

# Once hardware is finished, then we can start figuring out
# how we are going to choreograph the music

import RPi.GPIO as gp
import time
import threading
import os

from collections import deque

# Set gpio mode to broadcom and set warnings to false
gp.setmode(gp.BCM)
gp.setwarnings(False)

# Set channels for each of the outlets
# Channels will be seperated across two seperate mechanical relays
# 2 is outlet1
# 3 is outlet2
# 4 is outlet3
# 17 is outlet4
# 27 is outlet5
# 22 is outlet6
# 10 is outlet7
# 9 is outlet8
# 23 is outlet9
# 24 is outlet10
# 25 is outlet11
#  8 is outlet12
# 7 is outlet13
# 1 is outlet14
# 12 is outlet15
# 16 is outlet16

# For the initial set up of the pins
# avoid gp.cleanup() as it will screw the whole setup
pinList = [2, 3, 4, 17, 27, 22, 10, 9,
           23, 24, 25, 8, 7, 1, 12, 16]

for pin in pinList:
    gp.setup(pin, gp.OUT)
    gp.output(pin, gp.HIGH)

# Pin groups for each music element
beatList = [2, 3, 4]
voiceList = [17, 27, 22]
melodyList = [10, 9]
tempoList = [23, 24, 25, 8, 7, 1]
rhythmList = [12, 16]



# Build deques for my playlists, will alter as I please
# Songs will be played through omxplayer unless
# I feel like building my own audio player

# Will need to use popleft to play the first song in the queue
absolute_bops = deque()
absolute_bopsSongs = ["durga.mp3", "everything.mp3", "festival_of_lights.mp3",
                      "freaks.mp3", "harder_better_faster_stronger_bass_boosted.mp3",
                      "i_like_to_move_it.mp3", "live_your_life.mp3", "melody.mp3",
                      "moksha.mp3", "neverland.mp3", "party_till_we_die.mp3",
                      "psy_or_die.mp3", "punjabi.mp3", "strong.mp3",
                      "this_is_nightlife_remix.mp3"]
for song in absolute_bopsSongs:
    absolute_bops.append(absolute_bopsSongs[song])

ariana_grande = deque()
ariana_grandeSongs = ["bang_bang.mp3", "breathin.mp3", "into_you.mp3",
                      "no_tears_left_to_cry.mp3", "one_last_time.mp3",
                      "problem.mp3", "side_to_side.mp3"]
for song in ariana_grandeSongs:
    ariana_grande.append(ariana_grandeSongs[song])

britney_spears = deque()
britney_spearsSongs = ["baby_one_more_time.mp3", "circus.mp3", "gimme_more.mp3",
                      "hold_it_against_me.mp3", "i_wanna_go.mp3",
                      "if_u_seek_amy.mp3", "oops_i_did_it_again.mp3",
                      "three.mp3", "till_the_world_ends.mp3", "toxic.mp3",
                      "womanizer.mp3", "work_bitch_remix.mp3"]
for song in britney_spearsSongs:
    britney_spears.append(ariana_grandeSongs[song])

cascada = deque()
cascadaSongs = ["bad_boy.mp3", "dangerous.mp3", "evacuate_the_dancefloor.mp3",
                "everytime_we_touch.mp3", "miracle.mp3",
                "ready_or_not.mp3"]
for song in cascadaSongs:
    cascada.append(cascadaSongs[song])

# Will add more playlists as I feel the need to add them

# Functions to help speed up the control of the relays
def allOff():  # To open all relays before beginning new song
    for pin in range(len(pinList)):
        gp.output(pinList[pin], gp.HIGH)

# Breifer method for closing relay
def relay_closed(pin_number):
    gp.output(pin_number, gp.LOW)

# Breifer method for opening relay
def relay_open(pin_number):
    gp.output(pin_number, gp.HIGH)


if __name__ == "__main__":
    try:
        # Where all processes will be executed
        while cascada.count() != 0:
            song_name = cascada.popleft()
            os.system("omxplayer /home/pi/lightshowpi/music/cascada/{}".format(song_name))


    except KeyboardInterrupt:
        os.system("sudo killall omxplayer")
        allOff()
