# hello world

x = 0

# import pygame
# print(pygame.ver)

import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Control the Box")

# Define colors
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Set up the box
box_size = 50
box_x = screen_width // 2 - box_size // 2
box_y = screen_height // 2 - box_size // 2
box_speed = 5

# create bullets
bullet_size = 20
bullet_x = -screen_width
bullet_y = screen_height // 2 - bullet_size // 2
bullet_speed = 5

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get the state of all keyboard buttons
    keys = pygame.key.get_pressed()
    
    # Move the box
    if keys[pygame.K_LEFT]:
        box_x -= box_speed
    if keys[pygame.K_RIGHT]:
        box_x += box_speed
    if keys[pygame.K_UP]:
        box_y -= box_speed
    if keys[pygame.K_DOWN]:
        box_y += box_speed

    # move bullets
    bullet_x += bullet_speed
    
    # Ensure the box stays within the window boundaries
    box_x = max(0, min(box_x, screen_width - box_size))
    box_y = max(0, min(box_y, screen_height - box_size))

    # bullet boundaries
    bullet_x = max(0, min(bullet_x, screen_width - bullet_size))
    bullet_y = max(0, min(bullet_y, screen_height - bullet_size))
    
    # Fill the screen with white color
    screen.fill(white)
    
    # Draw the box
    pygame.draw.rect(screen, red, (box_x, box_y, box_size, box_size))

    # draw bullets
    pygame.draw.rect(screen, black, (bullet_x, bullet_y, bullet_size, bullet_size))
    
    # GAME

    if bullet_x == box_x and bullet_y == box_y:
        box_size = 0
        break

    # Update the display
    pygame.display.flip()
    
    # Cap the frame rate
    pygame.time.Clock().tick(60)


# Quit pygame
pygame.quit()
sys.exit()



print('yay')