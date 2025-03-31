import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def visualize_maze_solution(maze, path):
    """
    Visualize the maze and solution path.
    
    Args:
        maze (numpy.ndarray): 2D maze representation
        path (list): Solution path coordinates
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    fig.suptitle('Maze Solver: Environment vs. Path')

    # Define colors for the maze
    colors = ['white', 'black', 'white', 'white', 'green', 'red', 'blue']
    cmap = mcolors.ListedColormap(colors)
    bounds = [0, 1, 2, 3, 4, 5, 6, 7]
    norm = mcolors.BoundaryNorm(bounds, cmap.N)

    # Normal maze plot
    maze_plot = maze.copy()
    maze_plot = np.where(maze_plot == 2, 5, maze_plot)  
    maze_plot = np.where(maze_plot == 3, 6, maze_plot)  
    ax1.imshow(maze_plot, cmap=cmap, norm=norm)
    ax1.set_title('Maze Environment')
    ax1.grid(False)

    # Solution path plot
    solved_maze = maze.copy()
    for row, col in path:
        if solved_maze[row, col] == 0:  
            solved_maze[row, col] = 4  

    solved_maze = np.where(solved_maze == 2, 5, solved_maze)  
    solved_maze = np.where(solved_maze == 3, 6, solved_maze)  
    ax2.imshow(solved_maze, cmap=cmap, norm=norm)
    ax2.set_title('Solved Path')

    plt.show()