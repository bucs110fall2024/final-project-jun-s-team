
:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# << Tetris-esque >>
## CS110 Final Project  << Fall, 2024 >>

## Team Members

<< Jun Zheng >>

***

## Project Description

<< I will be remaking Tetris, hopefully all the features from the classic game will be shown. Its a brick game that clear lines once the line is filled with bricks or tetrominos. >>

***    

## GUI Design

### Initial Design



### Final Design



## Program Design

### Features

1. << Start menu 1 >>
2. << rotateable and moveable bricks >>
3. << game over screen >>
4. << next brick is shown >>
5. << full line of bricks causes them to dissapear>>

### Classes

- tetromino.py
  - creates the classic tetris block shapes
- constants.py 
  - the variables i need, color, shapes, etc
-grid.py
  - create the grid for the background
- controller.py

## ATP

Test Case 1: Piece Movement
Test Description: Ensure pieces move left, right, and down in response to player input.
Test Steps:
- Step 1: Start Game
  - Press the left arrow key; verify the piece moves left.
  - Press the right arrow key; verify the piece moves right.
  - Tap the down arrow key; verify the piece goes downward.
  - **Expected Outcome**
    - Pieces move appropriately based on arrow inputs.

Test Case 2: Rotation
Test Description: Verify that pieces rotate properly when the rotate key is pressed.
Test Steps:
- Step 1: Start Game
  - Press the rotate key for the active piece.
  - Check each rotation state (e.g., 0°, 90°, 180°, 270°).
  - **Expected Outcome**
    - Pieces rotate as expected without overlaps or misalignment.

Test Case 3: Line Clearing
Test Description: Ensure that completed rows are detected and cleared correctly.
Test Steps:
- Step 1: Start Game
  - Fill a row with pieces.
  - Observe if the row disappears and points are awarded
  - Verify remaining blocks shift downward.
  - **Expected Outcome**
    - Full rows are cleared with score updates.

Test Case 4: Game Over Condition
Test Description: Confirm that the game ends when pieces stack beyond the grid’s top.
Test Steps:
- Step 1: Start Game
  - Allow pieces to stack until they exceed the grid's top.
  - Verify that the game ends and displays a "Game Over" png.
  - **Expected Outcome**
    - Game stops, and a "Game Over" message is displayed.

Test Case 5: Graphics and UI
Test Description: Ensure game graphics and score updates function correctly.
Test Steps:
- Step 1: Start Game
  - Monitor real-time piece movements and visual updates.
  - Verify score changes with each cleared row.
  - **Expected Outcome**
    - Graphics update smoothly, and the score reflects gameplay.

