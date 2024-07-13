# Monty Hall Simulation
This Python script simulates the Monty Hall problem and visualizes the results using matplotlib.

## Overview
The Monty Hall problem is a famous probability puzzle based on a game show scenario. In the game, there are three doors, behind one of which is a car, and behind the other two are goats. The player initially chooses a door, and then the host, who knows what's behind each door, reveals one of the other doors with a goat behind it. The player is then given the option to stick with their initial choice or switch to the other unopened door. Surprisingly, it's to the player's advantage to switch doors.

## Functionality
- The script monty_hall_simulation.py contains functions to simulate the generalized version of Monty Hall problem having n doors and k of them have cars behind them else has goats.
- It includes a function to perform the simulation with a specified number of trials, doors, and cars.
- The simulation calculates the probability of winning if the player sticks with their initial choice or switches doors.
- It also includes a function to plot a 3D surface showing the winning probability ratios for different numbers of doors and cars.
## Usage
1. Ensure you have Python installed on your system.
2. Install the required dependencies using pip install -r requirements.txt.
3. Run the script monty_hall_simulation.py.
4. The script will print the probabilities of winning with sticking and switching.
5. It will also generate a 3D surface plot illustrating the winning probability ratios for different configurations of doors and cars.
## Example
```bash
  python monty_hall_simulation.py
```
