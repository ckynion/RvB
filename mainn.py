from tkinter import *

import battlefield, red_player

window = Tk()
window.title("RvB")
my_battlefield = battlefield.Battlefield(window)

red_player = red_player.Red_Player(battlefield=my_battlefield, width=85, height=100, x_posn=550, y_posn=140, color="red")

