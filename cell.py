from __future__ import annotations
from graphics import Window, Line, Point

import logging

logger = logging.getLogger(__name__)

# Define color constants
WALL_COLOR = "black"
NO_WALL_COLOR = "#d9d9d9"
MOVE_COLOR = "green"
UNDO_COLOR = "tomato"


class Cell:
    def __init__(self, win: Window = None) -> None:
        self.has_left_wall: bool = True
        self.has_right_wall: bool = True
        self.has_top_wall: bool = True
        self.has_bottom_wall: bool = True
        self.visited: bool = False
        self.__x1: int = None
        self.__y1: int = None
        self.__x2: int = None
        self.__y2: int = None
        self.__win: Window = win

    def __repr__(self):
        rep = f"""Cell(
                has_left_wall={self.has_left_wall!r}
                has_right_wall={self.has_right_wall!r}
                has_top_wall={self.has_top_wall!r}
                has_bottom_wall={self.has_bottom_wall!r}
                visited={self.visited!r}

                __x1={self.__x1!r}
                __y1={self.__y1!r}
                __x2={self.__x2!r}
                __y2={self.__y2!r}

                __win={self.__win!r}
            )"""
        return rep

    def draw(self, x1: int, y1: int, x2: int, y2: int):
        """
        Draw the cell in the window.

        Walls are drawn in black, and if there is no wall property, walls are drawn in white to illustrate "no" wall.
        The x1, y1, x2, y2 parameters represent the top-left and bottom-right corners of the cell respectively.
        """
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

        line = Line(Point(x1, y1), Point(x1, y2))
        if self.has_left_wall:
            self.__win.draw_line(line, WALL_COLOR)
        else:
            self.__win.draw_line(line, NO_WALL_COLOR)

        line = Line(Point(x2, y1), Point(x2, y2))
        if self.has_right_wall:
            self.__win.draw_line(line, WALL_COLOR)
        else:
            self.__win.draw_line(line, NO_WALL_COLOR)

        line = Line(Point(x1, y1), Point(x2, y1))
        if self.has_top_wall:
            self.__win.draw_line(line, WALL_COLOR)
        else:
            self.__win.draw_line(line, NO_WALL_COLOR)

        line = Line(Point(x1, y2), Point(x2, y2))
        if self.has_bottom_wall:
            self.__win.draw_line(line, WALL_COLOR)
        else:
            self.__win.draw_line(line, NO_WALL_COLOR)

    def get_center(self) -> (int, int):
        """
        Calculate the center of the cell The center is defined as the point equidistant from all four corners
        of the cell. This is used when drawing a line from one cell to another.
        """
        center_x = (self.__x1 + self.__x2) // 2
        center_y = (self.__y1 + self.__y2) // 2
        return center_x, center_y

    def draw_move(self, to_cell: Cell, undo: bool = False):
        """
        Create and draw a Line from the center of the current cell to another cell

        If 'undo' is True, the line is drawn in UNDO_COLOR, otherwise it's drawn in MOVE_COLOR.
        This can be used to visualize the pathfinding process.
        """
        center_x, center_y = self.get_center()
        to_center_x, to_center_y = to_cell.get_center()

        line = Line(Point(center_x, center_y), Point(to_center_x, to_center_y))
        fill_color = MOVE_COLOR
        if undo:
            fill_color = UNDO_COLOR

        self.__win.draw_line(line, fill_color)
