import os

print(os.getcwd())

import pygame
import time

from constants import *
from tetromino import Tetromino
from grid import *



class Controller:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Tetris")
        self.grid = Grid()
        self.current_tetromino = Tetromino.get_new_tetromino()
        self.next_tetromino = Tetromino.get_new_tetromino()
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.running = True
        self.game_started = False
        self.fall_time = 0 
        self.fall_speed = 0.5  
    
               
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(FPS)
        self.display_game_over()
    
    def display_game_over(self):
        game_over_image = pygame.image.load("assets/game-over-7952252_1280.png")
        game_over_image = pygame.transform.scale(game_over_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.screen.blit(game_over_image, (0, 0))
        pygame.display.flip()
        
        while True:
            event = pygame.event.wait()  
            if event.type == pygame.QUIT:  
                pygame.quit()
                exit()
                
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.move_tetromino(0, -1)
                elif event.key == pygame.K_RIGHT:
                    self.move_tetromino(0, 1)
                elif event.key == pygame.K_DOWN:
                    self.move_tetromino(1, 0)
                elif event.key == pygame.K_UP:
                    self.rotate_tetromino()

    def update(self):
        current_time = time.time()
        if current_time - self.fall_time >= self.fall_speed:
            if not self.move_tetromino(1, 0):
                self.grid.add_tetromino(self.current_tetromino)
                cleared_lines = self.grid.clear_full_rows()
                self.score += cleared_lines * 100
                self.current_tetromino = self.next_tetromino
                self.next_tetromino = Tetromino.get_new_tetromino()
                if not self.grid.is_valid(self.next_tetromino.get_positions()):
                    self.running = False
                self.current_tetromino = self.next_tetromino
                self.next_tetromino = Tetromino.get_new_tetromino()
    
            self.fall_time = current_time
    
    def move_tetromino(self, row_offset, col_offset):
        self.current_tetromino.move(row_offset, col_offset)
        if not self.grid.is_valid(self.current_tetromino.get_positions()):
            self.current_tetromino.move(-row_offset, -col_offset)
            return False
        return True

    def rotate_tetromino(self):
        self.current_tetromino.rotate()
        if not self.grid.is_valid(self.current_tetromino.get_positions()):
            self.current_tetromino.rotate()  

    def draw(self):
        self.screen.fill(COLORS['BG'])
        self.grid.draw(self.screen)
        self.draw_tetromino(self.current_tetromino)
        self.draw_next_tetromino()
        self.draw_score()


 #needs fixing
    def draw_tetromino(self, tetromino):
        for r, c in tetromino.get_positions():
            if r >= 0:
                pygame.draw.rect(self.screen, tetromino.color, (c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def draw_next_tetromino(self):
        x_offset = GAME_WIDTH + 20  
        y_offset = 20
        for r, c in self.next_tetromino.blocks:
            pygame.draw.rect(self.screen, self.next_tetromino.color,
                             (x_offset + (c + 2) * 30, y_offset + (r + 2) * 30, 30, 30))

    def draw_score(self):
        score_text = self.font.render(f"Score: {self.score}", True, COLORS['TEXT'])
        self.screen.blit(score_text, (GAME_WIDTH + 20, GAME_HEIGHT - 60))
