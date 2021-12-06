import pygame, random

# Initialize pygame
pygame.init()

# Create our display surface
WINDOW_WIDTH = 945
WINDOW_HIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HIGHT))
pygame.display.set_caption("Catch the Clown")

# Set FPS and clock
FPS = 30
clock = pygame.time.Clock()

# Set game values
PLAYER_STARTING_LIVES = 5
CLOWN_STARTING_VELOCITY = 3
CLOWN_ACCELERATION = .5

score = 0
player_lives = PLAYER_STARTING_LIVES

clown_velocity = CLOWN_STARTING_VELOCITY
clown_dx = random.choice([-1, 1])
clown_dy = random.choice([-1, 1])


# Set colors
BLUE = (1, 175, 209)
YELLOW = (248, 231, 28)

# Set fonts
font = pygame.font.Font("Franxurter.ttf", 32)

# Set text
title_text = font.render("Catch the Clown", True, BLUE)
title_rect = title_text.get_rect()
title_rect.topleft = (50, 10)

score_text = font.render("Score: " + str(score), True, YELLOW)
score_rect = score_text.get_rect()
score_rect.topright = (WINDOW_WIDTH - 50, 10)

lives_text = font.render("Lives: " + str(player_lives), True, YELLOW)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH - 50, 50)

game_over_text = font.render("GAMEOVER", True, YELLOW)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2, WINDOW_HIGHT//2)

continue_text = font.render("Click anywhere to play again", True, YELLOW, BLUE)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH//2, WINDOW_HIGHT//2 + 64)

# Set sound and music
click_sound = pygame.mixer.Sound("click_sound.wav")
miss_sound = pygame.mixer.Sound("miss_sound.wav")
pygame.mixer.music.load("ctc_background_music.wav")
 
# Set images
background_image = pygame.image.load("background.png")
background_rect = background_image.get_rect()
background_rect.topleft = (0, 0)


clown_image = pygame.image.load("clown.png")
clown_rect = clown_image.get_rect()
clown_rect.center = (WINDOW_WIDTH//2, WINDOW_HIGHT//2)

# The main gaim loop
running = True
while running:
    # Check to see if the user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Blit the background
    display_surface.blit(background_image, background_rect)
    
    # Blit HUD
    display_surface.blit(title_text, title_rect)
    display_surface.blit(score_text, score_rect)
    display_surface.blit(lives_text, lives_rect)
    
    # Blit assets
    display_surface.blit(clown_image, clown_rect)
    
    # Update the display and tick clock
    pygame.display.update()
    clock.tick(FPS)
            
# End the game
pygame.quit()

