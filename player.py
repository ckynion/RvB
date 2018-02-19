import battlefield, random
class Player:
# constructor 
    def _-init__(self, battlefield, width=100, height=100, x_posn=50, y_posn=50, color="red", x_speed=23, y_speed=23):
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
        self.rectangle = self.battlefield.draw_rectangle(self)
# methods
    def start_position(self):
        self.x_posn = self.x_start
        self.y_posn = self.y_start
    def detect_collision(self, movement, sides_sweet_spot=True, topnbottom_sweet_spot=False):
        collision_direction = ""
        collision = False
        feel = 5
# player variables
        top = self.y_posn
        bottom = self.y_posn + self.height
        left = self.x_posn
        right = self.x_posn + self.width
        v_centre = top + (self.height/2)
        h_centre = left + (self.width/2)
# bullet variables
        top_m = y_posn
        bottom_m = movement.y_posn + movement.height
        left_m = movement.x_posn
        right_m = movement.x_posn + movement.width
        r = (right_m - left_m)/2
        v_centre_m = top_m + r
        h_centre_m = left_m + r

        if((sides_sweet_spot == True) and (collision_direction == "W" or collision_direction == "E")):
# find out where the shooter shot
    def move_up(self, master):
        self.y_posn = self.y_posn - self.y_speed
        if(self.y_posn <= 0):
            self.y_posn = 0
        x1 = self.x_posn
        x2 = self.x_posn+self.width
        y1 = self.y_posn
        y2 = self.y_posn+self.height
        self.battlefield.move_item(self.rectangle, x1, y1, x2, y2)
    def move_down(self, master):
        self.y_posn = self.y_posn + self.y_speed
        far_bottom = self.battlefield.height - self.height
        if(self.y_posn >= far_bottom):
            self.y_posn = far_bottom
        x1 = self.x_posn
        x2 = self.x_posn+self.width
        y1 = self.y_posn
        y2 = self.y_posn+self.height
        self.battlefield.move_item(self.rectangle, x1, y1, x2, y2)
    def move_left(self, master):
        self.x_posn = self.x_posn - self.x_speed
        if(self.x_posn <= 0):
            self.x_posn = 0
        x1 = self.x_posn
        x2 = self.x_posn+self.width
        y1 = self.y_posn
        y2 = self.y_posn+self.height
        self.table.move_item(self.rectangle, x1, y1, x2, y2)
    def move_right(self, master):
        self.x_posn = self.x_posn + self.x_speed
        far_right = self.battlefield.width - self.width
        if(self.x_posn >= far_right):
            sefl.x_posn = far_right
        x1 = self.x_posn
        x2 = self.x_posn+self.width
        y1 = self.y_posn
        y2 = self.y_posn+self.height
        self.battlefield.move_item(self.rectanlge, x1, y1, x2, y2)



















                    


