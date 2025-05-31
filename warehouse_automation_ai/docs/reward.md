# Reward Function Design

This document details the reward schemes used for training reinforcement learning agents in the warehouse environment.

## Base Scheme (`rewards/base_scheme.py`)

-   **Step Penalty:** A small negative reward for each time step to encourage efficiency.
    -   `step_penalty()`
-   **Pickup Bonus:** A positive reward when an agent successfully picks up a package.
    -   `pickup_bonus()`

## Single Robot Reward (`rewards/single_robot.py`)

-   `compute(prev_obs, obs, done, info) -> float`
    -   (Details on how the reward is calculated for a single robot scenario, likely incorporating elements from the base scheme and task-specific bonuses/penalties like delivery bonus, collision penalty, etc.)

## Multi-Robot Reward (`rewards/multi_robot.py`)

-   `compute(prev_obs, obs, done, info) -> float`
    -   (Details on how the reward is calculated for a multi-robot scenario. This might involve considerations for cooperative behavior, collision avoidance between robots, and fair distribution of rewards or team-based rewards.)

## Considerations

-   **Sparse vs. Dense Rewards:** Discussion on the choice of reward density.
-   **Reward Shaping:** Techniques used to guide learning.
-   **Hyperparameter Tuning:** How reward magnitudes are balanced.
