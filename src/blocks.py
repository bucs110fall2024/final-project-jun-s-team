import random
import pygame
from colors import Colors

pygame.init()

class Blocks:
    # Load Assets
    assets = {
        1: pygame.image.load('assets/blue.png'),
        2: pygame.image.load('assets/green.png'),
        3: pygame.image.load('assets/red.png'),
        4: pygame.image.load('assets/pink.png'),
    }

    # Define Shapes
    Shapes = {
        'I': [[1, 5, 9, 13], [4, 5, 6, 7]],
        'Z': [[4, 5, 9, 10], [2, 6, 5, 9]],
        'S': [[6, 7, 9, 10], [1, 5, 6, 10]],
        'L': [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        'J': [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
        'T': [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        'O': [[1, 2, 5, 6]]
    }

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = random.choice(list(Blocks.Shapes.keys()))
        self.shape = Blocks.Shapes[self.type]
        self.color = random.randint(1, 4)
        self.orientation = 0

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.shape)

    def current_positions(self):
        return self.shape[self.rotation]

font = pygame.font.SysFont("verdana", 50)
font2 = pygame.font.SysFont("verdana", 15)

