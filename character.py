import pygame
import main

GRAVITY = 0.5
move_left = False
move_right = False

class Character(pygame.sprite.Sprite):
    def __init__(self, character_type, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.alive = True
        self.character_type = character_type
        self.animation_list = []
        self.index = 0
        self.animation_time = pygame.time.get_ticks()
        self.current_action = 0
        self.jump = False
        self.velocity_y = 0
        self.in_air = True

        idle_list = []

        # Iterate through the different images
        for i in range(10):
            image = pygame.image.load(
                f"images/{self.character_type}/Idle/{i}.png")
            image = pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale)))
            idle_list.append(image)
        self.animation_list.append(idle_list) 

        run_list = []
        for i in range(10):
            image = pygame.image.load(
                f"images/{self.character_type}/Run/{i}.png")
            image = pygame.transform.scale(
                image, (int(image.get_width() * scale), int(image.get_height() * scale)))
            run_list.append(image)
        self.animation_list.append(run_list)  

        jump_list = []
        for i in range(10):
            image = pygame.image.load(
                f"images/{self.character_type}/Jump/{i}.png")
            image = pygame.transform.scale(
                image, (int(image.get_width() * scale), int(image.get_height() * scale)))
            jump_list.append(image)
        self.animation_list.append(jump_list)  

        self.img = self.animation_list[self.current_action][self.index]
        self.rect = self.img.get_rect()
        self.rect.center = (x, y)
        self.speed = speed
        self.direction = 1 
        self.flip = False

    # Move method
    def move(self, move_left, move_right):
        dx = 0  
        dy = 0  
        
        # Move left
        if move_left:
            dx = -self.speed  
            self.flip = True  
            self.direction = -1 

        # Move right
        if move_right:
            dx = self.speed  
            self.flip = False  
            self.direction = 1 

        # Jump
        if self.jump == True and self.in_air == False:
            self.velocity_y = -11
            self.jump = False
            self.in_air = True

        # Gravity
        self.velocity_y += GRAVITY
        dy += self.velocity_y

        # Collision check with floor
        if self.rect.bottom + dy > 400:
            dy = 400 - self.rect.bottom
            self.in_air = False

        # Change the player's rectangle position
        self.rect.x += dx  
        self.rect.y += dy  

    # Animation method
    def animation(self):
        ANIMATION_TIMER = 50  # Animation timer 
        self.img = self.animation_list[self.current_action][self.index]

        # Check the time to move onto the next image
        if pygame.time.get_ticks() - self.animation_time > ANIMATION_TIMER:
            self.animation_time = pygame.time.get_ticks()
            self.index += 1
        
            if self.index >= len(self.animation_list[self.current_action]):
                self.index = 0

    # Changing player action method
    def new_action(self, different_action):
        if different_action != self.current_action:  
            self.current_action = different_action
            self.animation_time = pygame.time.get_ticks()
            self.index = 0

    # Draw method
    def draw(self):
        main.screen.blit(pygame.transform.flip(
            self.img, self.flip, False), self.rect)
    
    # Player action animations
    def player_actions(self):
        if self.alive:
            if (move_left and self.in_air) or (move_right and self.in_air):
                self.new_action(2)
            elif self.in_air:  
                self.new_action(2)  
            elif move_left or move_right:  
                self.new_action(1)  
            else:
                self.new_action(0)
