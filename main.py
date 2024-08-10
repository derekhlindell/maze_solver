from graphics import Window, Line, Point

def main():
    win = Window(800, 600)
    # Draw here
    line1 = Line(Point(30, 30), Point(30, 100))
    win.draw_line(line1, "black")
    win.draw_line(Line(Point(100, 30), Point(30, 30)), "red")

    win.wait_for_close()
main()