from tkinter import *

import battlefield, players, player, movement

window = Tk()
window.title("RvB")
my_battle = battlefield.Battlefield(window)
self.canvas.create_circle(x1, y1, x2, y2, fill="black")

player=player.Player(battlefield=my_battle,width=15,height=15,x_posn=575,y_posn=150,colour="red")

players=players.Players(battlefield=my_battle,width=15,height=15,x_posn=575,y_posn=150,colour="blue")

def game_flow():
    my_players.move_next()
    window.after(50, game_flow)
    if (my_players.x_posn + my_players.width >= my_battle.width - 3):
        my_battle.move_item(player.circle, 20, 150, 35, 250)
        my_battle.move_item(players.circle, 575, 150, 590, 250)


        
window.bind("w",players_B.move_up)
window.bind("s",players_B.move_down)
window.bind("a",players_B.move_left)
window.bind("d",players_B.move_right)
window.bind("q",players_B.shoot)
window.bind("<Up>",players_R.move_up)
window.bind("<Down>",players_R.move_down)
window.bind("<Left>",players_R.move_left)
window.bind("<Right>",players_R.move_right)
window.bind("<space>",players_R.shoot)

game_flow()

window.mainloop()
