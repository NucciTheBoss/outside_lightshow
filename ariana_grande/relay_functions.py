# Functions that make realy setup and control much easier

import RPi.GPIO as gp
# Setmode and setwarnings will be included in main song file
# This is just to help make the pin initialization and control
# much easier

def pinSetup(pinList):
    for pin in pinList:
        gp.setup(pin, gp.OUT)
        gp.output(pin, gp.HIGH)
    return


def allOff(pinList):
    for pin in pinList:
        gp.output(pin, gp.HIGH)
    return


def relay_closed(pin_number):
    gp.output(pin_number, gp.LOW)
    return


def relay_open(pin_number):
    gp.output(pin_number, gp.HIGH)
    return
