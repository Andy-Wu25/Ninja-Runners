import pygame
pygame.init()

class Character(pygame.sprite.Sprite):
    def __init__(self, character_type, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.character_type = character_type
        image = pygame.image.load(
            f"NEA_image/{self.character_type}/Idle/0.png")
        self.img = pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale)))
        self.rect = self.img.get_rect()
        self.rect.center = (x, y)
        self.speed = speed
        self.direction = 1  
        self.flip = False 

    # Move method
    def move(self, move_left, move_right):
        dx = 0  
        dy = 0  

        if move_left:
            dx = -self.speed  
            self.flip = True 
            self.direction = -1 

        if move_right:
            dx = self.speed  
            self.flip = False  
            self.direction = 1

        # Change the player's rectangle position
        self.rect.x += dx 
        self.rect.y += dy  

    # Draw method
    def draw(self):
        screen.blit(pygame.transform.flip(
            self.img, self.flip, False), self.rect)