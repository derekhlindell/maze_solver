# Maze Solver Project

## Overview

The Maze Solver is a depth-first algorithm, enhanced with a Tkinter interface, designed to navigate and solve a maze efficiently.

This is a semi-guided project from boot.dev

## Demo

<img src="https://github.com/derekhlindell/maze_solver/blob/main/maze_solver.gif" width="400" height="400"/>

## Goals

- Finish this project within a single weekend
- Create a program with Pythonic, clean, well-structured, and clear code.
- Includes features like type-hinting, docstrings, and `__repr__` methods.

## Features

- Efficient pathfinding using a depth-first approach.
- Visual representation of maze cell navigation through a Tkinter-based GUI.
- Recursive algorithm to explore possible paths.
- Type hints for better code readability and validation.
- Comprehensive docstrings for ease of understanding and maintenance.
- Intuitive `__repr__` methods for key classes to aid debugging and logging.

## Challenges

The project helped me to cement further my understanding of how simple 2D render systems work by implementing an algorithm via code and representing it visually. Initially, I struggled to conceptualize how to use the Cartesian system for cell navigation. Still, through a lot of pseudocode and drawing out the graphs on paper, I could fully grasp the structure and implement the code for the algorithms. I also used logging to track the program's state, which proved to be very useful for debugging and being able to grasp the flow of the program.

## Skills Strengthened

- Algorithm design and implementation
- GUI development with Tkinter
- Writing maintainable, readable code with type hints and docstrings
- Designing intuitive representations of class instances with `__repr__`

## Usage

Run the `solve()` method in `main.py` to see the maze-solving algorithm in action through the Tkinter interface.

## Conclusion

This project was a great chance to test my knowledge of my recent study of algorithms, specifically the depth-first search algorithm.

I've worked with UI before in Houdini, but this was my first time writing something to this logical complexity with a GUI. It also reminded me of the times I've tried a bit of graphics programming in the past, and I'm inspired to delve further using things like p5.js, and OpenGL.

I was able to complete all of the goals I set out for, albeit at the expense of the visuals. However, it was a great mix of algorithm implementation, GUI development, and problem-solving.

If I were to continue working on this project, I'd make the UI more interactive, adding buttons to modify the parameters of the Maze, implement a sprite system to turn the green solution line into a snake, and potentially create a side-by-side "race" game where a player could race the algorithm to see who can solve it faster.

I plan to use the experience I've learned from this project, to start learning PySide 2 to create standalone and embedded GUIs for DCCs like Houdini, Unreal Engine 5, and Autodesk Maya.
