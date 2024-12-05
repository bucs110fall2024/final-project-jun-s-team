import pygame
from constants import *

class Grid:
    def __init__(self):
        self.grid = [[None for _ in range(COLUMNS)] for _ in range(ROWS)]

    def add_tetromino(self, tetromino):
        for r, c in tetromino.get_positions():
            if r >= 0:
                self.grid[r][c] = tetromino.color

    def clear_full_rows(self):
        new_grid = [row for row in self.grid if any(cell is None for cell in row)]
        cleared = ROWS - len(new_grid)
        self.grid = [[None for _ in range(COLUMNS)] for _ in range(cleared)] + new_grid
        return cleared

    def is_valid(self, positions):
        return all(0 <= c < COLUMNS and r < ROWS and (r < 0 or self.grid[r][c] is None) for r, c in positions)

    def draw(self, screen):
        for r in range(ROWS):
            for c in range(COLUMNS):
                color = self.grid[r][c] if self.grid[r][c] else COLORS['GRID']
                pygame.draw.rect(screen, color, (c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                pygame.draw.rect(screen, COLORS['BG'], (c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)
