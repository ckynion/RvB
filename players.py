import battlefield, random
class Players:
# constructor 
    def __init__(players, battlefield, width=100, height=100, x_posn=50, y_posn=50, color="red", x_speed=23, y_speed=23):
        players.width = width
        players.height = height
        players.x_posn = x_posn
        players.y_posn = y_posn
        players.color = color
        players.x_start = x_posn
        players.y_start = y_posn
        players.x_speed = x_speed
        players.y_speed = y_speed
        players.battlefield = battlefield
        players.rectangle = players.battlefield.draw_rectangle(players)
# methods
    def start_position(players):
        players.x_posn = players.x_start
        players.y_posn = players.y_start
# player variables
        top = players.y_posn
        bottom = players.y_posn + players.height
        left = players.x_posn
        right = players.x_posn + players.width
        v_centre = top + (players.height/2)
        h_centre = left + (players.width/2)
# bullet variables
        top_m = y_posn
        bottom_m = movement.y_posn + movement.height
        left_m = movement.x_posn
        right_m = movement.x_posn + movement.width
        r = (right_m - left_m)/2
        v_centre_m = top_m + r
        h_centre_m = left_m + r

# find out where the shooter shot
def move_up(players, master):
    players.y_posn = players.y_posn - players.y_speed
    if(players.y_posn <= 0):
        players.y_posn = 0
        x1 = players.x_posn
        x2 = players.x_posn+players.width
        y1 = players.y_posn
        y2 = players.y_posn+players.height
        players.battlefield.move_item(players.rectangle, x1, y1, x2, y2)
    def move_down(players, master):
        players.y_posn = players.y_posn + players.y_speed
        far_bottom = players.battlefield.height - players.height
        if(players.y_posn >= far_bottom):
            players.y_posn = far_bottom
        x1 = players.x_posn
        x2 = players.x_posn+players.width
        y1 = players.y_posn
        y2 = players.y_posn+players.height
        players.battlefield.move_item(players.rectangle, x1, y1, x2, y2)
        players.x_posn = players.x_posn - players.x_speed
        if(players.x_posn <= 0):
            players.x_posn = 0
        x1 = players.x_posn
        x2 = players.x_posn+players.width
        y1 = players.y_posn
        y2 = players.y_posn+players.height
        players.table.move_item(players.rectangle, x1, y1, x2, y2)
    def move_right(players, master):
        players.x_posn = players.x_posn + players.x_speed
        far_right = players.battlefield.width - players.width
        if(players.x_posn >= far_right):
            players.x_posn = far_right
        x1 = players.x_posn
        x2 = players.x_posn+players.width
        y1 = players.y_posn
        y2 = players.y_posn+players.height
        players.battlefield.move_item(players.rectanlge, x1, y1, x2, y2)



















                    


