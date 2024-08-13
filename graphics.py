from tkinter import Tk, Canvas

import logging

logger = logging.getLogger(__name__)


class Point:
    def __init__(self, x: int, y: int) -> None:
        """Initialize a Point based on its x and y coordinates."""
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

class Line:
    def __init__(self, point1: Point, point2: Point) -> None:
        """Initialize a Line with two input Points."""
        self.__point1 = point1
        self.__point2 = point2

    def __repr__(self):
        return f"Line(point1={self.__point1!r}, point2={self.__point2!r})"

    def draw(self, canvas: Canvas, fill_color: str = "black", width: int = 3) -> None:
        """Draw a line on the input Canvas based on the input fill_color and width."""
        canvas.create_line(
            self.__point1.x,
            self.__point1.y,
            self.__point2.x,
            self.__point2.y,
            fill=fill_color,
            width=width,
        )


class Window:
    def __init__(self, width: int, height: int) -> None:
        """Initialize a Window with the specified width and height."""
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, height=height, width=width)
        self.__canvas.pack()
        self.__running = False

    def __repr__(self):
        return f"""Window(
                __root={self.__root!r},
                __root.title()={self.__root.title()!r},
                __canvas={self.__canvas!r},
                __running={self.__running!r},
            )"""

    def redraw(self) -> None:
        """Redraw the Window."""
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self) -> None:
        """Wait for the window to close."""
        self.__running = True
        while self.__running:
            self.redraw()
        logger.info("Window has been closed.")

    def draw_line(self, line: Line, fill_color: str = "black") -> None:
        """Draw a line on the window with the given color."""
        line.draw(self.__canvas, fill_color)

    def close(self) -> None:
        """Close the window."""
        self.__running = False
