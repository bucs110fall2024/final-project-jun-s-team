import random
import pygame

class Blocks:

	FIGURES = {
		'I' : [[1, 5, 9, 13], [4, 5, 6, 7]],
        'Z' : [[4, 5, 9, 10], [2, 6, 5, 9]],
        'S' : [[6, 7, 9, 10], [1, 5, 6, 10]],
        'L' : [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        'J' : [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
        'T' : [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        'O' : [[1, 2, 5, 6]]
	}

	TYPES = ['I', 'Z', 'S', 'L', 'J', 'T', 'O']

	def __init__(self, x, y, type):
		self.x = x
		self.y = y
		self.type = type
		self.shape = self.FIGURES[type]
		self.color = random.randint(1, 4)
		self.rotation = 0

	def image(self):
		return self.shape[self.rotation]

	def rotate(self):
		self.rotation = (self.rotation + 1) % len(self.shape)
class IBlock(Blocks):
    def __init__(self, x=0, y=0):
        super().__init__(x, y, 'I')

class ZBlock(Blocks):
    def __init__(self, x=0, y=0):
        super().__init__(x, y, 'Z')

class SBlock(Blocks):
    def __init__(self, x=0, y=0):
        super().__init__(x, y, 'S')

class LBlock(Blocks):
    def __init__(self, x=0, y=0):
        super().__init__(x, y, 'L')

class JBlock(Blocks):
    def __init__(self, x=0, y=0):
        super().__init__(x, y, 'J')

class TBlock(Blocks):
    def __init__(self, x=0, y=0):
        super().__init__(x, y, 'T')

class OBlock(Blocks):
    def __init__(self, x=0, y=0):
        super().__init__(x, y, 'O')
