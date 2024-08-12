from graphics import Window, Line, Point

import logging
logger = logging.getLogger(__name__)

class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self.__x1 = None
        self.__y1 = None
        self.__x2 = None
        self.__y2 = None
        self.__win = win

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

    def draw(self, x1, y1, x2, y2):
        ''' draw the cell '''
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

        line = Line(Point(x1, y1), Point(x1, y2))
        if self.has_left_wall:
            self.__win.draw_line(line)
        else:
            self.__win.draw_line(line, "#d9d9d9")

        line = Line(Point(x2, y1), Point(x2, y2))
        if self.has_right_wall:
            self.__win.draw_line(line)
        else:
            self.__win.draw_line(line, "#d9d9d9")

        line = Line(Point(x1, y1), Point(x2, y1))
        if self.has_top_wall:
            self.__win.draw_line(line)
        else:
            self.__win.draw_line(line, "#d9d9d9")

        line = Line(Point(x1, y2), Point(x2, y2))
        if self.has_bottom_wall:
            self.__win.draw_line(line)
        else:
            self.__win.draw_line(line, "#d9d9d9")


    def get_center(self):
        ''' calculate the center of the cell '''
        center_x = (self.__x1 + self.__x2) // 2
        center_y = (self.__y1 + self.__y2) // 2
        return center_x, center_y


    def draw_move(self, to_cell, undo=False):
        ''' creates a line from the centers of this cell to another cell '''
        # get this cells center
        center_x, center_y = self.get_center()
        to_center_x, to_center_y = to_cell.get_center()

        # if undo is set, create a gray line
        line = Line(Point(center_x, center_y), Point(to_center_x, to_center_y))

        fill_color = "red"
        if undo:
            fill_color = "gray"

        self.__win.draw_line(line, fill_color)

