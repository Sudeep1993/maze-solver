import numpy as np
import random

def generate_maze(width, height):
    """
    Generate a random maze using a recursive backtracking algorithm.
    
    Args:
        width (int): Width of the maze
        height (int): Height of the maze
    
    Returns:
        numpy.ndarray: 2D maze representation
    """
    maze = [[0] * (2 * width + 1) for _ in range(2 * height + 1)]
    
    def carve_passages(x, y):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height and maze[2 * ny + 1][2 * nx + 1] == 0:
                maze[2 * y + 1 + dy][2 * x + 1 + dx] = 1
                maze[2 * ny + 1][2 * nx + 1] = 1
                carve_passages(nx, ny)
                
    start_x, start_y = random.randint(0, width - 1), random.randint(0, height - 1)
    maze[2 * start_y + 1][2 * start_x + 1] = 1
    carve_passages(start_x, start_y)
    return np.array(maze)