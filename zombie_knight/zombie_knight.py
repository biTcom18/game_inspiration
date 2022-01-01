import pygame, random
# Use 2D vectors

vector = pygame.math.Vector2

# Initialize pygame
pygame.init()

# Set display surface (tile size is 32x32 so 1280/32 = 40 tiles wide, 736/32 = 23 tiles height)
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 736
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Zombie Knight")

# Set FPS  and clock
FPS = 30
clock = pygame.time.Clock()

# Define classes
class Game():
    """ A class to help manage gameplay """
    
    def __init__(self):
        """ Initialize the game """
        # Set constant variables
        self.STARTING_ROUND_TIME = 30
        
        # Set game values
        self.score = 0
        self.round_number = 1
        self.frame_count = 0
        self.round_time = self.STARTING_ROUND_TIME
        
        # Set fonts
        self.title_font = pygame.font.Font("zombie_knight/fonts/Poultrygeist.ttf", 48)
        self.HUD_font = pygame.font.Font("zombie_knight/fonts/Pixel.ttf", 24)
    
    def update(self):
        """ Update the game """ 
        # Update the round time every second
        self.frame_count += 1
        if self.frame_count % FPS == 0:
            self.round_time -= 1
            self.frame_count = 0
    
    def draw(self):
        """ Draw the game HUD """    
        # Set colors
        WHITE = (255, 255, 255)
        GREEN = (25, 200, 25)
        
        # Set text
        score_text = self.HUD_font.render("Score: " + str(self.score), True, WHITE)
        score_rect = score_text.get_rect()
        score_rect.topleft = (10, WINDOW_HEIGHT - 50)
        
        
        health_text = self.HUD_font.render("Health: " + str(100), True, WHITE)
        health_rect = health_text.get_rect()
        health_rect.topleft = (10, WINDOW_HEIGHT - 25)
        
        title_text = self.title_font.render("Zombie Knight", True, GREEN)
        title_rect = title_text.get_rect()
        title_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT - 25)
        
        round_text = self.HUD_font.render("Night: " + str(self.round_number), True, WHITE)
        round_rect = round_text.get_rect()
        round_rect.topright = (WINDOW_WIDTH - 10, WINDOW_HEIGHT - 50)
        
        time_text = self.HUD_font.render("Sunrise In: " + str(self.round_time), True, WHITE)
        time_rect = time_text.get_rect()
        time_rect.topright = (WINDOW_WIDTH - 10, WINDOW_HEIGHT - 25)
        
        # Draw the HUD
        display_surface.blit(score_text, score_rect)
        display_surface.blit(health_text, health_rect)
        display_surface.blit(title_text, title_rect)
        display_surface.blit(round_text, round_rect)
        display_surface.blit(time_text, time_rect)

        
        
    def add_zombie(self):
        """ Add a zombie to the game """
        pass
    
    def check_collisions(self):
        """ Check collisions that affect gameplay """
        pass
    
    def check_round_completion(self):
        """ Check if the player survived a single night """
        pass
    
    def check_game_over(self):
        """ Check to see if the player lost the game """
        pass
    
    def start_new_round(self):
        """ Start a new night """
        pass
    
    def pause_game(self):
        """ Pause the game """
        pass
    
    def reset_game(self):
        """ Reset the game """
        pass
    
    
class Tile(pygame.sprite.Sprite):
    """ A class to represent 32x32 pixel area in our display """
    
    def __init__(self, x, y, image_int, main_group, sub_group = ""):
        """ Initialize the tile """    
        super().__init__()
        # Load in the correct image and add it to the correct sub group
        # Dirt tiles
        if image_int == 1:
            self.image = pygame.transform.scale(pygame.image.load("zombie_knight/images/tiles/Tile_1.png"), (32,32))
        # Platform tiles
        elif image_int == 2:
            self.image = pygame.transform.scale(pygame.image.load("zombie_knight/images/tiles/Tile_2.png"), (32,32))
            sub_group.add(self)
        elif image_int == 3:
            self.image = pygame.transform.scale(pygame.image.load("zombie_knight/images/tiles/Tile_3.png"), (32,32))
            sub_group.add(self)
        elif image_int == 4:
            self.image = pygame.transform.scale(pygame.image.load("zombie_knight/images/tiles/Tile_4.png"), (32,32))
            sub_group.add(self)
        elif image_int == 5:
            self.image = pygame.transform.scale(pygame.image.load("zombie_knight/images/tiles/Tile_5.png"), (32,32))
            sub_group.add(self)
                                
        # Add every tile to the main group
        main_group.add(self)
        
        # Get the rect of the image and position within the grid
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)                                
            
    
class Player(pygame.sprite.Sprite):
    """ A class the user can control """
    
    def __init__(self, x, y, platform_group, portal_group, bullet_group):
        """ Initialize the player """
        super().__init__()
        
        # Set constant variables
        self.HORISONTAL_ACCELERATION = 2
        self.HORISONTAL_FRICTION = 0.15
        self.VERTICAL_ACCELERATION = 0.8 #Gravity
        self.VERTICAL_JUMP_SPEED = 18 #Determines how high the player can jump
        self.STARTING_HEALTH = 100
        
        # Animation frames
        self.move_right_sprites = []
        self.move_left_sprites = []
        self.idle_right_sprites = []
        self.idle_left_sprites = []
        self.jump_right_sprites = []
        self.jump_left_sprites = []
        self.attack_right_sprites = []
        self.attack_left_sprites = []
        
        # Moving
        self.move_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/player/run/Run (1).png"), (64,64))) 
        self.move_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/player/run/Run (2).png"), (64,64)))
        self.move_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/player/run/Run (3).png"), (64,64)))
        self.move_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/player/run/Run (4).png"), (64,64)))
        self.move_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/player/run/Run (5).png"), (64,64)))
        self.move_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/player/run/Run (6).png"), (64,64)))
        self.move_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/player/run/Run (7).png"), (64,64)))
        self.move_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/player/run/Run (8).png"), (64,64)))
        self.move_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/player/run/Run (9).png"), (64,64)))
        self.move_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/player/run/Run (10).png"), (64,64)))
        for sprite in self.move_right_sprites:
            self.move_left_sprites.append(pygame.transform.flip(sprite, True, False))
            
        # Idling
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/player/idle/Idle (1).png"), (64,64))) 
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/player/idle/Idle (2).png"), (64,64)))
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/player/idle/Idle (3).png"), (64,64)))
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/player/idle/Idle (4).png"), (64,64)))
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/player/idle/Idle (5).png"), (64,64)))
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/player/idle/Idle (6).png"), (64,64)))
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/player/idle/Idle (7).png"), (64,64)))
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/player/idle/Idle (8).png"), (64,64)))
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/player/idle/Idle (9).png"), (64,64)))
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/player/idle/Idle (10).png"), (64,64)))
        for sprite in self.idle_right_sprites:
            self.idle_left_sprites.append(pygame.transform.flip(sprite, True, False))
        
        # Jumping
        self.jump_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/player/jump/Jump (1).png"), (64,64))) 
        self.jump_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/player/jump/Jump (2).png"), (64,64)))
        self.jump_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/player/jump/Jump (3).png"), (64,64)))
        self.jump_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/player/jump/Jump (4).png"), (64,64)))
        self.jump_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/player/jump/Jump (5).png"), (64,64)))
        self.jump_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/player/jump/Jump (6).png"), (64,64)))
        self.jump_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/player/jump/Jump (7).png"), (64,64)))
        self.jump_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/player/jump/Jump (8).png"), (64,64)))
        self.jump_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/player/jump/Jump (9).png"), (64,64)))
        self.jump_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/player/jump/Jump (10).png"), (64,64)))
        for sprite in self.jump_right_sprites:
            self.jump_left_sprites.append(pygame.transform.flip(sprite, True, False))
        
        # Jumping
        self.attack_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/player/attack/Attack (1).png"), (64,64))) 
        self.attack_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/player/attack/Attack (2).png"), (64,64)))
        self.attack_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/player/attack/Attack (3).png"), (64,64)))
        self.attack_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/player/attack/Attack (4).png"), (64,64)))
        self.attack_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/player/attack/Attack (5).png"), (64,64)))
        self.attack_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/player/attack/Attack (6).png"), (64,64)))
        self.attack_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/player/attack/Attack (7).png"), (64,64)))
        self.attack_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/player/attack/Attack (8).png"), (64,64)))
        self.attack_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/player/attack/Attack (9).png"), (64,64)))
        self.attack_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/player/attack/Attack (10).png"), (64,64)))
        for sprite in self.attack_right_sprites:
            self.attack_left_sprites.append(pygame.transform.flip(sprite, True, False))
        
        # Load image and get rect
        self.current_sprite = 0
        self.image = self.idle_right_sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, y)
        
        # Attach sprite groups
        self.platform_group = platform_group
        self.portal_group = portal_group
        self.bullet_group = bullet_group
        
        # Animation booleans
        self.animate_jump = False
        self.animate_fire = False
        
        # Load sounds
        self.jump_sound = pygame.mixer.Sound("zombie_knight/sounds/jump_sound.wav")
        self.slash_sound = pygame.mixer.Sound("zombie_knight/sounds/slash_sound.wav")
        self.portal_sound = pygame.mixer.Sound("zombie_knight/sounds/portal_sound.wav")
        self.hit_sound = pygame.mixer.Sound("zombie_knight/sounds/player_hit.wav")
        
        # Kinematics vectors
        self.position = vector(x, y)
        self.velocity = vector(0, 0)
        self.acceleration = vector(0, self.VERTICAL_ACCELERATION)
        
        # Set initial player values
        self.health = self.STARTING_HEALTH
        self.starting_x = x
        self.starting_y = y    
    
            
    def update(self):
        """ Update the player """
        self.move()
        self.check_collisions()
        self.check_animations()
    
    
    def move(self):
        """ Move the player """
        # Set acceleration vector
        self.acceleration = vector(0, self.VERTICAL_ACCELERATION)
        
        # If the user is pressind a key, set the x-component if the acceleration to be non-zero
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acceleration.x = -1 * self.HORISONTAL_ACCELERATION
            self.animate(self.move_left_sprites, .5)
        elif keys[pygame.K_RIGHT]:
            self.acceleration.x = self.HORISONTAL_ACCELERATION
            self.animate(self.move_right_sprites, .5)
        else:
            if self.velocity.x > 0:
                self.animate(self.idle_right_sprites, .5)
            else:
                self.animate(self.idle_left_sprites, .5)
            
        # Calcilate new kinematics values: (4,1) + (2,8) = (6,9)
        self.acceleration.x -= self.velocity.x * self.HORISONTAL_FRICTION
        self.velocity += self.acceleration
        self.position += self.velocity + 0.5 * self.acceleration
        
        # Update rect based on kinematic calculations and add wrap around movement
        if self.position.x < 0:
            self.position.x = WINDOW_WIDTH
        elif self.position.x > WINDOW_WIDTH:
            self.position.x = 0
            
        self.rect.bottomleft = self.position    
    
    def check_collisions(self):
        """ Check for collisions with platforms and portals """
        # Collision check between player and platforms when falling
        if self.velocity.y > 0:
            collided_platforms = pygame.sprite.spritecollide(self, self.platform_group, False)
            if collided_platforms:
                self.position.y = collided_platforms[0].rect.top + 1
                self.velocity.y = 0
                
        # Collision check between player and platform if jumping up
        if self.velocity.y < 0:
            collided_platforms = pygame.sprite.spritecollide(self, self.platform_group, False)
            if collided_platforms:
                self.velocity.y = 0
                while pygame.sprite.spritecollide(self, self.platform_group, False):
                    self.position.y += 1
                    self.rect.bottomleft = self.position
        
        # Collision check for portals
        if pygame.sprite.spritecollide(self, self.portal_group, False):
            self.portal_sound.play()
            # Determine which portal you are moving to
            # Left and right
            if self.position.x > WINDOW_WIDTH//2:
                self.position.x = 86
            else:
                self.position.x = WINDOW_WIDTH - 150 
            # Top and bottom
            if self.position.y > WINDOW_HEIGHT//2:
                self.position.y = 64
            else:
                self.position.y = WINDOW_HEIGHT - 132
                
            self.rect.bottomleft = self.position  


    def check_animations(self):
        """ Check to see if jump/fire animation shpuld run """
        # Animate the player jump
        if self.animate_jump:
            if self.velocity.x > 0:
                self.animate(self.jump_right_sprites, .1)
            else:
                self.animate(self.jump_left_sprites, .1)
        
        # Animate the player attack
        if self.animate_fire:
            if self.velocity.x > 0:
                self.animate(self.attack_right_sprites, .25)
            else:
                self.animate(self.attack_left_sprites, .25)
        
            
        
    def jump(self):
        """ Jump upwards if on a platform """
        # Only jump if on a platform
        if pygame.sprite.spritecollide(self, self.platform_group, False):
            self.jump_sound.play()
            self.velocity.y = -1 * self.VERTICAL_JUMP_SPEED
            self.animate_jump = True
            
    def fire(self):
        """ Fire a 'bullet' from a sword """
        self.slash_sound.play()
        Bullet(self.rect.centerx, self.rect.centery, self.bullet_group, self)
        self.animate_fire = True

    def reset(self):
        """ Reset the player's position """
        self.position = vector(self.starting_x, self.starting_y)
        self.rect.bottomleft = self.position

    def animate(self, sprite_list, speed):
        """ Anemate the players actions """
        if self.current_sprite < len(sprite_list) - 1:
            self.current_sprite += speed
        else:
            self.current_sprite = 0
            # End the jump animation
            if self.animate_jump:
                self.animate_jump = False
            # End the attack animation
            if self.animate_fire:
                self.animate_fire = False
            
        self.image = sprite_list[int(self.current_sprite)]

class Bullet(pygame.sprite.Sprite):
    """ A projectile launched by the player """
    
    def __init__(self, x, y, bullet_group, player):
        """ Initialize the bullet """
        super().__init__()
        
        # Set constant variables
        self.VELOCITY = 20
        self.RANGE = 500
        
        # Load image and get a rect
        if player.velocity.x > 0:
            self.image = pygame.transform.scale(pygame.image.load("zombie_knight/images/player/slash.png"), (32,32))
        else:
            self.image = pygame.transform.scale(pygame.transform.flip(pygame.image.load("zombie_knight/images/player/slash.png"), True, False), (32,32))
            self.VELOCITY = -1*self.VELOCITY
            
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
        self.starting_x = x
        
        bullet_group.add(self)

    def update(self):
        """ Update the bullet """
        self.rect.x += self.VELOCITY
        
        # If the bullet has passed the range, kill it
        if abs(self.rect.x - self.starting_x) > self.RANGE:
            self.kill()

class Zombie(pygame.sprite.Sprite):
    """ An enemy class that moves across the screen """
    
    def __init__(self, platform_group, portal_group, min_speed, max_speed):
        """ Initialize the zombie """
        super().__init__()
        
        # Set constant variables
        self.VERTICAL_ACCELERATION = 3 # Gravity
        self.RISE_TIME = 2
        
        # Animation frames
        self.walk_right_sprites = []
        self.walk_left_sprites = []
        self.die_right_sprites = []
        self.die_left_sprites = []
        self.rise_left_sprites = []
        self.rise_right_sprites = []
        
        gender = random.randint(0,1)
        if gender == 0:
            # Walking
            self.walk_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/boy/walk/Walk (1).png"), (64,64)))
            self.walk_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/boy/walk/Walk (2).png"), (64,64)))
            self.walk_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/boy/walk/Walk (3).png"), (64,64)))
            self.walk_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/boy/walk/Walk (4).png"), (64,64)))
            self.walk_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/boy/walk/Walk (5).png"), (64,64)))
            self.walk_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/boy/walk/Walk (6).png"), (64,64)))
            self.walk_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/boy/walk/Walk (7).png"), (64,64)))
            self.walk_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/boy/walk/Walk (8).png"), (64,64)))
            self.walk_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/boy/walk/Walk (9).png"), (64,64)))
            self.walk_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/boy/walk/Walk (10).png"), (64,64)))
            for sprite in self.walk_right_sprites:
                self.walk_left_sprites.append(pygame.transform.flip(sprite, True, False))
                
            # Dying
            self.die_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/boy/dead/Dead (1).png"), (64,64)))
            self.die_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/boy/dead/Dead (2).png"), (64,64)))
            self.die_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/boy/dead/Dead (3).png"), (64,64)))
            self.die_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/boy/dead/Dead (4).png"), (64,64)))
            self.die_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/boy/dead/Dead (5).png"), (64,64)))
            self.die_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/boy/dead/Dead (6).png"), (64,64)))
            self.die_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/boy/dead/Dead (7).png"), (64,64)))
            self.die_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/boy/dead/Dead (8).png"), (64,64)))
            self.die_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/boy/dead/Dead (9).png"), (64,64)))
            self.die_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/boy/dead/Dead (10).png"), (64,64)))
            for sprite in self.die_right_sprites:
                self.die_left_sprites.append(pygame.transform.flip(sprite, True, False))
                
            #Rising
            self.rise_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/boy/walk/Walk (10).png"), (64,64)))
            self.rise_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/boy/walk/Walk (9).png"), (64,64)))
            self.rise_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/boy/walk/Walk (8).png"), (64,64)))
            self.rise_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/boy/walk/Walk (7).png"), (64,64)))
            self.rise_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/boy/walk/Walk (6).png"), (64,64)))
            self.rise_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/boy/walk/Walk (5).png"), (64,64)))
            self.rise_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/boy/walk/Walk (4).png"), (64,64)))
            self.rise_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/boy/walk/Walk (3).png"), (64,64)))
            self.rise_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/boy/walk/Walk (2).png"), (64,64)))
            self.rise_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/boy/walk/Walk (1).png"), (64,64)))
            for sprite in self.rise_right_sprites:
                self.rise_left_sprites.append(pygame.transform.flip(sprite, True, False))
        
        else:
            # Walking
            self.walk_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/girl/walk/Walk (1).png"), (64,64)))
            self.walk_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/girl/walk/Walk (2).png"), (64,64)))
            self.walk_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/girl/walk/Walk (3).png"), (64,64)))
            self.walk_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/girl/walk/Walk (4).png"), (64,64)))
            self.walk_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/girl/walk/Walk (5).png"), (64,64)))
            self.walk_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/girl/walk/Walk (6).png"), (64,64)))
            self.walk_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/girl/walk/Walk (7).png"), (64,64)))
            self.walk_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/girl/walk/Walk (8).png"), (64,64)))
            self.walk_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/girl/walk/Walk (9).png"), (64,64)))
            self.walk_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/girl/walk/Walk (10).png"), (64,64)))
            for sprite in self.walk_right_sprites:
                self.walk_left_sprites.append(pygame.transform.flip(sprite, True, False))
                
            # Dying
            self.die_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/girl/dead/Dead (1).png"), (64,64)))
            self.die_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/girl/dead/Dead (2).png"), (64,64)))
            self.die_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/girl/dead/Dead (3).png"), (64,64)))
            self.die_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/girl/dead/Dead (4).png"), (64,64)))
            self.die_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/girl/dead/Dead (5).png"), (64,64)))
            self.die_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/girl/dead/Dead (6).png"), (64,64)))
            self.die_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/girl/dead/Dead (7).png"), (64,64)))
            self.die_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/girl/dead/Dead (8).png"), (64,64)))
            self.die_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/girl/dead/Dead (9).png"), (64,64)))
            self.die_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/girl/dead/Dead (10).png"), (64,64)))
            for sprite in self.die_right_sprites:
                self.die_left_sprites.append(pygame.transform.flip(sprite, True, False))
                
            #Rising
            self.rise_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/girl/walk/Walk (10).png"), (64,64)))
            self.rise_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/girl/walk/Walk (9).png"), (64,64)))
            self.rise_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/girl/walk/Walk (8).png"), (64,64)))
            self.rise_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/girl/walk/Walk (7).png"), (64,64)))
            self.rise_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/girl/walk/Walk (6).png"), (64,64)))
            self.rise_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/girl/walk/Walk (5).png"), (64,64)))
            self.rise_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/girl/walk/Walk (4).png"), (64,64)))
            self.rise_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/girl/walk/Walk (3).png"), (64,64)))
            self.rise_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/girl/walk/Walk (2).png"), (64,64)))
            self.rise_right_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/zombie/girl/walk/Walk (1).png"), (64,64)))
            for sprite in self.rise_right_sprites:
                self.rise_left_sprites.append(pygame.transform.flip(sprite, True, False))
            
        
        # Load an image and get rect
        self.direction = random.choice([-1, 1])
        
        self.current_sprite = 0
        if self.direction == -1:
            self.image = self.walk_left_sprites[self.current_sprite]
        else:
            self.image = self.walk_right_sprites[self.current_sprite]
            
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (random.randint(100, WINDOW_WIDTH - 100), -100)          
        
        # Attach sprite groups
        self.platform_group = platform_group
        self.portal_group = portal_group
        
        # Animation booleans
        self.animate_death = False
        self.animate_rise = False
        
        # Load sounds
        self.hit_sound = pygame.mixer.Sound("zombie_knight/sounds/zombie_hit.wav")
        self.kick_sound = pygame.mixer.Sound("zombie_knight/sounds/zombie_kick.wav")
        self.portal_sound = pygame.mixer.Sound("zombie_knight/sounds/portal_sound.wav")            
        
        # Kinematics vectors
        self.position = vector(self.rect.x, self.rect.y)
        self.velocity = vector(self.direction * random.randint(min_speed, max_speed), 0)
        self.acceleration = vector(0, self.VERTICAL_ACCELERATION)
        
        # Initial zombie values
        self.is_dead = False
        self.round_time = 0
        self.frame_count = 0
        
            
    def update(self):
        """ Update the zombie """
        self.move()
        self.check_collisions()
        self.check_animations()
    
    def move(self):
        """ Move the zombie """
        # We don't need to update the acceleration vector because it never changes here         
        # Calcilate new kinematics values: (4,1) + (2,8) = (6,9)
        self.velocity += self.acceleration
        self.position += self.velocity + 0.5 * self.acceleration
        
        # Update rect based on kinematic calculations and add wrap around movement
        if self.position.x < 0:
            self.position.x = WINDOW_WIDTH
        elif self.position.x > WINDOW_WIDTH:
            self.position.x = 0
            
        self.rect.bottomleft = self.position    
    
    
    def check_collisions(self):
        """ Check for collisions with platforms and portals """
        # Collision check between player and platforms when falling
        collided_platforms = pygame.sprite.spritecollide(self, self.platform_group, False)
        if collided_platforms:
            self.position.y = collided_platforms[0].rect.top + 1
            self.velocity.y = 0
        
        # Collision check for portals
        if pygame.sprite.spritecollide(self, self.portal_group, False):
            self.portal_sound.play()
            # Determine which portal you are moving to
            # Left and right
            if self.position.x > WINDOW_WIDTH//2:
                self.position.x = 86
            else:
                self.position.x = WINDOW_WIDTH - 150 
            # Top and bottom
            if self.position.y > WINDOW_HEIGHT//2:
                self.position.y = 64
            else:
                self.position.y = WINDOW_HEIGHT - 132
                
            self.rect.bottomleft = self.position  
            
            
    def check_animations(self):
        """ Check to see if death/rise animation shpuld run """
        pass
    

    def animate(self):
        """ Animate the zombie's actions """
        pass
    
    
class RubyMaker(pygame.sprite.Sprite):
    """ A title that is animated.A ruby will be generated here """
    
    def __init__(self, x, y, main_group):
        """ Initialize the ruby maker """
        super().__init__()
        
        # Animation frames
        self.ruby_sprites = []
        
        # Rotating
        self.ruby_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/ruby/tile000.png"), (64, 64)))
        self.ruby_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/ruby/tile001.png"), (64, 64)))
        self.ruby_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/ruby/tile002.png"), (64, 64)))
        self.ruby_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/ruby/tile003.png"), (64, 64)))
        self.ruby_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/ruby/tile004.png"), (64, 64)))
        self.ruby_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/ruby/tile005.png"), (64, 64)))
        self.ruby_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/ruby/tile006.png"), (64, 64)))

        # Load image and get rect
        self.current_sprite = 0
        self.image = self.ruby_sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, y)
        
        # Add to the main group for drawing purposes
        main_group.add(self)
        
        
    def update(self):
        """ Update the ruby maker """
        self.animate(self.ruby_sprites, .25)

    def animate(self, sprite_list, speed):
        """ Animate the ruby maker """
        if self.current_sprite < len(sprite_list) - 1:
            self.current_sprite += speed
        else:
            self.current_sprite = 0
            
        self.image = sprite_list[int(self.current_sprite)]
    
    
class Ruby(pygame.sprite.Sprite):
    """ A class the player must collect to earn points and health """
    
    def __init__(self):
        """ Initialize the ruby """
        pass
    
    def update(self):
        """ Update the ruby """
        pass
    
    def move(self):
        """ Move the ruby """
        pass
    
    def check_collisions(self):
        """ Check for collisions with platforms and portals """
        pass
    
    def animate(self):
        """ Animate the ruby """
        pass
    
    
class Portal(pygame.sprite.Sprite):
    """ A class that if collided with will transport you """
    
    def __init__(self, x, y, color, portal_group):
        """ Initialize the portal """
        super().__init__()
        
        # Animation frames
        self.portal_sprites = []
        
        # Portal animation
        if color == "green":
            # Green portal
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/portals/green/tile000.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/portals/green/tile001.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/portals/green/tile002.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/portals/green/tile003.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/portals/green/tile004.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/portals/green/tile005.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/portals/green/tile006.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/portals/green/tile007.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/portals/green/tile008.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/portals/green/tile009.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/portals/green/tile010.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/portals/green/tile011.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/portals/green/tile012.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/portals/green/tile013.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/portals/green/tile014.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/portals/green/tile015.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/portals/green/tile016.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/portals/green/tile017.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/portals/green/tile018.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/portals/green/tile019.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/portals/green/tile020.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/portals/green/tile021.png"), (72, 72)))
        else:
            # Purple portal
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/portals/purple/tile000.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/portals/purple/tile000.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/portals/purple/tile000.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/portals/purple/tile000.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/portals/purple/tile000.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/portals/purple/tile000.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/portals/purple/tile000.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/portals/purple/tile000.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/portals/purple/tile001.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/portals/purple/tile002.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/portals/purple/tile003.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/portals/purple/tile004.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/portals/purple/tile005.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/portals/purple/tile006.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/portals/purple/tile007.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/portals/purple/tile008.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/portals/purple/tile009.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/portals/purple/tile010.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/portals/purple/tile011.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/portals/purple/tile012.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/portals/purple/tile013.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/portals/purple/tile014.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/portals/purple/tile015.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/portals/purple/tile016.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/portals/purple/tile017.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/portals/purple/tile018.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/portals/purple/tile019.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/portals/purple/tile020.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("zombie_knight/images/portals/purple/tile021.png"), (72, 72)))

        # Load an image and get a rect
        self.current_sprite = random.randint(0, len(self.portal_sprites) - 1)
        self.image = self.portal_sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, y)            
        
        # Add to the portal group
        portal_group.add(self)

    def update(self):
        """ Update the portal """
        self.animate(self.portal_sprites, .2)
    
    def animate(self, sprite_list, speed):
        """ Animate the portal """
        if self.current_sprite < len(sprite_list) - 1:
            self.current_sprite += speed
        else:
            self.current_sprite = 0
            
        self.image = sprite_list[int(self.current_sprite)]


# Create sprite groups
my_main_tile_group = pygame.sprite.Group() 
my_platform_group = pygame.sprite.Group()
my_player_group = pygame.sprite.Group()
my_bullet_group = pygame.sprite.Group()
my_zombie_group = pygame.sprite.Group()
my_portal_group = pygame.sprite.Group()
my_ruby_group = pygame.sprite.Group()

# Create the tile map
# 0-> no tile, 1-> dirt, 2-5-> platforms, 6-> ruby maker, 7-8-> platform, 9-> player
# 23 rows and 40 columns
tile_map = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0],
    [4,4,4,4,4,4,4,4,4,4,4,4,4,4,5,0,0,0,0,6,0,0,0,0,0,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,5,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [4,4,4,4,4,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,4,4,4,4,4],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,5,0,0,0,0,0,0,0,0,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,4,4,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,0,0],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
] 

# Generate Tile objects from the tile map
# Loop through the 23 lists (raws) in the tile map (i moves us down the map)
for i in range(len(tile_map)):
    # Loop through the 40 elements in a given list (cols) (j moves us across the map)
    for j in range(len(tile_map[i])):
        # Dirt tile
        if tile_map[i][j] == 1:
            Tile(j*32, i*32, 1, my_main_tile_group)
        # Platform tiles
        elif tile_map[i][j] == 2:
            Tile(j*32, i*32, 2, my_main_tile_group, my_platform_group)
        elif tile_map[i][j] == 3:
            Tile(j*32, i*32, 3, my_main_tile_group, my_platform_group)
        elif tile_map[i][j] == 4:
            Tile(j*32, i*32, 4, my_main_tile_group, my_platform_group)
        elif tile_map[i][j] == 5:
            Tile(j*32, i*32, 5, my_main_tile_group, my_platform_group)
        # Ruby Maker
        elif tile_map[i][j] == 6:
            RubyMaker(j*32, i*32, my_main_tile_group)
        # Portals
        elif tile_map[i][j] == 7:
            Portal(j*32, i*32, "green", my_portal_group)
        elif tile_map[i][j] == 8:
            Portal(j*32, i*32, "purple", my_portal_group)
        # Player 
        elif tile_map[i][j] == 9:
            my_player = Player(j*32 - 32, i*32 + 32, my_platform_group, my_portal_group, my_bullet_group)
            my_player_group.add(my_player)



# Load a background image (we must resize)
background_image = pygame.transform.scale(pygame.image.load("zombie_knight/images/background.png"), (1280, 736))
background_rect = background_image.get_rect()
background_rect.topleft = (0, 0)

# Create a game 
my_game = Game()

# The main game loop
running = True
while running:
    # Check to see if the user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # Player wants to jump
            if event.key == pygame.K_SPACE:
                my_player.jump()
            # Player wants to fire
            if event.key == pygame.K_UP:
                my_player.fire()
            # Rain zombies
            if event.key == pygame.K_RETURN:
                zombie = Zombie(my_platform_group, my_portal_group, 2, 7)
                my_zombie_group.add(zombie)
                
    # Blit the background
    display_surface.blit(background_image, background_rect)
    
    # Draw tiles and update ruby maker
    my_main_tile_group.update()
    my_main_tile_group.draw(display_surface)
    
    # Update and draw sprite groups
    my_portal_group.update()
    my_portal_group.draw(display_surface)
    
    my_player_group.update()
    my_player_group.draw(display_surface)
    
    my_bullet_group.update()
    my_bullet_group.draw(display_surface)
    
    my_zombie_group.update()
    my_zombie_group.draw(display_surface)
    
    # Update and draw the game
    my_game.update()
    my_game.draw()
    
    # Update the display and tick the clock
    pygame.display.update()
    clock.tick(FPS)
    
# End the game
pygame.quit()