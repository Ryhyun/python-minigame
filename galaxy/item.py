import pygame

class item():
    def __init__(self):
        self.x
        self.y

    def print_item(self):
        print("item")


# 체력 업
class HP_UP( item):
    def __init__(self):
        self.icon = pygame.image.load('image/HP_UP.png')
    def print_item(self):
        print("HP_UP")


# 파워 업
class POWER_UP( item):
    def __init__(self):
        self.icon = pygame.image.load('image/POWER_UP.png')

    def print_item(self):
        print("POWER_UP")
# 점수 업
class SCORE_UP(item):
    def __init__(self):
        self.icon = pygame.image.load('image/SCORE_UP.png')

    def print_item(self):
        print("SCORE_UP")

# 필살기 업
class SUPER_POWER_UP(item):
    def __init__(self):
        self.icon = pygame.image.load('image/SUPER_POWER_UP.png')

    def print_item(self):
        print("SUPER_POWER_UP")





hp_item = HP_UP()
hp_item.print_item()

