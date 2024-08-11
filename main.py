from graphics import Window, Line, Point
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)
    # Draw here

    x1 = 100
    y1 = 100
    x2 = 200
    y2 = 200

    maze = Maze(
            50,
            50,
            3,
            3,
            50,
            50,
            win
        )

    
    # cells
    # cell = Cell(win)
    # cell.draw(x1, y1, x2, y2)

    # c = Cell(win)
    # c.has_left_wall = False 
    # c.draw(50, 50, 100, 100)

    # c = Cell(win)
    # c.has_right_wall = False
    # c.draw(125, 125, 200, 200)

    # c2 = Cell(win)
    # c2.has_bottom_wall = False
    # c2.draw(225, 225, 250, 250)

    # c = Cell(win)
    # c.has_top_wall = False
    # c.draw(300, 300, 500, 500)

    # c.draw_move(c2)

    win.wait_for_close()


main()