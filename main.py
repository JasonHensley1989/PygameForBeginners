#imports pygame
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
# FPS sets a universal speed across machines, this needs to be set because if not your machine could run it hundreds of times if not thousands per second, which isnt necessary
FPS = 60




def draw_window():
     WIN.fill(WHITE)
        #updates game so loop continues and allows color on screen to be changed to white
     pygame.display.update()

#defines main function loop of game checks for collisions, updates score, redrawing window
# main game takes in functions built separetly all the action is happening here
def main():
    #clock controls speed of the while loop in this case 60
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        ##calls in draw function
        draw_window()
       

    pygame.quit()


if __name__ == "__main__":
    main()

