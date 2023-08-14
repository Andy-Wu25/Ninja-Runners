# Character class
import pygame
pygame.init()

class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        # Call the parent class (sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Instance variable
        # Load image into pygame
        image = pygame.image.load("NEA_image/player/Idle/0.png")
        # Scales the image down to a small image
        self.img = pygame.transform.scale(
            image, (int(image.get_width() * scale), int(image.get_height() * scale)))
        # Create a rectangle
        self.rect = self.img.get_rect()
        # Center of the rectangle will be set to the x and y values above
        self.rect.center = (x, y)

    def draw(self):
        screen.blit(self.img, self.rect)  # Displays it onto the screen