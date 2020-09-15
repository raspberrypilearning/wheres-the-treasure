#!/bin/python3

from sense_hat import *
from time import sleep
from random import randint

sense = SenseHat()
sense.clear()

# आम्हाला स्वारस्य असलेल्या कृती परत करा
def wait_for_move():
  while True:
    e = sense.stick.wait_for_event()
    if e.action != ACTION_RELEASED:
      return e

R = [255, 0, 0]  # red
Y = [255, 255, 0] # yellow
G = [0, 255, 0] # green
W = [255, 255, 255] # white

