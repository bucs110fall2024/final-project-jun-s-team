from game import *

class Preview:
	def __init__(self):
		
		# general
		self.display_surface = pygame.display.get_surface()
		self.surface = pygame.Surface((SIDEBAR_WIDTH, GAME_HEIGHT * PREVIEW_HEIGHT_FRACTION))
		self.rect = self.surface.get_rect(topright = (WINDOW_WIDTH - PADDING,PADDING))
	def run(self):
		self.surface.fill(GRAY)
		self.display_surface.blit(self.surface, self.rect)
		pygame.draw.rect(self.display_surface, LINE_COLOR, self.rect, 2, 2)
