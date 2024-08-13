from graphics import Window
from maze import Maze

import logging

logger = logging.getLogger(__name__)


def main() -> None:
    """
    The main function initialize the window and maze, attempts to solve the maze,
    and then waits for the window to close.
    """

    logging.basicConfig(level=logging.INFO)
    logger.info(" Started Maze Solver")

    win_x = 800  # Window width
    win_y = 600  # Window height

    win = Window(win_x, win_y)
    logger.info(" Window created: %s (size: %s, %s)", win, win_x, win_y)

    ### Begin drawing inside window ###

    margin = 50  # Margin of the maze
    num_cols = 9  # Number of columns in the maze
    num_rows = 9  # Number of rows in the maze
    cell_size_x = 50  # Width of each cell in the maze
    cell_size_y = 50  # Height of each cell in the maze

    maze = Maze(
        margin,
        margin,
        num_cols,
        num_rows,
        cell_size_x,
        cell_size_y,
        win,
    )

    maze.solve()  # solve the maze

    ### End drawing inside window ###

    win.wait_for_close()

    logger.info(" Finishing program!")


if __name__ == "__main__":
    main()
