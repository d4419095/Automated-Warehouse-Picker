# Warehouse Automation AI

This project focuses on developing AI agents for optimizing tasks in a simulated warehouse environment.
It leverages reinforcement learning techniques to train agents for tasks like package picking and delivery.

## Project Structure

-   `envs/`: Contains the warehouse simulation environment(s).
    -   `grid_layout.py`: Defines the layout of the warehouse.
    -   `package_env_base.py`: Base class for package delivery environments.
    -   `package_env_multi.py`: Multi-agent/multi-package environment.
    -   `wrappers/`: Environment wrappers (e.g., for battery, curriculum).
    -   `renderers/`: Rendering utilities (ASCII, Pygame).
-   `rewards/`: Defines reward schemes for agents.
-   `agents/`: Contains agent implementations and factories (e.g., DQN, PPO).
    -   `callbacks.py`: Custom callbacks for training.
-   `planners/`: Pathfinding and planning algorithms (e.g., A*).
-   `data/`: Stores data like simulation logs and trained models.
-   `docs/`: Project documentation.
    -   `specs.md`: Environment specifications.
    -   `reward.md`: Details on reward functions.
    -   `actions.md`: Description of agent actions.
    -   `figures/`: Images and diagrams for documentation.
-   `train.py`: Script for training agents.
-   `evaluate.py`: Script for evaluating trained agents.
-   `benchmark.py`: Script for benchmarking agents.
-   `plots.py`: Utilities for plotting results.
-   `utils.py`: General utility functions.
-   `requirements.txt`: Python dependencies.

## Setup

(Instructions to be added)

## Usage

(Instructions to be added for training, evaluation, etc.)

## Contributing

(Guidelines for contributing to be added)
