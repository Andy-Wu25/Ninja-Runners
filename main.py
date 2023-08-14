import pygame 
import character

pygame.init()

SCREEN_WIDTH = 1000  
SCREEN_HEIGHT = 800  

# Game window
screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_HEIGHT))

# Game window title
pygame.display.set_caption("Shooter Game")

player = character.Character(100, 200, 0.15)

# Starting position of character
x = 100
y = 200

scale = 0.15
run = True  
while run:  
    player.draw()

    # Event handler
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            run = False  

    pygame.display.update() 

pygame.quit()