from blocks import Blocks
import pygame

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
