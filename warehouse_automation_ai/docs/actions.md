# Action Space Definition

This document describes the actions available to agents operating within the warehouse environment.

## Discrete Actions

The environment typically uses a discrete action space. The available actions might include:

1.  **Move North (0):** Move one cell up.
2.  **Move East (1):** Move one cell right.
3.  **Move South (2):** Move one cell down.
4.  **Move West (3):** Move one cell left.
5.  **Pickup (4):** If at a package location and capacity allows, pick up the package.
6.  **Dropoff (5):** If at a docking station and carrying a package for that station, drop off the package.
7.  **Wait/Stay (6):** Remain in the current cell for one time step.

*(Note: The exact integer mapping and availability of actions might vary based on the specific environment configuration or agent capabilities, e.g., single vs. multi-agent, specific robot skills.)*

## Action Masks

In some scenarios, action masking might be used to invalidate actions that are not currently possible (e.g., moving into a wall, picking up when no package is present).

## Continuous Actions (Future Consideration)

While current implementations focus on discrete actions, future extensions might explore continuous action spaces for more nuanced control (e.g., velocity, steering angle for robots).
