# Item boxes
import pygame
import main

class ItemBox(pygame.sprite.Sprite):
    def __init__(self, item_type, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.item_type = item_type  # Determines which images in the item box folder to access
        # The index will represent the image being stored
        self.image = item_boxes[self.item_type]
        self.rect = self.image.get_rect()  # Create a rectangle around the item box
        self.rect.midtop = (x + TILE_SIZE // 2, y +
                            (TILE_SIZE - self.image.get_height()))

    def update(self):
        # Check collision between item box rectangle and player rectangle
        if pygame.sprite.collide_rect(self, player):
            # Check item box type using the item_type variable
            if self.item_type == "Health":  # Increase health
                player.health += 25

                if player.health > player.maximum_health:  # Check if the health has exceeded maximum health
                    # Make player health equal to maximum health
                    player.health = player.maximum_health

            elif self.item_type == "Weapon":  # increase weapons
                player.number_weapon += 1

            # Delete the item box when there is a collision
            self.kill()