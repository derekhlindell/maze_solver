import time
from cell import Cell

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
    ):
        self._cells = []
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows 
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win        

        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self):
        # create number of cells based on columns
        for col in range(self.num_cols):
            current_col = []
            for row in range(self.num_rows):
                current_col.append(Cell(self.win))
            self._cells.append(current_col)
        
        for col in range(self.num_cols):
            for row in range(self.num_rows):
                self._draw_cell(col, row)

    def _draw_cell(self, i, j):
        if self.win is None:
            return

        maze_corner_x, maze_corner_y = self.x1, self.y1

        # cell needs top left corner x and y, and bottom right corner of x and y
        cell_top_left_x = maze_corner_x + (self.cell_size_x * i)
        cell_top_left_y = maze_corner_y + (self.cell_size_y * j)
        cell_bottom_right_x = cell_top_left_x + self.cell_size_x
        cell_bottom_right_y = cell_top_left_y + self.cell_size_y
        self._cells[i][j].draw(
            cell_top_left_x,
            cell_top_left_y,
            cell_bottom_right_x,
            cell_bottom_right_y
        )
        self._animate()

    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(.05)

    def _break_entrance_and_exit(self):
        first_cell = self._cells[0][0]
        last_cell = self._cells[-1][-1]
        first_cell.has_left_wall = False
        self._draw_cell(0,0)
        last_cell.has_right_wall = False
        self._draw_cell(len(self._cells)-1,len(self._cells)-1)

        
