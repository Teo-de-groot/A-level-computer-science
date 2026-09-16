import os
import sys
import random

# Configuration
WIDTH, HEIGHT = 40, 15
PLAYER, ENEMY, GOAL, EMPTY, WALL = "P", "E", "X", ".", "#"

def get_char():
    if os.name == 'nt':
        import msvcrt
        return msvcrt.getch().decode('utf-8').lower()
    else:
        import tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch.lower()

def generate_looping_map():
    # Start with a grid of walls
    grid = [[WALL for _ in range(WIDTH)] for _ in range(HEIGHT)]
    
    # Define four large interconnected rooms (quadrants)
    # Room format: (top, bottom, left, right)
    rooms = [
        (1, 6, 1, 18),   # Top Left
        (1, 6, 21, 38),  # Top Right
        (8, 13, 1, 18),  # Bottom Left
        (8, 13, 21, 38)  # Bottom Right
    ]
    
    for (t, b, l, r) in rooms:
        for y in range(t, b + 1):
            for x in range(l, r + 1):
                grid[y][x] = EMPTY

    # Create wide hallways to connect them into a giant circle
    # Horizontal hallways
    for x in range(15, 25):
        grid[3][x] = EMPTY
        grid[4][x] = EMPTY
        grid[10][x] = EMPTY
        grid[11][x] = EMPTY
    
    # Vertical hallways
    for y in range(5, 10):
        grid[y][8] = EMPTY
        grid[y][9] = EMPTY
        grid[y][30] = EMPTY
        grid[y][31] = EMPTY
        
    return grid

def can_move(grid, nx, ny):
    return 0 <= nx < WIDTH and 0 <= ny < HEIGHT and grid[ny][nx] != WALL

def move_enemy(ex, ey, px, py, grid):
    # Enemy calculates the best move to close the distance
    best_move = (ex, ey)
    min_dist = abs(ex - px) + abs(ey - py)
    
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = ex + dx, ey + dy
        if can_move(grid, nx, ny):
            d = abs(nx - px) + abs(ny - py)
            if d < min_dist:
                min_dist = d
                best_move = (nx, ny)
    return best_move

def draw(grid, px, py, ex, ey, gx, gy):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("RUN: Get to 'X' ")
    output = []
    for y in range(HEIGHT):
        row = ""
        for x in range(WIDTH):
            if x == px and y == py: row += PLAYER
            elif x == ex and y == ey: row += ENEMY
            elif x == gx and y == gy: row += GOAL
            else: row += grid[y][x]
        output.append(row)
    print("\n".join(output))

def main():
    grid = generate_looping_map()
    px, py = 2, 2
    gx, gy = WIDTH - 3, HEIGHT - 3
    ex, ey = WIDTH - 3, 2
    
    turn = 0
    while True:
        draw(grid, px, py, ex, ey, gx, gy)
        
        if px == gx and py == gy:
            print("\nVICTORY! You outmaneuvered the stalker.")
            break
        if px == ex and py == ey:
            print("\nCAUGHT! Use the rooms to circle around him.")
            break

        move = get_char()
        if move == 'q': break
        
        nx, ny = px, py
        if move == 'w': ny -= 1
        elif move == 's': ny += 1
        elif move == 'a': nx -= 1
        elif move == 'd': nx += 1
        
        if can_move(grid, nx, ny):
            px, py = nx, ny
            turn += 1
            # Enemy moves every 2nd turn to ensure you can outrun it
            if turn % 2 == 0:
                ex, ey = move_enemy(ex, ey, px, py, grid)

if __name__ == "__main__":
    main()