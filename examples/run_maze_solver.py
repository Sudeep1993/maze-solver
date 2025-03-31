from maze_solver.maze_generator import generate_maze
from maze_solver.maze_solver import MazeSolver
from maze_solver.visualizer import visualize_maze_solution
import numpy as np

def main():
    # Generate a 20x20 maze
    width, height = 20, 20
    maze = generate_maze(width, height)
    
    # Preprocess maze (convert 0s to walls, 1s to paths)
    maze = np.where(maze == 0, 1, np.where(maze == 1, 0, maze))
    
    # Add start and goal points manually
    maze[1, 1] = 2  # Start point
    maze[-2, -2] = 3  # Goal point
    
    # Create and train the solver
    solver = MazeSolver(maze)
    solver.train(episodes=20000)
    
    # Solve and visualize the maze
    path = solver.solve_maze()
    visualize_maze_solution(maze, path)

if __name__ == "__main__":
    main()