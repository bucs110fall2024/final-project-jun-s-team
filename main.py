
import pygame
from src.final_project.game import *
from final_project.constants import Score
from final_project.grid import Preview

class Main:
	def __init__(self):

		# general 
		pygame.init()
		self.display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
		self.clock = pygame.time.Clock()
		pygame.display.set_caption('Tetris')

		self.game = Game()
		self.score = Score()
		self.preview = Preview()
		
	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					exit()

			# display 
			self.display_surface.fill(GRAY)
			
			self.game.run()
			self.score.run()
			self.preview.run()

			# updating the game
			pygame.display.update()
	
        		
if __name__ == '__main__':
	main = Main()
	main.run()
