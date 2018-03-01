import movement
class Players:
# constructor 
    def __init__(players, battlefield, width=100, height=100, x_posn=50, y_posn=50, color="blue", x_speed=23, y_speed=23):
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
        players.rectangle = players.battlefield.draw_square(players)
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

    def draw_circle (self, circle):
        x1 = circle.x_posn
        x2 = circle.x_posn + square.width
        y1 = circle.y_posn
        y2 = circle.y_posn + square.height
        c = circle.color
        return self.canvas.create_circle(x1, y1, x2, y2, fill=c)

    
    def move_up(self, master):
        self.y_posn = self.y_posn - self.y_speed
        if(self.y_posn <= 0):
            self.y_posn = 0
        x1 = self.x_posn
        x2 = self.x_posn+self.width
        y1 = self.y_posn
        y2 = self.y_posn+self.height
        self.table.move_item(self.circle, x1, y1, x2, y2)

    def move_down(self, master):
        self.y_posn = self.y_posn + self.y_speed
        far_bottom = self.table.height - self.height
        if(self.y_posn >= far_bottom):
            self.y_posn = far_bottom
        x1 = self.x_posn
        x2 = self.x_posn+self.width
        y1 = self.y_posn
        y2 = self.y_posn+self.height
        self.table.move_item(self.circle, x1, y1, x2, y2)

    def move_left(self, master):
        self.x_posn = self.x_posn - self.x_speed
        if(self.x_posn <= 0):
            self.x_posn = 0
        x1 = self.x_posn
        x2 = self.x_posn+self.width
        y1 = self.y_posn
        y2 = self.y_posn+self.height
        self.table.move_item(self.circle, x1, y1, x2, y2)

    def move_right(self, master):
        self.x_posn = self.x_posn + self.x_speed
        far_right = self.table.width - self.width
        if(self.x_posn >= far_right):
            self.x_posn = far_right
        x1 = self.x_posn
        x2 = self.x_posn+self.width
        y1 = self.y_posn
        y2 = self.y_posn+self.height
        self.table.move_item(self.circle, x1, y1, x2, y2)
    def detect_collision(self, ball, sides_sweet_spot=True, topnbottom_sweet_spot=False):
        collision_direction = " "
        collision = False
        feel = 5
        


