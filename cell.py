from graphics import Window, Line, Point


class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = None
        self.__y1 = None
        self.__x2 = None
        self.__y2 = None
        self.__win = win
    
    def draw(self, x1, y1, x2, y2):
        ''' draw the cell '''
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self.__win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self.__win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self.__win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self.__win.draw_line(line)
    
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


