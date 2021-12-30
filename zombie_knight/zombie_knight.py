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
    
    def __ini__(self):
        """ Initialize the player """
        pass
    
    def update(self):
        """ Update the player """
        pass
    
    def move(self):
        """ Move the player """
        pass
    
    
    def check_collisions(self):
        """ Check for collisions with platforms and portals """
        pass 

    def check_animations(self):
        """ Check to see if jump/fire animation shpuld run """
        pass
        
    def jump(self):
        """ Jump upwards if on a platform """
        pass        
    
    def fire(self):
        """ Fire a 'bullet' from a sword """
        pass

    def reset(self):
        """ Reset the player's position """
        pass

    def animate(self):
        """ Anemate the players actions """
        pass

class Bullet(pygame.sprite.Sprite):
    """ A projectile launched by the player """
    
    def __init__(self):
        """ Initialize the bullet """
        pass

    def update(self):
        """ Update the bullet """
        pass

class Zombie(pygame.sprite.Sprite):
    """ An enemy class that moves across the screen """
    
    def __ini__(self):
        """ Initialize the zombie """
        pass
    
    def update(self):
        """ Update the zombie """
        pass
    
    def move(self):
        """ Move the zombie """
        pass
    
    
    def check_collisions(self):
        """ Check for collisions with platforms and portals """
        pass 

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
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,5,0,0,0,0,0,0,0,0,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,4,4,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
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
            pass



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
            
    # Blit the background
    display_surface.blit(background_image, background_rect)
    
    # Draw tiles and update ruby maker
    my_main_tile_group.update()
    my_main_tile_group.draw(display_surface)
    
    # Update and draw sprite groups
    my_portal_group.update()
    my_portal_group.draw(display_surface)
    
    # Update and draw the game
    my_game.update()
    my_game.draw()
    
    # Update the display and tick the clock
    pygame.display.update()
    clock.tick(FPS)
    
# End the game
pygame.quit()