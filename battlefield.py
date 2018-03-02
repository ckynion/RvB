from tkinter import *
import player
class Battlefield:


    def __init__(self, window, color="tan", width=1000, height=800):
        self.width = width
        self.height = height
        self.color = color
        self.canvas = Canvas(window, bg=self.color, height=self.height, width=self.width)
        self.canvas.pack()

    def draw_rectangle(self, rectangle):
        x1 = rectangle.x_posn
        x2 = rectangle.x_posn + rectangle.width
        y1 = rectangle.y_posn
        y2 = rectangle.y_posn + rectangle.height
        c = rectangle.color
        return self.canvas.create_rectangle(x1, y1, x2, y2, fill=c)
         
