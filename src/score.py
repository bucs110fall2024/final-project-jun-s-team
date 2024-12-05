import pygame
from game import *

class Score: 
    def __init__(self):
        self.surface = pygame.Surface((SIDEBAR_WIDTH,GAME_HEIGHT * SCORE_HEIGHT_FRACTION - PADDING))
        self.rect = self.surface.get_rect(bottomright = (WINDOW_WIDTH - PADDING,WINDOW_HEIGHT - PADDING))
        self.display_surface = pygame.display.get_surface()
    
    def run(self): 
        self.surface.fill(GRAY)
        self.display_surface.blit(self.surface,self.rect)
        pygame.draw.rect(self.display_surface, LINE_COLOR, self.rect, 2, 2)
