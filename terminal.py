import pygame
from type_text import type_text
import textwrap


def terminal_game(screen, clock):
    x = 200
    y = 200
    black = (0, 0, 0) #RGB values
    text_color = (0, 255, 0)
    window = (150, 150, 500, 300)

    terminal_font = pygame.font.SysFont('courier', 16)
    welcome_message = terminal_font.render("SpaceLinux v 0.0.1 Copyright SpaceMine Inc.", True, text_color)
    puzzle_message = terminal_font.render("The Elusive answer lies within reach, do you See iT?", True, text_color)
    input_prompt = "Captain@Galactic-bridge$ "
    user_string = ""
    user_message = terminal_font.render(input_prompt+user_string, True, text_color)

    running = True
    computer_screen = pygame.Surface((x, y))
    while running:
        pygame.draw.rect(screen, black, window)
        screen.blit(welcome_message, (150, 150))
        screen.blit(puzzle_message, (150, 200))
        screen.blit(user_message, (160, 400))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                #running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_BACKSPACE:
                    user_string = user_string[:-1]

                else:
                    user_string += type_text(chr(event.key))

                    if user_string == "test":
                        running = False
                user_message = terminal_font.render(input_prompt + user_string, True, text_color)
                    # print(f"User string: {user_string}")
        # Look at all keys being pressed
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_q]:
        #     print("This is where we would quit")
        #     running = False
        clock.tick(10)

