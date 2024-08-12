from graphics import Window, Line, Point
from cell import Cell
from maze import Maze
import random
import logging
logger = logging.getLogger(__name__)

def main():
    # logging.basicConfig(filename='maze_solver.log', level=logging.DEBUG)
    logging.basicConfig(level=logging.DEBUG)
    logger.info(' Started')

    win = Window(800, 600)
    # Draw here

    x1 = 100
    y1 = 100
    x2 = 200
    y2 = 200

    maze = Maze(
            50,
            50,
            9,
            9,
            50,
            50,
            win,
            0
        )

    maze.solve()

    win.wait_for_close()
    logger.info(' Finished')

main()