import os
import time
import random

WIDTH = 30
HEIGHT = 15
GENERATIONS = 50

INFECTION_PROBABILITY = 0.25
INFECTION_DURATION = 5
RECOVERY_RATE = 0.7
MORTALITY_RATE = 0.3

SUSCEPTIBLE = "S"
INFECTED = "I"
RECOVERED = "R"
DEAD = "D"

symbols = {
    SUSCEPTIBLE: "\033[94mS\033[0m",  # Azul
    INFECTED: "\033[91mI\033[0m",     # Vermelho
    RECOVERED: "\033[92mR\033[0m",    # Verde
    DEAD: "\033[90mD\033[0m",         # Cinza
}

def create_board():
    board = [[{"state": SUSCEPTIBLE, "time": 0} for _ in range(WIDTH)] for _ in range(HEIGHT)]
    board[HEIGHT // 2][WIDTH // 2] = {"state": INFECTED, "time": 0}
    return board

def has_infected_neighbor(board, x, y):
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < HEIGHT and 0 <= ny < WIDTH:
                if board[nx][ny]["state"] == INFECTED:
                    return True
    return False

def next_generation(board):
    new_board = [[cell.copy() for cell in row] for row in board]
    for x in range(HEIGHT):
        for y in range(WIDTH):
            cell = board[x][y]
            if cell["state"] == SUSCEPTIBLE:
                if has_infected_neighbor(board, x, y) and random.random() < INFECTION_PROBABILITY:
                    new_board[x][y] = {"state": INFECTED, "time": 0}
            elif cell["state"] == INFECTED:
                new_time = cell["time"] + 1
                if new_time >= INFECTION_DURATION:
                    if random.random() < RECOVERY_RATE:
                        new_board[x][y] = {"state": RECOVERED, "time": 0}
                    else:
                        new_board[x][y] = {"state": DEAD, "time": 0}
                else:
                    new_board[x][y]["time"] = new_time
    return new_board

def print_board(board):
    os.system("cls" if os.name == "nt" else "clear")
    for row in board:
        print("".join(symbols[cell["state"]] for cell in row))

def main():
    board = create_board()
    for generation in range(GENERATIONS):
        print(f"Geração {generation+1}")
        print_board(board)
        board = next_generation(board)
        time.sleep(0.3)

if __name__ == "__main__":
    main()
