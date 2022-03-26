#imports pygame
from termios import VEOL # initializes velocity actions
import pygame # initializes pygame
import os #initializes system
pygame.font.init() # initializes font
pygame.mixer.init() # initializes sound

#creates window sets width and height
#convention is to capitalize constant values
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# changes name
pygame.display.set_caption("Galaga")

#colors for use in game
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

#creates borders for players to contain them within certain coordinates 
BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

#brings in sound files
BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Grenade+1.mp3'))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Gun+Silencer.mp3'))
#creates health bar
HEALTH_FONT =  pygame.font.SysFont('comicsans', 40)

#creates winner text
WINNER_FONT = pygame.font.SysFont('comicsans', 100)
# FPS sets a universal speed across machines, this needs to be set because if not your machine could run it hundreds of times if not thousands per second, which isnt necessary
FPS = 60

# Sets bullet velocity, and max value
BULLET_VEL = 7
MAX_BULLETS = 5

# sets spaceship dimensions to be called in
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

# Represents the code for custom user events, allowing each to have individual events
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2


#Creates 2 player images aka surfaces
#resizes and rotates image to proper dimensions using transform
YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)


RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))


# Allows images to be drawn on the screen
def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
        #draws in border to window, takes in black as color, and border as shape and size
     WIN.blit(SPACE, (0, 0))
     pygame.draw.rect(WIN, BLACK, BORDER)
    #blit allows you to draw surfaces onto screen must be called after fill or the layers will be wrong

    #draws in health bars
     red_health_text = HEALTH_FONT.render("Health: " + str(red_health), 1, WHITE)
     yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow_health), 1, WHITE)
     WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
     WIN.blit(yellow_health_text, (10, 10))

     #draws in spaceships
     WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
     WIN.blit(RED_SPACESHIP, (red.x, red.y))
    
    #draws yellow and red bullets
     for bullet in red_bullets:
         pygame.draw.rect(WIN, RED, bullet)

     for bullet in yellow_bullets:
         pygame.draw.rect(WIN, YELLOW, bullet)
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


#defines bullet moves bullet, handles collision of bullet, and handles removing bullets when they go off screen or hit a character
def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    # yellow player hit
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)
    # red player hit
    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)


#defines winner and draws on surface
def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

#defines main function loop of game checks for collisions, updates score, redrawing window
# main game takes in functions built separetly all the action is happening here
def main():

    # defines player positions and allows movement
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    #defines bullets
    red_bullets = []
    yellow_bullets = []

    #defines health points
    red_health = 10
    yellow_health = 10

    #clock controls speed of the while loop in this case 60
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
   

        #creates bullets on key press
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 -2, 10, 5)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height//2 -2, 10, 5)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
            #controls player hits
            if event.type == RED_HIT:
                red_health -= 1

            if event.type == YELLOW_HIT:
                yellow_health -= 1

        # conditional to determine winner and generate text
        winner_text = ""        
        if red_health <= -1:
            winner_text = "Yellow Wins"
            BULLET_HIT_SOUND.play()
            
        if yellow_health <= -1:
            winner_text = "Red Wins"
            BULLET_HIT_SOUND.play()

        if winner_text != "":
            draw_winner(winner_text)
            break


        #runs key press function
        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)

        #moves bullets and checks to see if a hit was confirmed
        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        #draws bullets and health bars
        draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)
       

    main()


if __name__ == "__main__":
    main()

