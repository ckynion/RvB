#
import battlefield
import players



class movement:
    class Blue:
        def __init__(players, battlefield, width=14, height=14, colour="blue",
                 x_speed=6, y_speed=4, x_start=0, y_start=0):
            players.width = width
            players.height = height
            players.x_posn = x_start
            players.y_posn = y_start
            players.color = color

            players.x_start = x_start
            players.y_start = y_start
            players.x_speed = x_speed
            players.y_speed = y_speed
            players.battlefield = battlefield
            players.circle = players.battlefield.draw_oval(players)

        def start_position(players):
           players.x_posn = players.x_start
           players.y_posn = players.y_start

        def start_ball(players, x_speed, y_speed):
            players.x_speed = -x_speed if random.randint(0,1) else x_speed
            players.y_speed = -y_speed if random.randint(0,1) else y_speed
            players.start_position()

        def move_next(players):
            players.x_posn = players.x_posn + players.x_speed
            players.y_posn = players.y_posn + players.y_speed
            if(players.x_posn <= 3):
                players.x_pson = 3
                players.x_speed = -players.x_speed
            if(players.x_posn >=(players.battlefield.width - (players.width - 3))):
                players .x_pson = (players.battlefield.width - (players.width - 3))
                players.x_speed = -players.x_speed

            if(players.y_posn <= 3):
                players.y_pson = 3
                players.y_speed = -players.y_speed
            if(players.y_posn >=(players.battlefield.height - (players.height - 3))):
                players.y_pson = (players.battlefield.height - (players.height - 3))
                players.y_speed = -players.y_speed

        x1 = players.x_posn
        x2 = players.x_posn+players.width
        y1 = players.y_posn
        y2 = players.y_posn+players.height
        players.battlefield.move_item(players.circle, x1, y1, x2, y2)

class Red:
    def __init__(players, battlefield, width=14, height=14, colour="red",
                 x_speed=6, y_speed=4, x_start=0, y_start=0):
            players.width = width
            players.height = height
            players.x_posn = x_start
            players.y_posn = y_start
            players.color = color

            players.x_start = x_start
            players.y_start = y_start
            players.x_speed = x_speed
            players.y_speed = y_speed
            players.battlefield = battlefield
            players.circle = players.battlefield.draw_oval(players)

    def start_position(players):
           players.x_posn = players.x_start
           players.y_posn = players.y_start

    def start_ball(players, x_speed, y_speed):
            players.x_speed = -x_speed if random.randint(0,1) else x_speed
            players.y_speed = -y_speed if random.randint(0,1) else y_speed
            players.start_position()

    def move_next(players):
            players.x_posn = players.x_posn + players.x_speed
            players.y_posn = players.y_posn + players.y_speed
            if(players.x_posn <= 3):
                players.x_pson = 3
                players.x_speed = -players.x_speed
            if(players.x_posn >=(players.battlefield.width - (players.width - 3))):
                players .x_pson = (players.battlefield.width - (players.width - 3))
                players.x_speed = -players.x_speed

            if(players.y_posn <= 3):
                players.y_pson = 3
                players.y_speed = -players.y_speed
            if(players.y_posn >=(players.battlefield.height - (players.height - 3))):
                players.y_pson = (players.battlefield.height - (players.height - 3))
                players.y_speed = -players.y_speed

            x1 = players.x_posn
            x2 = players.x_posn+players.width
            y1 = players.y_posn
            y2 = players.y_posn+players.height
            players.battlefield.move_item(players.circle, x1, y1, x2, y2)


