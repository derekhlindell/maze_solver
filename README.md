# Maze Solver Project

## Overview

The Maze Solver is a depth-first algorithm, enhanced with a Tkinter interface, designed to navigate and solve a maze efficiently.

This is a semi-guided project from boot.dev

## Features

- Efficient pathfinding using a depth-first approach.
- Visual representation of maze cell navigation through a Tkinter-based GUI.
- Recursive algorithm to explore possible paths.
- Type hints for better code readability and validation.
- Comprehensive docstrings for ease of understanding and maintenance.
- Intuitive `__repr__` methods for key classes to aid in debugging and logging.

## Challenges

Conceptualizing the cartesian system for cell navigation was initially challenging. But through a lot of Pseudocode, and drawing out the graphs on paper allowed me to fully grasp the structure and implement the code for the algorithms.

## Skills Strengthened

- Algorithm design and implementation
- GUI development with Tkinter
- Writing maintainable, readable code with type hints and docstrings
- Designing intuitive representations of class instances with `__repr__`

## Usage

Run the `solve()` method in `main.py` to see the maze-solving algorithm in action through the Tkinter interface.

## Conclusion

This project was a great chance to test my knowledge on my recent gained knowledge of algorithms, specifically the depth-first search algorithm. It was great to do a project that demonstrates how an algorithm works visually.

I've worked with UI before in Houdini, but this was my first time writing something to this logical complexity with a GUI. It also reminded me of the times I've delved into graphics programming in the past, and I'm inspired to delve further via things like p5.js, and OpenGL.

The project also really helped me to further cement my understanding of how simple 2D render systems work by implementing an algorithm via code and representing it visually. Initially I struggled conceptualize how to use the Cartesian system for cell navigation, but through a lot of pseudocode and drawing out the graphs on paper, I was able to fully grasp the structure and implement the code for the algorithms.

In terms of code quality, I really wanted to focus on writing maintainable and readable code that can be easy to understand if someone needed to iterate on my current functionality. I used type hints, docstrings, and intuitive `__repr__` methods. I also used logging for tracking the program's state, which proved to be very useful for debugging and understanding the flow of the program.

If I were to continue working on this project, I'd make the UI more interactive, adding in buttons to modify the parameters of the Maze, implement a sprite system to turn the green solution line into a snake, and potentially create a side by side "race" game where a player could race the algorithm to see who can solve it faster.

My goals for this project were to demonstrate my coding ability, finish it within a single weekend, and create a program that is well-structured, clear and has features like type-hinting that allow for better Pythonic code. 

I was able to complete all of these goals, albeit at the expense of the visuals. However, it was a great mix of algorithm implementation, GUI development, and problem-solving.

I plan to use the experience I've learned from this project, to start learning PySide 2 to create standalone and embedded GUIs for DCCs like Houdini, Unreal Engine 5, and Autodesk Maya.
