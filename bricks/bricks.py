import pygame

# Initialize pygame
pygame.init()

# Set display
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Bricks")


# Set FPS and clock
FPS = 30
clock = pygame.time.Clock()

# Set colors 
BLACK = (0, 0, 0)

# Set game values
player_Y = 540
mouse_x = 0
mouse_y = player_Y

# Bat initialization
bat_image = pygame.image.load("bat.png")
bat_rect = bat_image.get_rect()




# ball init
# brick init


# Main loop
running = True
while running:
    display_surface.fill(BLACK)
    
    # brick draw
    
    # bat and ball draw
    display_surface.blit(bat_image, bat_rect)
    
    # all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # main game logic
    
    # collision detection
    
    # Update display and tick the clock
    pygame.display.update()
    clock.tick(FPS)
            


# End the game
pygame.quit()