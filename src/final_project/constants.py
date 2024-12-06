
COLUMNS, ROWS = 10, 20
CELL_SIZE = 40
GAME_WIDTH, GAME_HEIGHT = COLUMNS * CELL_SIZE, ROWS * CELL_SIZE
SIDEBAR_WIDTH = 200
WINDOW_WIDTH, WINDOW_HEIGHT = GAME_WIDTH + SIDEBAR_WIDTH, GAME_HEIGHT
FPS = 10


COLORS = {
    'T': (255, 0, 255),  # Pink
    'O': (255, 255, 0),  # Yellow
    'J': (0, 0, 255),    # Blue
    'L': (255, 165, 0),  # Orange
    'I': (0, 255, 255),  # Cyan
    'S': (0, 255, 0),    # Green
    'Z': (255, 0, 0),    # Red
    'GRID': (255, 255, 255),
    'BG': (0, 0, 0),
    'TEXT': (255, 255, 255)
}


SHAPES = {
    'T': [(0, 0), (-1, 0), (1, 0), (0, -1)],
    'O': [(0, 0), (0, -1), (1, 0), (1, -1)],
    'J': [(0, 0), (0, -1), (0, 1), (-1, 1)],
    'L': [(0, 0), (0, -1), (0, 1), (1, 1)],
    'I': [(0, 0), (0, -1), (0, -2), (0, 1)],
    'S': [(0, 0), (-1, 0), (0, -1), (1, -1)],
    'Z': [(0, 0), (1, 0), (0, -1), (-1, -1)]
}


