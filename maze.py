import time
import random
from cell import Cell

import logging
logger = logging.getLogger(__name__)

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
        seed=None,
    ):
        self._cells = []
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win        
        self.seed = seed

        logging.info("=== Creating the Maze ===")
        self._create_cells()
        logging.info(" breaking entrance and exit ")
        self._break_entrance_and_exit()
        # If we don't have a seed set the generation will always be random
        # set this for debugging!
        if self.seed is not None:
            self.seed = random.seed(seed)
        
        logging.info(" breaking walls ")
        self._break_walls_r(0,0)

    def __repr__(self):
        return f'''Maze(
                _cells={self._cells!r},
                x1={self.x1!r},
                y1={self.y1!r},
                num_rows={self.num_rows!r},
                num_cols={self.num_cols!r},
                cell_size_x={self.cell_size_x!r}, 
                cell_size_y={self.cell_size_y!r},
                win={self.win!r},         
                seed={self.seed!r}
            )'''

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

    def _break_walls_r(self, i, j):
        # mark current cell as visited
        current_cell = self._cells[i][j]
        current_cell.visited = True
        direction = None

        while True:
            # create new empty list to hold which i, j values we're going to visit
            to_visit = []
            
            # check if the cells directly adjacent to the current cell
            # check left
            if i-1 >= 0:
                if self._cells[i-1][j].visited is False:
                    to_visit.append((i-1,j))

            # check right
            if i+1 < self.num_cols:
                if self._cells[i+1][j].visited is False:
                    to_visit.append((i+1,j))
            
            # check top
            if j-1 >= 0:
                if self._cells[i][j-1].visited is False:
                    to_visit.append((i,j-1))

            ## check bottom
            if j+1 < self.num_rows: 
                if self._cells[i][j+1].visited is False:
                    to_visit.append((i,j+1))


            # if there are no cells we can go to then draw the current cell and return to break the loop
            if len(to_visit) < 1:
                # draw current cell
                self._draw_cell(i, j)
                return

            # else, pick a random direction to go to
            else:
                next_col, next_row = random.choice(to_visit)
                next_cell = self._cells[next_col][next_row]
                # knock down the walls between current cell and the next cell
                # next cell is left
                if next_col < i:
                    current_cell.has_left_wall = False
                    next_cell.has_right_wall = False
                # next cell is right
                elif next_col > i:
                    current_cell.has_right_wall = False
                    next_cell.has_left_wall = False
                # next cell is above
                elif next_row < j:
                    current_cell.has_top_wall = False
                    next_cell.has_bottom_wall = False
                # next cell is below 
                elif next_row > j:
                    current_cell.has_bottom_wall = False
                    next_cell.has_top_wall = False
                
                self._draw_cell(i,j)
                self._draw_cell(next_col, next_row)

                # check which direction the new cell is from the current cell
                # move to that cell by recursively calling the current function
                self._break_walls_r(next_col, next_row)
                print(to_visit)


