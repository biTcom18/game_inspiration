import pygame, random

# Initialize pygame
pygame.init()

# Set display surface
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 400
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Feed the Dragon")

# Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

# Set game values
PLAYER_STARTING_LIVES = 5
PLAYER_VELOCITY = 5
COIN_STARTING_VELOCITY = 5
COIN_ACCELERATION = 0.5
BUFFER_DISTANCE = -900

score = 0
player_lives = PLAYER_STARTING_LIVES
coin_velocity = COIN_STARTING_VELOCITY


# Set colors
GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# Set fonts
font = pygame.font.Font("AttackGraffiti.ttf", 32)

# Set text
score_text = font.render("Score :" + str(score), True, GREEN, DARKGREEN)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

title_text = font.render("Feed the Dragon", True, WHITE, DARKGREEN)
title_rect = title_text.get_rect()

title_rect.centerx = WINDOW_WIDTH//2
title_rect.y = 10

lives_text = font.render("Lives: " + str(player_lives), True, GREEN, DARKGREEN)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH - 10, 10)

game_over_text = font.render("GAMEOVER", True, GREEN, DARKGREEN)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

continue_text = font.render("Press any key to play again", True, GREEN, DARKGREEN)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 32)

# Set sounds and music
coin_sound = pygame.mixer.Sound("sound_1.wav")
miss_sound = pygame.mixer.Sound("sound_2.wav")
miss_sound.set_volume(.1)
pygame.mixer.music.load("music.wav")

# Set images
player_image = pygame.image.load("dragon_left.png")
player_rect = player_image.get_rect()
player_rect.left = 900
player_rect.centery = WINDOW_HEIGHT//2

coin_image = pygame.image.load("coin.png")
coin_rect = coin_image.get_rect()
coin_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
coin_rect.y = random.randint(64, WINDOW_HEIGHT - 32)


 


# Main loop
running = True
while running:
    # Check to see if user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Fill the display
    display_surface.fill(BLACK)
    
    # Blit the HUD to screen
    display_surface.blit(score_text, score_rect)
    display_surface.blit(title_text, title_rect)
    display_surface.blit(lives_text, lives_rect)
    pygame.draw.line(display_surface, WHITE, (0,64),(WINDOW_WIDTH, 64), 2)
    
    # Blit assets to screen
    display_surface.blit(player_image, player_rect)
    display_surface.blit(coin_image, coin_rect)
    
    # Update display and tick the clock
    pygame.display.update()
    clock.tick(FPS)
    
    

# End the game
pygame.quit()
