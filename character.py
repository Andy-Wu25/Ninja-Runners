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
        self.rect.x += dx 
        self.rect.y += dy

    def update(self):
        self.animation()  
        self.check_alive()
        if self.throw_cooldown > 0:
            self.throw_cooldown -= 1
            
    # Animation method
    def animation(self):
        ANIMATION_TIMER = 50 
        self.img = self.animation_list[self.current_action][self.index]
        if pygame.time.get_ticks() - self.animation_time > ANIMATION_TIMER:
            self.animation_time = pygame.time.get_ticks()
            self.index += 1
            if self.index >= len(self.animation_list[self.current_action]):
                if self.current_action == 4:
                    self.index = len(
                        self.animation_list[self.current_action]) - 1
                elif self.current_action == 3:
                    self.index = 0
                    global throw_completed
                    throw_completed = True
                else:
                    self.index = 0 

    # Changing player action method
    def new_action(self, different_action):
        if different_action != self.current_action:  
            self.current_action = different_action
            self.animation_time = pygame.time.get_ticks()
            self.index = 0

    # Throw method
    def throw(self):
        if player.number_weapon > 0 and self.throw_cooldown == 0:
            self.throw_cooldown = 50
            weapon = Weapon(self.rect.centerx + (90 * self.direction),
                            self.rect.centery + 30, self.direction) # Create new Weapon instance
            weapon_group.add(weapon)
            player.number_weapon -= 1

    # Check alive method
    def check_alive(self):
        if self.health <= 0: 
            self.health = 0  
            self.alive = False  
            self.new_action(4)

    # Draw method
    def draw(self):
        screen.blit(pygame.transform.flip(
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
