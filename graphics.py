from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, height=height, width=width)
        self.__canvas.pack()
        self.__running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("Window has been closed.")

    def draw_line(self, line, fill_color="black"):
        # creates a line from an input line object with the input fill color
        line.draw(self.__canvas, fill_color)

    def close(self):
        self.__running = False


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    # takes in two point classes
    def __init__(self, point1, point2):
        self.__point1 = point1
        self.__point2 = point2
    
    # draws a line on the current canvas
    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.__point1.x, self.__point1.y,
            self.__point2.x, self.__point2.y, 
            fill=fill_color, 
            width=2,
        )