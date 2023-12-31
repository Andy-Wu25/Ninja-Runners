import pygame 
import character
import background
from pygame.constants import DROPTEXT
pygame.init()

# Game variables
clock = pygame.time.Clock()
FPS = 60
scale = 0.15
run = True 

# Game window
SCREEN_WIDTH = 1000  
SCREEN_HEIGHT = 800  
screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_HEIGHT))
pygame.display.set_caption("Shooter Game")

# Player and enemy instance
player = character.Character(100, 200, 0.15)
enemy = character.Character("enemy", 200, 200, 0.175, 3)

while run: 
    clock.tick(FPS)  
    background.draw_background()  
    player.draw() 
    enemy.draw()
    player.player_action()
    player.move(move_left, move_right)  

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            run = False  
        # Key presses
        if event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_w and player.alive:
                player.jump = True
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
