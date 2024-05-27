import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Shift Key Detector")

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LSHIFT:
                print("Left Shift key is pressed")
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LSHIFT:
                print("Left Shift key is released")

# Quit Pygame
pygame.quit()
