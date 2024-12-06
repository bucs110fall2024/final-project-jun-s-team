import pygame
import pygame_gui
from constants import *

class StartScreen:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.manager = pygame_gui.UIManager((WINDOW_WIDTH, WINDOW_HEIGHT), 'theme.json')
        self.running = True
        self.create_ui()

    def create_ui(self):
        # Title Label
        self.title_label = pygame_gui.elements.UITextBox(
            html_text="<bigger>TETRIS</bigger>",
            relative_rect=pygame.Rect(0, WINDOW_HEIGHT // 4, WINDOW_WIDTH, 150 ),
            manager=self.manager,
            object_id="title_label"
        )

        # Start Button
        self.start_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT // 2 + 100), (200, 50)),
            text="Start",
            manager=self.manager,
            object_id="start_button"
        )

        # Instructions Label
        self.instructions_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((WINDOW_WIDTH // 2 - 150, WINDOW_HEIGHT // 2 + 200), (300, 50)),
            text="Press Start to Begin!",
            manager=self.manager,
            object_id="instructions_label"
        )

    def run(self):
        while self.running:
            time_delta = self.clock.tick(60) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED and event.ui_element == self.start_button:
                        print("Start Button Clicked")
                        self.running = False

                self.manager.process_events(event)

            self.manager.update(time_delta)
            self.screen.fill(COLORS['BG'])  # Replace with the actual background color
            self.manager.draw_ui(self.screen)
            pygame.display.flip()
