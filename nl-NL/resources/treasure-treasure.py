#!/bin/python3

from sense_hat import *
from time import sleep
from random import randint

sense = SenseHat()
sense.clear()

# Geef gewoon de acties terug waarin we geïnteresseerd zijn
def wacht_op_zet():
  while True:
    e = sense.stick.wait_for_event()
    if e.action != ACTION_RELEASED:
      return e

R = [255, 0, 0]  # rood
Y = [255, 255, 0] # geel
G = [0, 255, 0] # groen
W = [255, 255, 255] # wit

