















































import pygame

# Initialize pygame
pygame.init()

# Set display surface
WINDOW_WIDTH = 960
WINDOW_HEIGHT = 640

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Making a tile map!")

# Set FPS and clock
FPS = 30
clock = pygame.time.Clock()

# The main game loop
running = True
while running:
    # Check to see if the user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    # Update display and tick clock        
    pygame.display.update()
    clock.tick(FPS)
  
# End the game      
pygame.quit()
