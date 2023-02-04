#!/usr/bin/env python3

import tkinter as tk
from game import play, quit_app

class CoordinatePlane:

    # master is the parent widget of the GUI application
    def __init__(self, master):
        
        # assign parameter to class variable
        self.master = master

        # set title on class variable
        self.master.title('Coordinate Plane')

        # create canvas object
        self.canvas = tk.Canvas(self.master, width=400, height=400)

        # build geometry
        self.canvas.pack()
        self.draw_grid()

    # this function draws a line every 20 units in a grid pattern
    def draw_grid(self):
        for i in range(20):
            x = 20 * i
            self.canvas.create_line(x, 0, x, 400, fill="#cccccc")
            self.canvas.create_line(0, x, 400, x, fill="#cccccc")

def main():
    root = tk.Tk()
    start_button = tk.Button(root, text='Start game', command=play)
    start_button.pack()

    quit_button = tk.Button(root, text='Quit game', command=quit_app)
    quit_button.pack()

    app = CoordinatePlane(root)
    root.mainloop()


if __name__ == '__main__':
    main()
