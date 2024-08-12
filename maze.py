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

        self._reset_cells_visited()

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
        time.sleep(.01)

    def _break_entrance_and_exit(self):
        first_cell = self._cells[0][0]
        last_cell = self._cells[-1][-1]
        first_cell.has_left_wall = False
        self._draw_cell(0,0)
        last_cell.has_right_wall = False
        self._draw_cell(len(self._cells)-1,len(self._cells)-1)

    def _check_valid_cells(self, current_cell, i, j, check_walls=False):
        ''' 
            check each adjacent cell if they haven't been visited.
            if check_walls is on, check if there are any walls in the way. 
        '''
        valid_cell_coords = []

        # check left
        if i-1 >= 0 and not self._cells[i-1][j].visited:
            if not check_walls or (
                not current_cell.has_left_wall and 
                not self._cells[i-1][j].has_right_wall
            ):
                valid_cell_coords.append((i-1,j))
        # check right
        if i+1 < self.num_cols and not self._cells[i+1][j].visited:
            if not check_walls or (
                not current_cell.has_right_wall and 
                not self._cells[i+1][j].has_left_wall
            ):
                valid_cell_coords.append((i+1, j))
        # check top
        if j-1 >= 0 and not self._cells[i][j-1].visited:
            if not check_walls or (
                not current_cell.has_top_wall and 
                not self._cells[i][j-1].has_bottom_wall
            ):
                valid_cell_coords.append((i,j-1))
        ## check bottom
        if j+1 < self.num_rows and not self._cells[i][j+1].visited:
            if not check_walls or (
                not current_cell.has_bottom_wall and 
                not self._cells[i][j+1].has_top_wall
            ):
                valid_cell_coords.append((i,j+1))

        return valid_cell_coords

    def _break_walls_r(self, i, j):
        # mark current cell as visited
        current_cell = self._cells[i][j]
        current_cell.visited = True
        direction = None
        while True:
            to_visit = self._check_valid_cells(current_cell, i, j)

            # if there are no cells we can go to then draw the current cell and return
            if len(to_visit) < 1:
                # draw current cell
                self._draw_cell(i, j)
                return

            else:
                #randomly choose which cell we're going to visit next
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

    def _reset_cells_visited(self):
        for col in range(self.num_cols):
            for row in range(self.num_rows):
                self._cells[col][row].visited = False

    def _solve_r(self, i, j):
        self._animate()
        current_cell = self._cells[i][j]
        current_cell.visited = True

        #if at end, return True
        if current_cell == self._cells[self.num_rows-1][self.num_cols-1]:
            return True

        valid_cell_coords = self._check_valid_cells(current_cell, i, j, check_walls=True)
        print(valid_cell_coords)
        if len(valid_cell_coords) == 0:
            print("no cells")
            return False

        for cell_coord in valid_cell_coords:
            next_cell = self._cells[cell_coord[0]][cell_coord[1]]
            current_cell.draw_move(next_cell)
            if self._solve_r(cell_coord[0], cell_coord[1]):
                return True
            else:
                current_cell.draw_move(next_cell, undo=True)

    def solve(self):
        return self._solve_r(0, 0)
