import pygame
import random

class TetrisGame:
    def __init__(self):
        pygame.init()

        self.width, self.height = 300, 500
        self.win = pygame.display.set_mode((self.width, self.height), pygame.NOFRAME)

        self.cellsize = 20
        self.rows = (self.height - 120) // self.cellsize
        self.cols = self.width // self.cellsize

        self.clock = pygame.time.Clock()
        self.FPS = 24

        self.Assets = {
            1: pygame.image.load('Assets/1.png'),
            2: pygame.image.load('Assets/2.png'),
            3: pygame.image.load('Assets/3.png'),
            4: pygame.image.load('Assets/4.png'),
        }
    
        self.font = pygame.font.Font('Fonts/Alternity-8w7J.ttf', 50)
        self.font2 = pygame.font.SysFont('cursive', 25)
    def run(self):
        running = True
        while running:
            self.clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.win.fill((0, 0, 0))  
            pygame.display.update()

