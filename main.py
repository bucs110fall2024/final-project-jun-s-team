
import controller
import pygame
import random



import pygame
from sys import exit

# Constants for window dimensions and colors
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GRAY = (200, 200, 200)

def main():
    # General setup
    pygame.init()
    display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption('Tetris')

    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Display updates
        display_surface.fill(GRAY)

        # Update the game
        pygame.display.update()
        clock.tick(60)  # Limit to 60 FPS

# Entry point for the program
if __name__ == "__main__":
    main()

    #Create an instance on your controller object
    #Call your mainloop
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
