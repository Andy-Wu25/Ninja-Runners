# Character class
class Character(pygame.sprite.Sprite):
    def __init__(self, character_type, x, y, scale, speed, number_weapon, health):
        pygame.sprite.Sprite.__init__(self)
        self.alive = True
        self.character_type = character_type
        self.animation_list = []
        # Index of the animation list
        self.index = 0
        self.animation_time = pygame.time.get_ticks()
        self.current_action = 0
        self.jump = False
        self.velocity_y = 0
        self.in_air = True

        # Idle animation list
        idle_list = []
        for i in range(10):
            image = pygame.image.load(
                f"NEA_image/{self.character_type}/Idle/{i}.png")
            image = pygame.transform.scale(
                image, (int(image.get_width() * scale), int(image.get_height() * scale)))
            idle_list.append(image)
        self.animation_list.append(idle_list)  # Index 0 in animation_list

        # Run animation list
        run_list = []
        for i in range(10):
            image = pygame.image.load(
                f"NEA_image/{self.character_type}/Run/{i}.png")
            image = pygame.transform.scale(
                image, (int(image.get_width() * scale), int(image.get_height() * scale)))
            run_list.append(image)
        self.animation_list.append(run_list)  # Index 1 in animation_list

        # Jump animation list
        jump_list = []
        for i in range(10):
            image = pygame.image.load(
                f"NEA_image/{self.character_type}/Jump/{i}.png")
            image = pygame.transform.scale(
                image, (int(image.get_width() * scale), int(image.get_height() * scale)))
            jump_list.append(image)
        self.animation_list.append(jump_list)  # Index 2 in animation list

        # Throw animation list
        throw_list = []
        for i in range(10):
            image = pygame.image.load(
                f"NEA_image/{self.character_type}/Throw/{i}.png")
            image = pygame.transform.scale(
                image, (int(image.get_width() * scale), int(image.get_height() * scale)))
            throw_list.append(image)
        self.animation_list.append(throw_list)  # Index 3 in animation list

        # Death animation list
        death_list = []
        for i in range(10):
            image = pygame.image.load(
                f"NEA_image/{self.character_type}/Death/{i}.png")
            image = pygame.transform.scale(
                image, (int(image.get_width() * scale), int(image.get_height() * scale)))
            death_list.append(image)
        self.animation_list.append(death_list)  # Index 4 in animation list

        self.img = self.animation_list[self.current_action][self.index]

        self.rect = self.img.get_rect()

        self.rect.center = (x, y)

        self.speed = speed

        self.direction = 1  

        self.flip = False

        self.throw_cooldown = 0


        self.number_weapon = number_weapon

        self.health = health

        self.maximum_health = self.health

    # Move method

    def move(self, move_left, move_right):

        dx = 0 
        dy = 0

        # Movement variables
        if move_left:
            dx = -self.speed  
            self.flip = True 
            self.direction = -1 

        # Move right
        if move_right:
            dx = self.speed  
            self.flip = False  
            self.direction = 1  # 1 represents facing right

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
        self.rect.x += dx  # Rectangle's x-coordinate will increase by dx
        self.rect.y += dy  # Rectangle's y-coordinate will increase by dy

    # Update method, handles all the animations and cooldowns

    def update(self):
        self.animation()  # Call the animation method
        # Call the alive method to load the death animation if the instance has died
        self.check_alive()
        # Update throw cooldown
        if self.throw_cooldown > 0:
            self.throw_cooldown -= 1

    # Animation method

    def animation(self):
        ANIMATION_TIMER = 50  # Animation timer to keep track of when to load the next image
        # Change the animation image depending on the current action of the player
        self.img = self.animation_list[self.current_action][self.index]
        # Check the time passed to go onto the next animation image
        # Current time - last update time > ANIMTION_TIMER
        if pygame.time.get_ticks() - self.animation_time > ANIMATION_TIMER:
            # Reset the animation_time to the current time, resetting the timer
            self.animation_time = pygame.time.get_ticks()
            # Move onto the next index of the animation list, loading the next animation image
            self.index += 1
            # Check the current index against the total number of images in the current action list
            # If current action is 0 (idle), it will check the length of the list in index 0 of the animation list

            # Check if the index is greater than or equal to the total number of images in the current action list
            # This means that it has reached the end of the action animation
            if self.index >= len(self.animation_list[self.current_action]):
                # Check if the current action is 4, which is the death animation
                if self.current_action == 4:
                    # Make the index remain at the length of the death animation list - 1, which will be the last index of the list
                    self.index = len(
                        self.animation_list[self.current_action]) - 1

                # Check if  the current action value is 3, which is the throw animation
                elif self.current_action == 3:
                    self.index = 0

                    global throw_completed
                    throw_completed = True  # The throw animation has completed
                else:
                    self.index = 0  # Reset all other animation index back to 0 so that it repeats through the animation images again

    # Changing player action method

    def new_action(self, different_action):
        if different_action != self.current_action:  # Check if current action is equal to new action
            # Set the current action to different_action if they are not the same
            self.current_action = different_action

            # Set the animation to current time so that it can be used to keep track of how much time has passed
            self.animation_time = pygame.time.get_ticks()
            # Reset index variable so that when there is a change in animation, it starts at index 0 again
            self.index = 0

    # Throw method

    def throw(self):
        # Check that the player has not run out of weapons to throw
        if player.number_weapon > 0 and self.throw_cooldown == 0:
            # Create a instance of the Weapon class
            self.throw_cooldown = 50
            weapon = Weapon(self.rect.centerx + (90 * self.direction),
                            self.rect.centery + 30, self.direction)
        # Add the instance to the sprite group
            weapon_group.add(weapon)
            # Reduce number of weapons by 1 everytime the player presses the spacebar
            player.number_weapon -= 1

    # Check alive method

    def check_alive(self):
        if self.health <= 0:  # Check if the health of the instance is below or equal to 0
            self.health = 0  # Set health to 0 so it is not negative
            self.alive = False  # The instance has died due to the health being <= 0
            # Set the different_action value to 4, causing the animation to change to index 4 of animation_list, which is the death animation
            self.new_action(4)

    # Draw method

    def draw(self):
        screen.blit(pygame.transform.flip(
            self.img, self.flip, False), self.rect)
        #pygame.draw.rect(screen, RED, self.rect, 1)
    
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
