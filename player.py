from tkinter import *

class Player:

    def __init__(self, battlefield, width=80, height=100, x_posn=50, y_posn=50, color="red", x_speed=23, y_speed=23):
        self.width = width
        self.height = height
        self.x_posn = x_posn
        self.y_posn = y_posn
        self.color = color
        self.x_start = x_posn
        self.y_start = y_posn
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.battlefield = battlefield
        self.polygon = self.battlefield.create_player(self)
        
    def create_player(self, x, y, tk_fill):
        return self.canvas.create_polygon(x, y, x + 20, y - 30, x - 20, y - 30, fill=tk_fill)
         
