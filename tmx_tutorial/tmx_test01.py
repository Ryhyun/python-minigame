import sys
import os
import pygame
import pytmx


## https://www.mapeditor.org/
pygame.init()
display = pygame.display.set_mode((800, 800))
pygame.display.set_caption("tmx file load")

tmx_data = pytmx.load_pygame("/Users/Choichanghyun/Desktop/test02.tmx")

clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    display.fill((255,255,255))

    for layer in tmx_data.visible_layers:
        for x, y, gid, in layer:
            tile = tmx_data.get_tile_image_by_gid(gid)
            if tile:
                display.blit(tile, (x * tmx_data.tilewidth, y * tmx_data.tileheight))

    pygame.display.update()
    clock.tick(60)
