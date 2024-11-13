import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Constants for the game
WINDOW_SIZE = 300
GRID_SIZE = 3
CELL_SIZE = WINDOW_SIZE // GRID_SIZE
WHITE = (255, 255, 255)
LINE_COLOR = (0, 0, 0)
LINE_WIDTH = 10
FONT_SIZE = 50
FONT = pygame.font.Font(None, FONT_SIZE)

# Create the game window
window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Tic-Tac-Toe")

# Create the game board using NumPy
board = np.full((GRID_SIZE, GRID_SIZE), "")

# Function to draw the grid lines
def draw_grid():
    for i in range(1, GRID_SIZE):
        pygame.draw.line(window, LINE_COLOR, (0, i * CELL_SIZE), (WINDOW_SIZE, i * CELL_SIZE))
        pygame.draw.line(window, LINE_COLOR, (i * CELL_SIZE, 0), (i * CELL_SIZE, WINDOW_SIZE))

# Function to check for a win
def check_win(player):
    return (
        any(np.all(board == player, axis=0)) or
        any(np.all(board == player, axis=1)) or
        np.all(np.diag(board) == player) or
        np.all(np.diag(np.fliplr(board)) == player)
    )

# Main game loop
current_player = "X"
game_over = False
winner = None

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEBUTTONDOWN and not check_win("X") and not check_win("O"):
            row = event.pos[1] // CELL_SIZE
            col = event.pos[0] // CELL_SIZE
            if board[row, col] == "":
                board[row, col] = current_player
                current_player = "O" if current_player == "X" else "X"

    window.fill(WHITE)
    draw_grid()

    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if board[row, col] != "":
                text = FONT.render(board[row, col], True, LINE_COLOR)
                text_rect = text.get_rect(center=(col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2))
                window.blit(text, text_rect)

    if check_win("X"):
        game_over = True
        winner = "X"
    elif check_win("O"):
        game_over = True
        winner = "O"
    elif np.all(board != ""):
        game_over = True
        winner = "Tie"

    pygame.display.flip()

if winner == "Tie":
    print("It's a tie!")
else:
    print("Player {} wins!".format(winner))

pygame.display.flip()

# Wait for 10 seconds
pygame.time.wait(5000)

pygame.quit()
