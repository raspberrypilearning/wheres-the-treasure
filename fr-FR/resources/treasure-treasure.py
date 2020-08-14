#!/bin/python3

from sense_hat import *
from time import sleep
from random import randint

sense = SenseHat()
sense.clear()

# On renvoie seulement les actions qui nous intéressent
def attendre_mouvement():
  while True:
    e = sense.stick.attendre_evenement()
    if e.action != ACTION_RELEASED:
      return e

R = [255, 0, 0]  # rouge
J = [255, 255, 0] # jaune
V = [0, 255, 0] # vert
W = [255, 255, 255] # blanc

