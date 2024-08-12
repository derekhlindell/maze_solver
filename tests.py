import unittest

from maze import Maze

import logging
logger = logging.getLogger(__name__)

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_maze_create_cells_large(self):
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_reset_maze(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

        visited = []
        for col in range(num_cols):
            for row in range(num_rows):
                if m1._cells[col][row].visited:
                    visited.append(m1._cells[col][row])
        
        self.assertEqual(
            len(visited),
            0
        )

if __name__ == "__main__":
    unittest.main()