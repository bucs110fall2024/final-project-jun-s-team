from blocks import *
from colors import Colors
from grid import grid
import random 
import pygame

class Controller:
  def __init__(self):
	  self.grid = grid()
		self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
	  self.current_block = self.get_random_block()
		self.next_block = self.get_random_block()
		self.game_over = False
		self.score = 0
		
  def get_random_block(self):
		if len(self.blocks) == 0:
		self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
		block = random.choice(self.blocks)
		self.blocks.remove(block)
		return block
    
  def mainloop(self):
    #select state loop
    
  
  ### below are some sample loop states ###

  def menuloop(self):
    
      #event loop

      #update data

      #redraw
      
  def gameloop(self):
      #event loop

      #update data

      #redraw
    
  def gameoverloop(self):
      #event loop

      #update data

      #redraw
