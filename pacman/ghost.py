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

    def changeRandom(self, ghost, turn, steps , pacman_left , pacman_top  ):
      try:
            z = 10000
            moveX = [ 30, 0 , -30, 0 ]
            moveY = [ 0,  30, 0 ,- 30]
            left = self.rect.left
            top = self.rect.top
            if steps < z:
                v = randint( 0,7)
                a = [0,1,2,3]
                if( left < pacman_left ):
                    # 0
                    a.append( 0)
                    a.append(0)
                else:
                    # 2
                    a.append(2)
                    a.append(2)
                if( top < pacman_top):
                    # 1
                    a.append(1)
                    a.append(1)
                else:
                    # 3
                    a.append(3)
                    a.append(3)


                self.change_x = moveX[ a[v] ]
                self.change_y = moveY[ a[v] ]
                steps += 1


            return [turn, steps]
      except IndexError:
          return [0, 0]