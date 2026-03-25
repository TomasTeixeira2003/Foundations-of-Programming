# Meadow Ecosystem Simulation

## Overview
This project consists of a program that simulates the ecosystem of a meadow where animals coexist and interact. These animals can move, feed, reproduce, and die according to defined rules.

The simulation takes place in a meadow surrounded by mountains. Initially, some positions are occupied by animals—either predators or prey—while the remaining positions are empty or contain obstacles.

---

## Simulation Details
Animals in the ecosystem behave according to specific rules:

- **Movement** – Animals move across the meadow.
- **Feeding** – Predators hunt prey to survive.
- **Reproduction** – Animals reproduce based on defined conditions.
- **Death** – Animals may die due to starvation or other factors.

Different rules apply depending on whether the animal is a **predator** or a **prey**.

---

## Generations
The population evolves over discrete time steps called **generations**.  
Each generation represents a new state of the meadow after applying the simulation rules.

The simulation works by constructing successive generations of the population over time.

---

## Implementation
To build the simulator, the project defines:

- **Abstract Data Types (ADTs)** to represent the core entities (e.g., meadow, animals, positions)
- A set of **supporting functions** to implement the ecosystem rules and ensure correct simulation behavior

---

## Objective
The goal of this project is to correctly simulate the evolution of an ecosystem by applying the defined rules across multiple generations.
