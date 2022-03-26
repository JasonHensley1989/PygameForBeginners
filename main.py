#imports pygame
from termios import VEOL
import pygame
import os


#creates window sets width and height
#convention is to capitalize constant values
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# changes name
pygame.display.set_caption("Galaga")

#colors for use in game
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#creates borders for players to contain them within certain coordinates 
BORDER = pygame.Rect(WIDTH/2 - 5, 0, 10, HEIGHT)

# FPS sets a universal speed across machines, this needs to be set because if not your machine could run it hundreds of times if not thousands per second, which isnt necessary
FPS = 60
# Sets bullet velocity, and max value
BULLET_VEL = 7
MAX_BULLETS = 5
# sets spaceship dimensions to be called in
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40



#Creates 2 player images aka surfaces
#resizes and rotates image to proper dimensions using transform
YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)


RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)


# Allows images to be drawn on the screen
def draw_window(red, yellow):
    # calls in backround color
     WIN.fill(WHITE)
     #draws in border to window, takes in black as color, and border as shape and size
     pygame.draw.rect(WIN, BLACK, BORDER)
    #blit allows you to draw surfaces onto screen must be called after fill or the layers will be wrong
     WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
     WIN.blit(RED_SPACESHIP, (red.x, red.y))
    #updates game so loop continues and allows color on screen to be changed to white
     pygame.display.update()


#defines movement for yellow player and statments control player from going outside of border
def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEOL > 0: #left key registered as a defines move left
        yellow.x -=  VEOL
    if keys_pressed[pygame.K_d] and yellow.x + VEOL + yellow.width < BORDER.x: #left key registered as d defines move right
        yellow.x +=  VEOL
    if keys_pressed[pygame.K_w] and yellow.y - VEOL > 0: #left key registered as w defines move up
        yellow.y -=  VEOL
    if keys_pressed[pygame.K_s] and yellow.y + VEOL + yellow.height < HEIGHT - 15: #left key registered as s defines move down
        yellow.y +=  VEOL

#defines movement for red player
def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEOL > BORDER.x + BORDER.width: #left key registered left arrow
        red.x -=  VEOL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEOL + red.width < WIDTH: #left key registered right arrow
        red.x +=  VEOL
    if keys_pressed[pygame.K_UP] and red.y - VEOL > 0: #left key registered up arrow
        red.y -=  VEOL
    if keys_pressed[pygame.K_DOWN] and red.y + VEOL + red.height < HEIGHT - 15: #left key registered down arrow
        red.y +=  VEOL

#defines main function loop of game checks for collisions, updates score, redrawing window
# main game takes in functions built separetly all the action is happening here
def main():

    # defines player positions and allows movement
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    #defines bullets
    red_bullets = []
    yellow_bullets = []

    #clock controls speed of the while loop in this case 60
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
   

        #creates bullets on key press
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height/2 -2, 10, 5)
                    yellow_bullets.append(bullet)


                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height/2 -2, 10, 5)
                    red_bullets.append(bullet)
                    
        #runs key press function
        print(red_bullets, yellow_bullets)
        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        draw_window(red, yellow)
       

    pygame.quit()


if __name__ == "__main__":
    main()

