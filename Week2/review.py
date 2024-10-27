#I am creating a small adventure game

import pygame

#Dimentions of the screens
screen = pygame.display.set_mode((600, 400))

#Title of the app
pygame.display.set_caption('Mini Adventure')

#Choosing the background color and filling the screen with it
background_color = (255, 255, 255)
screen.fill(background_color)

pygame.display.flip()

#Drawing the roads/paths using lines
#Left Road
pygame.draw.line(screen, "black", (1, 1), (200, 200))
pygame.draw.line(screen, "black", (90, 1), (250, 150))
#Middle Road



#Right Road

#Drawing the player
pygame.draw.circle(screen, "black", (300, 250), 10)

pygame.display.flip()

running = True

# game loop
while running:

    # for loop through the event queue
    for event in pygame.event.get():

        # Check for QUIT event
        if event.type == pygame.QUIT:
            running = False


#Limiting FPS to 30
pygame.time.Clock().tick(30)

#pygame.display.flip()
