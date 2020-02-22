import numpy as np
import pygame


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
    map_to_image = [floor_image, wall_image, wall_image_transparent]

    # 0 = floor, 1 = wall (pillar)
    for tile_type in [0, 1, 2]:
        the_rows, the_cols = np.where(grid == tile_type)
        for i in range(len(the_cols)):
            screen.blit(map_to_image[tile_type], (the_cols[i] * 30 + start_location[0],
                                                  the_rows[i] * 30 + start_location[1]))
