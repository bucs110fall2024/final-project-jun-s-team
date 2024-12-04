import random
import pygame

class Blocks:
      self.Assets = {
            1: pygame.image.load('Assets/1.png'),
            2: pygame.image.load('Assets/2.png'),
            3: pygame.image.load('Assets/3.png'),
            4: pygame.image.load('Assets/4.png'),
        }
    
    FIGURES = {
        'I': [[1, 5, 9, 13], [4, 5, 6, 7]],
        'Z': [[4, 5, 9, 10], [2, 6, 5, 9]],
        'S': [[6, 7, 9, 10], [1, 5, 6, 10]],
        'L': [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        'J': [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
        'T': [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        'O': [[1, 2, 5, 6]]
    }
    Blocks = ['I', 'Z', 'S', 'L', 'J', 'T', 'O']
    
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = random.choice(self.Blocks)
        self.shape = self.FIGURES[self.type]
        self.color = random.randint(1, 4)
        self.rotation = 0

    def image(self):
        return self.shape[self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.shape)




