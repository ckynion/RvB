from tkinter import*
class Movement:
    def move_item(self,item,x1,y1,x2,y2):
        self.canvas.coords(item,x1,y1,x2,y2)
  
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

    def start_position(self):
        self.x_posn=self.x_start
        self.y_posn=self.y_start
