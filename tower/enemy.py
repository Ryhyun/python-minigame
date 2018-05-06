import pygame

class Enemy:
    def __init__(self):
        self.hp = 1
        self.icon = pygame.image.load('image/enemy.png')
        self.width = 20
        self.height = 20
        self.isShot = False
        self.speed = 3
        self.initX = 0
        self.initY = 0
        self.x =0
        self.y =0


    def setPosition(self, x, y):
        self.initX = x
        self.initY = y
        self.x = x
        self.y = y


class Boss:
    def __init__(self):
        self.hp = 10;

        self.icon = pygame.image.load('image/devil.png')
        self.width = 40
        self.height = 40
        self.speed = 0
        self.x=0;
        self.y=0 ;
        self.initX = 0
        self.initY = 0

    def setPosition(self, x, y):
        self.initX = x
        self.initY = y
        self.x = x
        self.y= y






