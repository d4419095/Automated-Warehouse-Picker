# Environment Specifications

This document outlines the specifications for the warehouse simulation environments.

## Observation Space

(Details about the observation space for agents - e.g., grid features, robot state, package locations)

## Action Space

(Details about the available actions for agents - e.g., move, pick up, drop off)

## Dynamics

(How the environment changes based on agent actions - e.g., robot movement, package state changes)

## Termination Conditions

(Conditions under which an episode ends - e.g., all packages delivered, timeout, robot out of battery)

## Initial State

(How the environment is initialized at the start of an episode)

## Grid Resolution

The simulation grid uses a cell size of 1 meter x 1 meter.

This resolution was chosen because:
- It's a realistic dimension for the operational space of Kiva-style warehouse robots, allowing for clear pathways and maneuverability.
- It simplifies calculations for distance, speed, and area without losing essential detail for pathfinding and layout planning.
- It provides a good balance between simulation granularity and computational efficiency. Robots can be considered to occupy a single cell at any given time, and their movement from one cell to another represents a 1-meter step.
