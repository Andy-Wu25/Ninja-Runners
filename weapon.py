import pygame
import main

# Load weapon image
weapon_image = pygame.image.load("NEA_image/weapon.png")
weapon_image = pygame.transform.scale(weapon_image, (int(
    weapon_image.get_width() * 0.4), int(weapon_image.get_height() * 0.4)))
weapon_image = pygame.transform.rotate(weapon_image, -90)

class Weapon(pygame.sprite.Sprite):
    def __init__(self, x, y, direction): 
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.flip(weapon_image, main.player.flip, False)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction  
        self.change_pixel = 5  

    # Weapon movement
    def update(self):
        self.rect.x += (self.direction * self.change_pixel)

        if self.rect.x > main.SCREEN_WIDTH or self.rect.x < 0:
            self.kill()

        # Check collision with instances
        # Collision between player and weapon
        if pygame.sprite.spritecollide(main.player, main.weapon_group, False):
            if main.player.alive: 
                self.kill()  
                main.player.health -= 50  

        # Collision between enemy and weapon
        if pygame.sprite.spritecollide(main.enemy, main.weapon_group, False):
            if main.enemy.alive:  
                self.kill()
                main.enemy.health -= 50 
                print(main.enemy.health)
