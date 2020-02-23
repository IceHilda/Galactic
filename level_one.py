import pygame
import numpy as np

#pygame.init()

cockpit = np.zeros((14, 22))
cockpit[0, :] = 1
cockpit[-1, :] = 2
cockpit[:, 0] = 1
cockpit[:, -1] = 1

cockpit[3, 4] = 3
cockpit[3, 5] = 99
cockpit[0, 20] = 10
