import pygame 
import character
from pygame.constants import DROPTEXT

pygame.init()
clock = pygame.time.Clock()
FPS = 60  

# Game window
SCREEN_WIDTH = 1000  
SCREEN_HEIGHT = 800  
screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_HEIGHT))
pygame.display.set_caption("Shooter Game")

# Background
BROWN = (165, 42, 42)
def draw_background():
    screen.fill(BROWN)

# Player and enemy instance
player = character.Character(100, 200, 0.15)
enemy = character.Character("enemy", 200, 200, 0.175, 3)

scale = 0.15
run = True  
while run: 
    clock.tick(FPS)  
    draw_background()  
    player.draw() 
    enemy.draw()
    player.move(move_left, move_right) 

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            run = False  

        # Key presses
        if event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_a:  
                move_left = True
            if event.key == pygame.K_d:  
                move_right = True

            if event.key == pygame.K_ESCAPE:
                run = False

        # Key releases
        if event.type == pygame.KEYUP:  
            if event.key == pygame.K_a:
                move_left = False
            if event.key == pygame.K_d:
                move_right = False

    pygame.display.update()  

pygame.quit()