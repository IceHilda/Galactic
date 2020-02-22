import pygame
import numpy
import draw
from level_one import cockpit
pygame.init()

WIDTH = 800
HEIGHT = 600

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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ship_location[0] -= 10
            elif event.key == pygame.K_RIGHT:
                ship_location[0] += 10
            elif event.key == pygame.K_UP:
                ship_location[1] -= 10
            elif event.key == pygame.K_DOWN:
                ship_location[1] += 10


    screen.blit(bg_image, (0, 0))
    draw.draw_room(screen, cockpit, (100, 100))
    #screen.blit(planet_image, (50, 50))
    #screen.blit(ship_image, ship_location)
    pygame.display.flip()
    clock.tick(30)

pygame.quit()


