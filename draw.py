import numpy as np
import pygame


def draw_floor(screen, grid, start_location):
    """
    Given an existing pygame screen and a level (grid), plot the contents onto the screen using room images.
    :param screen: An initiated pygame screen
    :param grid: A 2D numpy array
    :param start_location: (x,y) The offset (in pixels) to begin drawing from
    :return:
    """
    floor_image = pygame.image.load("images/floor.png")
    # better tile management for multiple environments / create multiple environments.
    # 0 = floor, 1 = wall (pillar)
    max_dimensions = grid.shape
    for r in range(max_dimensions[0]):
        for c in range(max_dimensions[1]):
            screen.blit(floor_image, (c * 30 + start_location[0],
                                      r * 30 + start_location[1]))


def draw_room(screen, grid, start_location):
    """
    Given an existing pygame screen and a level (grid), plot the contents onto the screen using room images.
    :param screen: An initiated pygame screen
    :param grid: A 2D numpy array
    :param start_location: (x,y) The offset (in pixels) to begin drawing from
    :return:
    """
    wall_image = pygame.image.load("images/pillar.png")
    wall_image_transparent = pygame.image.load("images/pillar_80.png")
    floor_image = pygame.image.load("images/floor.png")
    computer_image = pygame.image.load("images/desk_computer.png")

    # map_to_image = [floor_image,  # 0
    #                 wall_image,   # 1
    #                 wall_image_transparent,  # 2
    #                 computer_image]  # 3
    map_to_image = {
        "0": floor_image,
        "1": wall_image,
        "2": wall_image_transparent,
        "3": computer_image,
        "10": wall_image  # Secret passage
    }
    # better tile management for multiple environments / create multiple environments.
    # 0 = floor, 1 = wall (pillar)
    # First draw floor everywhere
    max_dimensions = grid.shape
    for r in range(max_dimensions[0]):
        for c in range(max_dimensions[1]):
            screen.blit(floor_image, (c * 30 + start_location[0],
                                      r * 30 + start_location[1]))

    for tile_type in [1, 2, 3, 10]:
        the_rows, the_cols = np.where(grid == tile_type)
        for i in range(len(the_cols)):
            screen.blit(map_to_image[str(tile_type)], (the_cols[i] * 30 + start_location[0],
                                                       the_rows[i] * 30 + start_location[1]))


def draw_player(screen, spaceman):
    offset_x = 0
    offset_y = 15

    image_to_draw = spaceman.sprite[spaceman.direction][spaceman.frame]
    adjusted_location = (spaceman.location[0] + offset_x, spaceman.location[1] + offset_y)
    screen.blit(image_to_draw, adjusted_location)
