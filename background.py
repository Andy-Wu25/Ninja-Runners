import main
import pygame

BROWN = (165, 42, 42)
BLACK = (0, 0, 0)

def draw_background():
    main.screen.fill(BROWN)
    pygame.draw.line(main.screen, BLACK, (0, 400), (main.SCREEN_WIDTH, 400))