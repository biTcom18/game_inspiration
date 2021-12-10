





















































import pygame

# Initialize pygame
pygame.init()

# Set display surface
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Sprite Group")


# The main gaim loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
            
# End game
pygame.quit()
