import pygame
from map import Wall,Block,setupRoomOne,setupGate
from player import Player
from ghost  import Ghost


black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
purple = (255, 0, 255)
yellow = (255, 255, 0)

Trollicon = pygame.image.load('images/pacman_l.png')
pygame.display.set_icon(Trollicon)

# Add music
pygame.mixer.init()
#pygame.mixer.music.load('pacman.mp3')
#pygame.mixer.music.play(-1, 0.0)



# Call this function so the Pygame library can initialize itself
pygame.init()

# Create an 606x606 sized screen
screen = pygame.display.set_mode([700, 700])

# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'RenderPlain.'


# Set the title of the window
pygame.display.set_caption('Pacman')

# Create a surface we can draw on
background = pygame.Surface(screen.get_size())

# Used for converting color maps and such
background = background.convert()

# Fill the screen with a black background
background.fill(black)

clock = pygame.time.Clock()

pygame.font.init()
font = pygame.font.Font("freesansbold.ttf", 24)

# default locations for Pacman and monstas
w = 303 - 16  # Width
p_h = (7 * 60) + 19  # Pacman height
m_h = (4 * 60) + 19  # Monster height
b_h = (3 * 60) + 19  # Binky height
i_w = 303 - 16 - 32  # Inky width
c_w = 303 + (32 - 16)  # Clyde width

Pinky_directions = [
[0,-30,4],
[15,0,9],
[0,15,11],
[-15,0,23],
[0,15,7],
[15,0,3],
[0,-15,3],
[15,0,19],
[0,15,3],
[15,0,3],
[0,15,3],
[15,0,3],
[0,-15,15],
[-15,0,7],
[0,15,3],
[-15,0,19],
[0,-15,11],
[15,0,9]
]
pl = len(Pinky_directions) - 1

def startGame():
    all_sprites_list = pygame.sprite.RenderPlain()

    block_list = pygame.sprite.RenderPlain()

    monsta_list = pygame.sprite.RenderPlain()

    pacman_collide = pygame.sprite.RenderPlain()

    wall_list = setupRoomOne(all_sprites_list)

    gate = setupGate(all_sprites_list)

    p_turn = 0
    p_steps = 0

    b_turn = 0
    b_steps = 0

    i_turn = 0
    i_steps = 0

    c_turn = 0
    c_steps = 0


    # Draw the grid
    for row in range(19):
        for column in range(19):
            if (row == 7 or row == 8) and (column == 8 or column == 9 or column == 10):
                continue
            else:
                block = Block(yellow, 4, 4)

                # Set a random location for the block
                block.rect.x = (30 * column + 6) + 26
                block.rect.y = (30 * row + 6) + 26

                b_collide = pygame.sprite.spritecollide(block, wall_list, False)
                p_collide = pygame.sprite.spritecollide(block, pacman_collide, False)
                if b_collide:
                    continue
                elif p_collide:
                    continue
                else:
                    # Add the block to the list of objects
                    block_list.add(block)
                    all_sprites_list.add(block)

    bll = len(block_list)

    score = 0

    done = False

    i = 0
    Pacman = Player(w, p_h, "images/pacman_l.png")
    all_sprites_list.add(Pacman)
    pacman_collide.add(Pacman)


    Blinky = Ghost(w, b_h, "images/Blinky.png")
    monsta_list.add(Blinky)
    all_sprites_list.add(Blinky)

    Pinky = Ghost(w, m_h, "images/Pinky.png")
    monsta_list.add(Pinky)
    all_sprites_list.add(Pinky)

    Inky = Ghost(i_w, m_h, "images/Inky.png")
    monsta_list.add(Inky)
    all_sprites_list.add(Inky)

    Clyde = Ghost(c_w, m_h, "images/Clyde.png")
    monsta_list.add(Clyde)
    all_sprites_list.add(Clyde)

    while done == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    Pacman.changespeed(-30, 0)
                    Pacman.changeIcon("images/pacman_l.png")
                if event.key == pygame.K_RIGHT:
                    Pacman.changespeed(30, 0)
                    Pacman.changeIcon("images/pacman_R.png")
                if event.key == pygame.K_UP:
                    Pacman.changespeed(0, -30)
                    Pacman.changeIcon("images/pacman_u.png")
                if event.key == pygame.K_DOWN:
                    Pacman.changespeed(0, 30)
                    Pacman.changeIcon("images/pacman_d.png")

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    Pacman.changespeed(30, 0)
                if event.key == pygame.K_RIGHT:
                    Pacman.changespeed(-30, 0)
                if event.key == pygame.K_UP:
                    Pacman.changespeed(0, 30)
                if event.key == pygame.K_DOWN:
                    Pacman.changespeed(0, -30)


        if(  Pacman.rect.left <= 0  and Pacman.rect.top >= 460 and Pacman.rect.top <= 510 ):
            Pacman.rect.left = 590
            Pacman.rect.top = 110

        elif(  Pacman.rect.left >= 600  and Pacman.rect.top >= 100 and Pacman.rect.top <= 150 ):
            Pacman.rect.left = 15
            Pacman.rect.top = 470

        if (Pacman.rect.left <= 0 and Pacman.rect.top >= 100 and Pacman.rect.top <= 150):
            Pacman.rect.left = 590
            Pacman.rect.top = 470

        elif (Pacman.rect.left >= 600 and Pacman.rect.top >= 460 and Pacman.rect.top <= 510):
            Pacman.rect.left = 15
            Pacman.rect.top = 110

        returned = Pinky.changeRandom( False, p_turn, p_steps,Pacman.rect.left, Pacman.rect.top)
        p_turn = returned[0]
        p_steps = returned[1]
        #Pinky.changeRandom( False, p_turn, p_steps, Pacman.rect.left, Pacman.rect.top)
        Pinky.update(wall_list, False)


        returned = Blinky.changeRandom( False, b_turn, b_steps,Pacman.rect.left, Pacman.rect.top)
        b_turn = returned[0]
        b_steps = returned[1]
        #Blinky.changeRandom( False, b_turn, b_steps,Pacman.rect.left, Pacman.rect.top)
        Blinky.update(wall_list, False)

        returned = Inky.changeRandom( False, i_turn, i_steps,Pacman.rect.left, Pacman.rect.top)
        i_turn = returned[0]
        i_steps = returned[1]
        #Inky.changeRandom( False, i_turn, i_steps,Pacman.rect.left, Pacman.rect.top)
        Inky.update(wall_list, False)

        returned = Clyde.changeRandom( "clyde", c_turn, c_steps,Pacman.rect.left, Pacman.rect.top)
        c_turn = returned[0]
        c_steps = returned[1]
        #Clyde.changeRandom( "clyde", c_turn, c_steps,Pacman.rect.left, Pacman.rect.top)
        Clyde.update(wall_list, False)

        # See if the Pacman block has collided with anything.
        blocks_hit_list = pygame.sprite.spritecollide(Pacman, block_list, True)
        if len(blocks_hit_list) > 0:
            score += len(blocks_hit_list)
        Pacman.update(wall_list, gate)

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        screen.fill(black)

        wall_list.draw(screen)
        gate.draw(screen)
        all_sprites_list.draw(screen)
        monsta_list.draw(screen)

        text = font.render("Score: " + str(score) + "/" + str(bll), True, red)
        screen.blit(text, [10, 10])

        if score == bll:
            doNext("Congratulations, you won!", 145, all_sprites_list, block_list, monsta_list, pacman_collide,
                   wall_list, gate)

        monsta_hit_list = pygame.sprite.spritecollide(Pacman, monsta_list, False)

        if monsta_hit_list:
            doNext("Game Over", 235, all_sprites_list, block_list, monsta_list, pacman_collide, wall_list, gate)

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        pygame.display.flip()

        clock.tick(10)


def doNext(message, left, all_sprites_list, block_list, monsta_list, pacman_collide, wall_list, gate):
    while True:
        # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.key == pygame.K_RETURN:
                    del all_sprites_list
                    del block_list
                    del monsta_list
                    del pacman_collide
                    del wall_list
                    del gate
                    startGame()

        # Grey background
        w = pygame.Surface((400, 200))  # the size of your rect
        w.set_alpha(10)  # alpha level
        w.fill((128, 128, 128))  # this fills the entire surface
        screen.blit(w, (100, 200))  # (0,0) are the top-left coordinates

        # Won or lost
        text1 = font.render(message, True, white)
        screen.blit(text1, [left, 233])

        text2 = font.render("To play again, press ENTER.", True, white)
        screen.blit(text2, [135, 303])
        text3 = font.render("To quit, press ESCAPE.", True, white)
        screen.blit(text3, [165, 333])

        pygame.display.flip()

        clock.tick(10)


startGame()

pygame.quit()