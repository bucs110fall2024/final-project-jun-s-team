import pygame
import random


pygame.init()

screen = width, height = 300, 500
win = pygame.display.set_mode(screen, pygame.NOFRAME)

cellsize = 20
rows = (height-120) // cellsize
cols = width // cellsize

clock = pygame.time.Clock()
FPS = 24


img1 = pygame.image.load('Assets/1.png')
img2 = pygame.image.load('Assets/2.png')
img3 = pygame.image.load('Assets/3.png')
img4 = pygame.image.load('Assets/4.png')

Assets = {1 : img1,
	2 : img2,
	3 : img3,
	4 : img4}


font = pygame.font.Font('Fonts/Alternity-8w7J.ttf', 50)
font2 = pygame.font.SysFont('cursive', 25)


