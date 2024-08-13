from graphics import Window
from cell import Cell

import time
import random

import logging

logger = logging.getLogger(__name__)


ANIMATION_DELAY = 0.01  # Delay between animation frames in seconds


class Maze:
    def __init__(
        self,
        x1: int,
        y1: int,
        num_cols: int,
        num_rows: int,
        cell_size_x: int,
        cell_size_y: int,
        win: Window = None,
        seed: int = None,
    ) -> None:
        """
        Initialize a Maze with the specified parameters.

        The x1 and y1 parameters represent the top-left corner of the maze.
        The num_cols and num_rows parameters represent the number of columns and rows in the maze.
        The cell_size_x and cell_size_y parameters represent the width and height of each cell in the maze.
        The win parameter is the Window object where the maze will be drawn.
        The seed parameter is used to initialize the random number generator for maze creation, set this to a set number for debugging.
        """
        self.x1 = x1
        self.y1 = y1
        self.num_cols = num_cols
        self.num_rows = num_rows
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.seed = seed
        self._cells: list[Cell] = []

        logging.info("=== Creating the Maze ===")
        self._create_cells()

        logging.info(" Breaking entrance and exit cells of maze")
        self._break_entrance_and_exit()

        if (
            self.seed is not None
        ):  # If we don't have a seed set the generation will always be random
            self.seed = random.seed(seed)

        logging.info(" Breaking walls to create maze")
        self._break_walls_r(0, 0)

        logging.info(" Resetting cells visited value to False")
        self._reset_cells_visited()

    def __repr__(self):
        return f"""Maze(
                _cells={self._cells!r},
                x1={self.x1!r},
                y1={self.y1!r},
                num_cols={self.num_cols!r},
                num_rows={self.num_rows!r},
                cell_size_x={self.cell_size_x!r}, 
                cell_size_y={self.cell_size_y!r},
                win={self.win!r},
                seed={self.seed!r}
            )"""

    def _create_cells(self) -> None:
        """Creates a nested list of Cells based on num_cols and num_rows and draws each Cell."""
        for col in range(self.num_cols):
            current_col = []
            for row in range(self.num_rows):
                current_col.append(Cell(self.win))
            self._cells.append(current_col)

        for col in range(self.num_cols):
            for row in range(self.num_rows):
                self._draw_cell(col, row)

    def _draw_cell(self, i: int, j: int) -> None:
        """Draws a cell based on the input (i, j) coordinates"""
        if self.win is None:
            return

        maze_corner_x, maze_corner_y = self.x1, self.y1

        cell_top_left_x = maze_corner_x + (self.cell_size_x * i)
        cell_top_left_y = maze_corner_y + (self.cell_size_y * j)
        cell_bottom_right_x = cell_top_left_x + self.cell_size_x
        cell_bottom_right_y = cell_top_left_y + self.cell_size_y

        self._cells[i][j].draw(
            cell_top_left_x, cell_top_left_y, cell_bottom_right_x, cell_bottom_right_y
        )
        self._animate()

    def _animate(self) -> None:
        """Redraw the window and delay for a short time to 'animate'."""
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(ANIMATION_DELAY)

    def _break_entrance_and_exit(self) -> None:
        """Breaks the first and last cells in the maze to create an entrance and exit."""
        first_cell = self._cells[0][0]
        last_cell = self._cells[-1][-1]
        first_cell.has_left_wall = False
        self._draw_cell(0, 0)
        last_cell.has_right_wall = False
        self._draw_cell(len(self._cells) - 1, len(self._cells) - 1)

    def _check_valid_cells(
        self, current_cell: Cell, i: int, j: int, check_walls: bool = False
    ) -> list[tuple]:
        """
        Check each adjacent cell if they haven't been visited.
        if check_walls is on, check if there are any walls in the way.
        """
        valid_cell_coords = []

        # check left
        if i - 1 >= 0 and not self._cells[i - 1][j].visited:
            if not check_walls or (
                not current_cell.has_left_wall
                and not self._cells[i - 1][j].has_right_wall
            ):
                valid_cell_coords.append((i - 1, j))
        # check right
        if i + 1 < self.num_cols and not self._cells[i + 1][j].visited:
            if not check_walls or (
                not current_cell.has_right_wall
                and not self._cells[i + 1][j].has_left_wall
            ):
                valid_cell_coords.append((i + 1, j))
        # check top
        if j - 1 >= 0 and not self._cells[i][j - 1].visited:
            if not check_walls or (
                not current_cell.has_top_wall
                and not self._cells[i][j - 1].has_bottom_wall
            ):
                valid_cell_coords.append((i, j - 1))
        ## check bottom
        if j + 1 < self.num_rows and not self._cells[i][j + 1].visited:
            if not check_walls or (
                not current_cell.has_bottom_wall
                and not self._cells[i][j + 1].has_top_wall
            ):
                valid_cell_coords.append((i, j + 1))

        return valid_cell_coords

    def _break_walls_r(self, i: int, j: int) -> None:
        """
        Recursively break walls to generate the maze.

        This method assesses which direction the next cell is to the current cell (i, j), removes the wall between them,
        and then moves to the next. This continues until all cells in the maze have been visited.
        """
        current_cell = self._cells[i][j]
        current_cell.visited = True

        while True:
            to_visit: list[tuple[int, int]] = self._check_valid_cells(
                current_cell, i, j
            )

            # if there are no cells we can go to then draw the current cell and return
            if len(to_visit) < 1:
                self._draw_cell(i, j)
                return

            else:
                # randomly choose which cell we're going to visit next
                next_col, next_row = random.choice(to_visit)
                next_cell = self._cells[next_col][next_row]

                # check which direction the next cell is and remove walls
                # left
                if next_col < i:
                    current_cell.has_left_wall = False
                    next_cell.has_right_wall = False
                # right
                elif next_col > i:
                    current_cell.has_right_wall = False
                    next_cell.has_left_wall = False
                # top
                elif next_row < j:
                    current_cell.has_top_wall = False
                    next_cell.has_bottom_wall = False
                # bottom
                elif next_row > j:
                    current_cell.has_bottom_wall = False
                    next_cell.has_top_wall = False
                self._draw_cell(i, j)
                self._draw_cell(next_col, next_row)

                # move to next cell
                self._break_walls_r(next_col, next_row)

    def _reset_cells_visited(self) -> None:
        """Reset the visited value on each Cell to False to allow the solve method to reuse visited."""
        for col in range(self.num_cols):
            for row in range(self.num_rows):
                self._cells[col][row].visited = False

    def _solve_r(self, i: int, j: int) -> bool:
        """
        Recursively solve the maze using a depth-first search.

        This method starts from the current cell (i, j), then calls _check_valid_cells() for a list of tuples of valid cells to visit.
        It then moves to the next cell, and recurses until the maze is solved. If a dead end is found (either no unvisited neighbours or there's a wall in the way)
        it will backtrack to the previous cell and create a red line to indicate an undo. The solved path is drawn in a green line.
        """

        self._animate()
        current_cell = self._cells[i][j]
        current_cell.visited = True

        # if at end, return True
        if current_cell == self._cells[self.num_rows - 1][self.num_cols - 1]:
            return True

        valid_cell_coords = self._check_valid_cells(
            current_cell, i, j, check_walls=True
        )
        if len(valid_cell_coords) == 0:
            return False

        for cell_coord in valid_cell_coords:
            next_cell = self._cells[cell_coord[0]][cell_coord[1]]
            current_cell.draw_move(next_cell)
            if self._solve_r(cell_coord[0], cell_coord[1]):
                return True
            else:
                current_cell.draw_move(next_cell, undo=True)

    def solve(self) -> bool:
        """
        Solves the maze.

        The maze is solved via a recursive depth-first search algorithm to find a path from the start to the end of the maze.
        Each path correctly "solved" is displayed with a green line.
        """
        logging.info(" Starting to solve the maze!")
        return self._solve_r(0, 0)
