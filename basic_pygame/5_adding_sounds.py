import  pygame

# Initialize pygame
pygame.init()

# Create display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Adding Sounds")

# Loading sound effects
sound_1 = pygame.mixer.Sound('sound_1.wav')
sound_2 = pygame.mixer.Sound('sound_2.wav')

# Play the sound effects
sound_1.play()
pygame.time.delay(2000)
sound_2.play()

# Change the volume og a sound effect
sound_2.set_volume(.1)
sound_2.play()

# Load background music
pygame.mixer.music.load('music.wav')

# Play and stop the music
pygame.mixer.music.play(-1, 0.0)
pygame.time.delay(15000)
pygame.mixer.music.stop()

# The main gaim loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# The end of game
pygame.quit()

