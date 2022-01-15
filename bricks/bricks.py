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

# Settings for bat
player_Y = 540
mouse_x = 0
mouse_y = player_Y

# Settings for ball
ball_start_Y = 200
ball_speed = 3
ball_served = False

# Bat initialization
bat_image = pygame.image.load("bat.png")
bat_rect = bat_image.get_rect()

# Ball initialization
ball_image = pygame.image.load("ball.png")
ball_rect = ball_image.get_rect()

b_X, b_Y = (24, ball_start_Y)
s_X, s_Y = (ball_speed, ball_speed)
ball_rect.topleft = (b_X, b_Y)

# brick init
brick = pygame.image.load("brick.png")
bricks = []
for y in range(5):
    brick_Y = (y * 24) + 100
    for x in range(10):
        brick_X = (x * 31) + 245
        width = brick.get_width()
        height = brick.get_height()
        rect = pygame.Rect(brick_X,brick_Y,width,height)
        bricks.append(rect)


# Main loop
running = True
while running:
    display_surface.fill(BLACK)
    
    # brick draw
    for b in bricks:
        display_surface.blit(brick,b)
    
    # bat and ball draw
    display_surface.blit(bat_image, bat_rect)
    display_surface.blit(ball_image, ball_rect)
    
    # all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.MOUSEMOTION:
            if not ball_served:
                ball_served = True
            mouse_x, mouse_y = event.pos
            if (mouse_x < 800 - 55):
                bat_rect.topleft = (mouse_x, player_Y)
            else:
                bat_rect.topleft = (800 - 55, player_Y)
            
            
    # main game logic
    if ball_served:
        b_X += s_X
        b_Y += s_Y
        ball_rect.topleft = (b_X, b_Y)
        
    # collision detection
    
    if (b_Y <= 0):
        b_Y = 0
        s_Y *= -1
        
    if (b_Y >= 600-8):
        b_Y = 600 - 8
        s_Y *= -1
    
    if (b_X <= 0):
        b_X = 0
        s_X *= -1
        
    if (b_X >= 800-8):
        b_X = 800 - 8
        s_X *= -1
    
    if ball_rect.colliderect(bat_rect):
        b_Y = player_Y - 8
        s_Y *= -1
    
    # Update display and tick the clock
    pygame.display.update()
    clock.tick(FPS)
            


# End the game
pygame.quit()