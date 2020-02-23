import pygame


class Player:
    def __init__(self, start_x, start_y):
        self.location = [start_x, start_y]
        self.frame = 0
        self.speed = 15
        self.direction = "down"
        self.sprite = {
            "left": [pygame.image.load("images/spacesuit_left.png"),
                     pygame.image.load("images/spacesuit_left_1.png"),
                     pygame.image.load("images/spacesuit_left_2.png"),
                     pygame.image.load("images/spacesuit_left_3.png"),
                     pygame.image.load("images/spacesuit_left_4.png")
                     ],
            "right": [pygame.image.load("images/spacesuit_right.png"),
                      pygame.image.load("images/spacesuit_right_1.png"),
                      pygame.image.load("images/spacesuit_right_2.png"),
                      pygame.image.load("images/spacesuit_right_3.png"),
                      pygame.image.load("images/spacesuit_right_4.png")
                      ],
            "up": [pygame.image.load("images/spacesuit_back.png"),
                   pygame.image.load("images/spacesuit_back_1.png"),
                   pygame.image.load("images/spacesuit_back_2.png"),
                   pygame.image.load("images/spacesuit_back_3.png"),
                   pygame.image.load("images/spacesuit_back_4.png")
                   ],
            "down": [pygame.image.load("images/spacesuit_front.png"),
                     pygame.image.load("images/spacesuit_front_1.png"),
                     pygame.image.load("images/spacesuit_front_2.png"),
                     pygame.image.load("images/spacesuit_front_3.png"),
                     pygame.image.load("images/spacesuit_front_4.png")
                     ]
        }
