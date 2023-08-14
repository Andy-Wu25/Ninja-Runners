# Character class
import pygame
pygame.init()

class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)

        image = pygame.image.load("NEA_image/player/Idle/0.png")
        self.img = pygame.transform.scale(
            image, (int(image.get_width() * scale), int(image.get_height() * scale)))
        self.rect = self.img.get_rect()
        self.rect.center = (x, y)

    # Display function
    def draw(self):
        screen.blit(self.img, self.rect)