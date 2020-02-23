import pygame
import numpy as np
from player import Player
import draw
import copy
from level_one import cockpit
import terminal

pygame.init()

# Pygame screen parameters
WIDTH = 800
HEIGHT = 600
FPS = 10  # Updates per second
room_offset = (100, 100)  # How far in the window is the room drawn

astronaut = Player(130, 150)
planet_image = pygame.image.load("images/mars.png")
ship_image = pygame.image.load("images/ship.png")
bg_image = pygame.image.load("images/backdrop.jpg")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galactic: The Final Frontier")
running = True
clock = pygame.time.Clock()

walkable_spaces = [0, 10]

while running:
    player_to_grid_x = (astronaut.location[0] - room_offset[0]) / 30
    player_to_grid_y = (astronaut.location[1] - room_offset[1]) / 30
    old_location = copy.copy(astronaut.location)
    # Check user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Check for object usage
                if cockpit[int(player_to_grid_y), int(player_to_grid_x) - 1] == 0:
                    # Todo: Make this much more accurate
                    print("Computer hacking detected")
                    terminal.terminal_game(screen, clock)
            elif event.key == pygame.K_ESCAPE:
                running = False
    # Look at all keys being pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        astronaut.frame = (astronaut.frame + 1) % 5
        astronaut.direction = "left"
        astronaut.location[0] -= astronaut.speed
    elif keys[pygame.K_RIGHT]:
        astronaut.frame = (astronaut.frame + 1) % 5
        astronaut.direction = "right"
        astronaut.location[0] += astronaut.speed
    elif keys[pygame.K_UP]:
        astronaut.frame = (astronaut.frame + 1) % 5
        astronaut.direction = "up"
        astronaut.location[1] -= astronaut.speed
    elif keys[pygame.K_DOWN]:
        astronaut.frame = (astronaut.frame + 1) % 5
        astronaut.direction = "down"
        astronaut.location[1] += astronaut.speed

    # Simple collision test
    if cockpit[int(player_to_grid_y), int(player_to_grid_x)] not in walkable_spaces:
        astronaut.location = old_location

    # Draw everything
    screen.blit(bg_image, (0, 0))
    #draw.draw_floor(screen, cockpit, room_offset)
    draw.draw_room(screen, cockpit, room_offset)
    draw.draw_player(screen, astronaut)
    #draw.draw_room(screen, cockpit, room_offset)
    # Update the screen
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()


