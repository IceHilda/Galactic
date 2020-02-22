import pygame
import numpy
from player import Player
import draw
from level_one import cockpit
pygame.init()

WIDTH = 800
HEIGHT = 600

astronaut = Player(130, 150)
planet_image = pygame.image.load("images/mars.png")
ship_image = pygame.image.load("images/ship.png")
bg_image = pygame.image.load("images/backdrop.jpg")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space the Final Frontier")
running = True
clock = pygame.time.Clock()
#pygame.

ship_location = [130, 150]

while running:

    #check user input

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # elif event.type == pygame.KEYDOWN:
        #     astronaut.frame = (astronaut.frame+1) % 5
        #     if event.key == pygame.K_LEFT:
        #         astronaut.direction = "left"
        #         astronaut.location[0] -= astronaut.speed
        #     elif event.key == pygame.K_RIGHT:
        #         astronaut.direction = "right"
        #         astronaut.location[0] += astronaut.speed
        #     elif event.key == pygame.K_UP:
        #         astronaut.direction = "up"
        #         astronaut.location[1] -= astronaut.speed
        #     elif event.key == pygame.K_DOWN:
        #         astronaut.direction = "down"
        #         astronaut.location[1] += astronaut.speed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        astronaut.frame = (astronaut.frame + 1) % 5
        astronaut.direction = "left"
        astronaut.location[0] -= astronaut.speed
    if keys[pygame.K_RIGHT]:
        astronaut.frame = (astronaut.frame + 1) % 5
        astronaut.direction = "right"
        astronaut.location[0] += astronaut.speed
    if keys[pygame.K_UP]:
        astronaut.frame = (astronaut.frame + 1) % 5
        astronaut.direction = "up"
        astronaut.location[1] -= astronaut.speed
    if keys[pygame.K_DOWN]:
        astronaut.frame = (astronaut.frame + 1) % 5
        astronaut.direction = "down"
        astronaut.location[1] += astronaut.speed

    screen.blit(bg_image, (0, 0))
    draw.draw_room(screen, cockpit, (100, 100))
    draw.draw_player(screen, astronaut)
    #screen.blit(planet_image, (50, 50))
    #screen.blit(ship_image, ship_location)
    pygame.display.flip()
    clock.tick(10)

pygame.quit()


