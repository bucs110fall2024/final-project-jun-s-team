import pygame
from controller import *
from start_screen import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 800))  
    start_screen = StartScreen(screen)
    start_screen.run()
    game = Controller()
    game.run()

if __name__ == "__main__":
    main()

