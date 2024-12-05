from constants import *
import random
import pygame

class Tetromino:
    def __init__(self, shape):
        self.shape = shape
        self.color = COLORS[shape]
        self.blocks = SHAPES[shape]
        self.row = 0
        self.col = COLUMNS // 2

    def get_positions(self):
        return [(self.row + r, self.col + c) for r, c in self.blocks]

    def move(self, row_offset, col_offset):
        self.row += row_offset
        self.col += col_offset

    def rotate(self):
        self.blocks = [(-c, r) for r, c in self.blocks]

    def get_new_tetromino():
        return Tetromino(random.choice(list(SHAPES.keys())))
