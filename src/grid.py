import pygame
import random

class Grid:
    def __init__(self):
        pygame.init()
        self.width, self.height = 300, 500
        self.win = pygame.display.set_mode((self.width, self.height), pygame.NOFRAME)
        self.cellsize = 20
        self.rows = (self.height - 120) // self.cellsize
        self.cols = self.width // self.cellsize
        self.clock = pygame.time.Clock()
        self.FPS = 35

    def draw_grid(self):
        for row in range(self.rows):
            for col in range(self.cols):
                x = col * self.cellsize
                y = row * self.cellsize
                pygame.draw.rect(
                    self.win,
                    (40, 40, 40),  
                    (x, y, self.cellsize, self.cellsize),
                )

    def run(self):
        running = True
        while running:
            self.clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.win.fill((0, 0, 0)) 
            self.draw_grid()        
            pygame.display.update()

