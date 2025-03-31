import numpy as np
import random

class MazeSolver:
    def __init__(self, maze, learning_rate=0.1, discount_factor=0.9, 
                 exploration_rate=1.0, min_exploration_rate=0.01, exploration_decay=0.995):
        """
        Initialize the Maze Solver using Q-Learning
        
        Args:
            maze (numpy.ndarray): 2D maze representation
            learning_rate (float): Rate at which the agent learns
            discount_factor (float): Importance of future rewards
            exploration_rate (float): Probability of random exploration
            min_exploration_rate (float): Minimum exploration probability
            exploration_decay (float): Rate of exploration decay
        """
        self.maze = maze
        self.rows, self.cols = maze.shape
        
        # Q-learning hyperparameters
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.min_exploration_rate = min_exploration_rate
        self.exploration_decay = exploration_decay
        
        # Find start and goal positions
        start_positions = np.where(maze == 2)
        goal_positions = np.where(maze == 3)
        
        if len(start_positions[0]) == 0 or len(goal_positions[0]) == 0:
            raise ValueError("Maze must contain exactly one start (2) and one goal (3) position")
        
        self.start_pos = (start_positions[0][0], start_positions[1][0])
        self.goal_pos = (goal_positions[0][0], goal_positions[1][0])
        
        # Initialize Q-table
        self.q_table = np.zeros((self.rows, self.cols, 4))
        
        # Possible actions: Up, Right, Down, Left
        self.actions = [
            (-1, 0),  # Up
            (0, 1),   # Right
            (1, 0),   # Down
            (0, -1)   # Left
        ]

    def is_valid_move(self, pos):
        """Check if a move is valid within the maze."""
        row, col = pos
        return (0 <= row < self.rows and 
                0 <= col < self.cols and 
                self.maze[row, col] != 1)

    def choose_action(self, state):
        """Choose an action based on exploration/exploitation strategy."""
        if random.uniform(0, 1) < self.exploration_rate:
            return random.randint(0, 3)
        else:
            return np.argmax(self.q_table[state[0], state[1]])

    def get_next_state(self, state, action):
        """Get the next state based on current state and chosen action."""
        row, col = state
        d_row, d_col = self.actions[action]
        next_state = (row + d_row, col + d_col)
        return next_state if self.is_valid_move(next_state) else state

    def get_reward(self, state):
        """Compute reward for a given state."""
        if state == self.goal_pos:
            return 100  
        elif not self.is_valid_move(state):
            return -10  
        return -1  

    def train(self, episodes=1000):
        """
        Train the Q-learning agent.
        
        Args:
            episodes (int): Number of training episodes
        """
        for episode in range(episodes):
            current_state = self.start_pos
            done = False

            while not done:
                action = self.choose_action(current_state)
                next_state = self.get_next_state(current_state, action)
                reward = self.get_reward(next_state)

                current_q = self.q_table[current_state[0], current_state[1], action]
                max_next_q = np.max(self.q_table[next_state[0], next_state[1]])
                new_q = current_q + self.learning_rate * (reward + self.discount_factor * max_next_q - current_q)
                self.q_table[current_state[0], current_state[1], action] = new_q

                current_state = next_state
                if current_state == self.goal_pos:
                    done = True

            # Decay exploration rate
            self.exploration_rate = max(self.min_exploration_rate, self.exploration_rate * self.exploration_decay)

    def solve_maze(self):
        """
        Find the path from start to goal using learned Q-table.
        
        Returns:
            list: Path from start to goal
        """
        path = [self.start_pos]
        current_state = self.start_pos

        while current_state != self.goal_pos:
            action = np.argmax(self.q_table[current_state[0], current_state[1]])
            next_state = self.get_next_state(current_state, action)

            if next_state in path:
                break

            path.append(next_state)
            current_state = next_state

        return path