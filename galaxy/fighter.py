import pygame

class Fighter:
    def __init__(self):
        self.hp = 10
        self.icon = pygame.image.load('image/fighter.png')

        self.width = 36
        self.height= 38
        self.x = 0;
        self.y= 0;
        self.initX = 0
        self.initY = 0
        self.change = 0

    def setPosition(self,x,y):
        self.initX = x
        self.initY = y

    def moveFighter(self, x):
        self.change += x






class Bullet:
    def __init__(self):
        self.bullets = 1;
        self.icon = pygame.image.load('image/bullet.png')
        self.x =0
        self.y =0

    def moveBullet(self,x,y):
        self.x = x
        self.y = y

