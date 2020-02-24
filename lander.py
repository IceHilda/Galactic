import pygame

pygame.init()

# Pygame screen parameters
WIDTH = 800
HEIGHT = 600
FPS = 24  # Updates per second

pad_location = 300
x_speed = 0
y_speed = 0
fuel = 100
thrust = -2
gravity = 0.5

screen = pygame.display.set_mode((WIDTH, HEIGHT))
ground_image = pygame.image.load("images/soil.png")
pad_image = pygame.image.load("images/floor_pad.png")
ship_image = pygame.image.load("images/rescue_ship.png")
exhaust_image = pygame.image.load("images/exhaust.png")
exhaust_image = pygame.transform.scale(exhaust_image, (40, 20))
ship_image = pygame.transform.scale(ship_image, (40, 90))
arial = pygame.font.SysFont('arial', 14)

ship_location = [WIDTH/2 - ship_image.get_width()/2, 0]

pygame.display.set_caption("Lunar Lander")
running = True
clock = pygame.time.Clock()


while running:
    # Draw everything
    screen.fill((10, 10, 10))
    pygame.draw.rect(screen, (150, 100, 100), (0, HEIGHT-30, 800, 30))
    screen.blit(pad_image, (pad_location, 570))
    screen.blit(pad_image, (pad_location + 30, 570))
    screen.blit(ship_image, ship_location)

    # Draw stats
    fuel_text = arial.render("FUEL  " + str(fuel), True, (255, 255, 255,))
    speed_text = arial.render("SPEED  " + str(round(y_speed)), True, (255, 255, 255,))
    screen.blit(fuel_text, (WIDTH - 60, 0))
    screen.blit(speed_text, (WIDTH - 60, 20))

    # Check for end conditions
    # At or below baseline
    if ship_location[1] + ship_image.get_height() >= HEIGHT-30:
        if y_speed > 10 or x_speed > 5:
            print("lose")
        elif ship_location[0] < pad_location or ship_location[0] > pad_location + 60:
            print("lose")
        else:
            print("win")
        pygame.time.wait(500)
        running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Test for key inputs
    keys = pygame.key.get_pressed()
    if fuel > 0:
        if keys[pygame.K_LEFT]:
            x_speed += 0.25 * thrust
            fuel -= 0.25 * 1
        elif keys[pygame.K_RIGHT]:
            x_speed -= 0.25 * thrust
            fuel -= 0.25 * 1
        elif keys[pygame.K_UP]:
            y_speed += thrust
            fuel -= 1
            screen.blit(exhaust_image, (ship_location[0], ship_location[1] + ship_image.get_height()))

    # Process gravity
    y_speed += gravity

    # Move location
    ship_location[0] += x_speed
    ship_location[1] += y_speed

    # Update the screen
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
