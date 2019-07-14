# Test file to see if all my outlets are working correctly
# Will also help me see if I have my pi wired correctly

import RPi.GPIO as gp
import time

gp.setmode(gp.BCM)
gp.setwarnings(False)

pinList = [2, 3, 4, 17, 27, 22, 10, 9,
           23, 24, 25, 8, 7, 1, 12, 16]

for pin in pinList:
    gp.setup(pin, gp.OUT)
    gp.output(pin, gp.HIGH)

# Run testing loop until I hit crtl-c
try:
    x = True
    while x is True:
        for pin in pinList:
            gp.output(pin, gp.LOW)
            time.sleep(.5)  # Wait 50 milliseconds before moving to next relay
            gp.output(pin, gp.HIGH)

except KeyboardInterrupt:
    exit()  # Exit the program once I am done testing
