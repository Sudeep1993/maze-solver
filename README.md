Q-Learning Maze Solver
Overview
This project implements a maze solver using Q-Learning, a reinforcement learning technique. The solver can generate random mazes, train an agent to find the optimal path, and visualize the solution.
Features

Random maze generation
Q-Learning based pathfinding
Visualization of maze and solution path
Configurable learning parameters

Installation
Prerequisites

Python 3.7+
pip

Install from PyPI
bashCopypip install maze-solver
Clone and Install
bashCopygit clone https://github.com/Sudeep1993/maze-solver.git
cd maze-solver
pip install -r requirements.txt
python setup.py install
Usage
Generate and Solve a Maze
pythonCopyfrom maze_solver.maze_generator import generate_maze
from maze_solver.maze_solver import MazeSolver

# Generate a 20x20 maze
maze = generate_maze(20, 20)

# Create a solver
solver = MazeSolver(maze)

# Train the solver
solver.train(episodes=20000)

# Visualize the solution
solver.visualize_solution()
Customization
You can customize the Q-Learning parameters:

learning_rate: Controls how much new information overrides old information
discount_factor: Determines the importance of future rewards
exploration_rate: Balances exploration vs exploitation

Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
License
This project is licensed under the MIT License.
