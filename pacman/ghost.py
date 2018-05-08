import pygame
from player import Player
from random import *
class Ghost(Player):
    # Change the speed of the ghost
    def changespeed(self,list,ghost,turn,steps,l):
      try:
        z=list[turn][2]
        if steps < z:
          self.change_x=list[turn][0]
          self.change_y=list[turn][1]
          steps+=1
        else:
          if turn < l:
            turn+=1
          elif ghost == "clyde":
            turn = 2
          else:
            turn = 0
          self.change_x=list[turn][0]
          self.change_y=list[turn][1]
          steps = 0
        return [turn,steps]
      except IndexError:
         return [0,0]

    def changeRandom(self, ghost, turn, steps):
      try:
          z = 1000
          moveX = [ 30, 0 , -30, 0 ]
          moveY = [ 0,  30, 0 ,- 30]
          if steps < z:
              v = randint( 0,3)
              self.change_x = moveX[ v ]
              self.change_y = moveY[ v]
              steps += 1


          return [turn, steps]
      except IndexError:
          return [0, 0]