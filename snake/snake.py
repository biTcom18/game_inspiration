import pygame, random

# Initialize pygame
pygame.init()

# Set display window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("~~Snake~~")

# Set FPS and clock
FPS = 20
clock = pygame.time.Clock()

# Set game values  
SNAKE_SIZE = 20

head_x = WINDOW_WIDTH//2
head_y = WINDOW_HEIGHT//2 + 100

snake_dx = 0
snake_dy = 0

score = 0

# Set colors
GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
RED = (255, 0 , 0)
DARKRED = (150, 0, 0)
WHITE = (255, 255, 255)

# Set fonts
font = pygame.font.SysFont("gabriola",  48)


# Set text
title_text = font.render("~~Snake~~", True, GREEN, DARKRED)
title_rect = title_text.get_rect()
title_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

score_text = font.render("Score: " + str(score), True, GREEN, DARKRED)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

game_over_text = font.render("GAMEOVER", True, RED, DARKGREEN)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2, WINDOW_WIDTH//2)



continue_text = font.render('Press any key to play again', True, RED, DARKGREEN)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 64)


# Set sound and music
pick_up_sound = pygame.mixer.Sound("pick_up.wav")

# Set images ( in this case, use simple rects ... so just create their coordinates top-left x,top-left y, width, height)
apple_coord = (500, 500, SNAKE_SIZE, SNAKE_SIZE) 
apple_rect = pygame.draw.rect(display_surface, RED, apple_coord)

head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
head_rect = pygame.draw.rect(display_surface, RED, head_coord)

body_coord = []


# The main game loop
running = True
while running:
    # Check to see if the user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        #Move the snake
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_dx = -1*SNAKE_SIZE
                snake_dy = 0
            if event.key == pygame.K_RIGHT:
                snake_dx = SNAKE_SIZE
                snake_dy = 0
            if event.key == pygame.K_UP:
                snake_dx = 0
                snake_dy = -1*SNAKE_SIZE
            if event.key == pygame.K_DOWN:
                snake_dx = 0
                snake_dy = SNAKE_SIZE
                
    # Update the x,y position of the snakes head and make a new coordinates
    head_x += snake_dx
    head_y += snake_dy
    head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE) 
            
     
     
    # Check for colli sions 
    if head_rect.colliderect(apple_rect):
        score += 1
        pick_up_sound.play()
    
        apple_x = random.randint(0, WINDOW_WIDTH - SNAKE_SIZE)
        apple_y = random.randint(0, WINDOW_HEIGHT - SNAKE_SIZE)
        apple_coord = (apple_x, apple_y, SNAKE_SIZE, SNAKE_SIZE)
        
    # Fill the surface
    display_surface.fill(WHITE)
    
    # Blit HUD
    display_surface.blit(title_text, title_rect)
    display_surface.blit(score_text, score_rect)
    
                
    # Blit assets and still need the body
    head_rect = pygame.draw.rect(display_surface, GREEN, head_coord)
    apple_rect = pygame.draw.rect(display_surface, RED, apple_coord)
    
    # Update display and tick clock
    pygame.display.update()
    clock.tick(FPS)
    
                
                        
# End the game
pygame.quit()

