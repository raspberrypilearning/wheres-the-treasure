#!/bin/python3

from sense_hat import *
from time import sleep
from random import randint

sense = SenseHat()
sense.clear()

# Solo devuelve las acciones que nos interesan
def wait_for_move():
  while True:
    e = sense.stick.wait_for_event()
    if e.action != ACTION_RELEASED:
      return e

R = [255, 0, 0]  # rojo
A = [255, 255, 0] # amarillo
V = [0, 255, 0] # verde
B = [255, 255, 255] # blanco

