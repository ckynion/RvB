import table
class Bat:
    def __init__(self,table,width=15,height=100,x_posn=50,y_posn=50,colour="tan",x_speed=23,y_speed=23):
        self.width=width
        self.height=height
        self.x_posn=x_posn
        self.y_posn=y_posn
        self.colour=colour
        self.x_start=x_posn
        self.y_start=y_posn
        self.x_speed=x_speed
        self.y_speed=y_speed
        self.table=table
        self.rectangle=self.table.draw_rectangle(self)
        
    def move_up(self,master):
        self.y_posn=self.y_posn-self.y_speed
        if(self.y_posn<=0):
            self.y_posn=0
        x1=self.x_posn
        x2=self.x_posn+self.width
        y1=self.y_posn
        y2=self.y_posn+self.height
        self.table.move_item(self.rectangle,x1,y1,x2,y2)
        
    def move_down(self,master):
        self.y_posn=self.y_posn+self.y_speed
        far_bottom=self.table.height-self.height
        if(self.y_posn>=far_bottom):
            self.y_posn=far_bottom
        x1=self.x_posn
        x2=self.x_posn+self.width
        y1=self.y_posn
        y2=self.y_posn+self.height
        self.table.move_item(self.rectangle,x1,y1,x2,y2)

    def move_left(self,master):
        self.x_posn=self.x_posn-self.x_speed
        if(self.x_posn<=0):
            self.x_posn=0
        x1=self.x_posn
        x2=self.x_posn+self.width
        y1=self.y_posn
        y2=self.y+posn+self.height
        self.table.move_item(self.rectangle,x1,y1,x2,y2)

    def move_right(self,master):
        self.x_posn=self.x_posn+self.x_speed
        far_right=self.table.width-self.width
        if(self.xposn>=far_right):
            self.x_posn=far_right
        x1=self.x_posn
        x2=self.x_posn+self.width
        y1=self.y_posn
        y2=self.y_posn+self.height
        self.table.move_item(self.rectangle,x1,y1,x2,y2)
