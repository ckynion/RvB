import tkinter as tk
 
SCREEN = 1000, 1300
         
class Bullet:
    def __init__(self, canvas, x, y, tk_fill, movement):
        self.bullet = canvas.create_oval(x -3 , y - 3, x + 3, y + 3, fill=tk_fill)
        self.movement = movement
         
    def move(self, canvas):
        canvas.move(self.bullet, self.movement[0], self.movement[1])
 
class App(tk.Frame):
    def __init__(self, master):
        # put canvas in frame so you can have other goodies
        tk.Frame.__init__(self, master)
        self.pack()
        self.canvas = tk.Canvas(self, width=SCREEN[0], height=SCREEN[1])
        self.canvas.pack()
        self.bullets = [] # store bullets
        self.tick_loop() # start the tick loop
        self.ship = self.create_ship(300, 370, "red")
         
        master.bind("a", self.go_left)
        master.bind("d", self.go_right)
        master.bind("w", self.go_up)
        master.bind("s", self.go_down)
        master.bind("z", self.space_key)
        master.bind("x", self.go_b)
        master.bind("c", self.go_v)
         
    def create_ship(self, x, y, tk_fill):
        return self.canvas.create_polygon(x, y, x - 20, y + 30, x + 20, y + 30, fill=tk_fill)
         
    def tick_loop(self):
        remove_list = []
        for enum, bullet in enumerate(self.bullets):
            coords = self.canvas.coords(bullet.bullet)
            if coords[1] < 0 or coords[0] < 0 or coords[2] > SCREEN[0]:
                remove_list.append(enum)
                self.canvas.delete(bullet.bullet)
            else:
                bullet.move(self.canvas)
         
        # fix poping bug        
        for enum, index in enumerate(remove_list):
            self.bullets.pop(index - enum)
     
        # framerate per seconds 1000/30 = 30 frames roughly
        self.after(int(1000/30), self.tick_loop)        
         
    def go_left(self, event):
        self.canvas.move(self.ship, -5, 0)
        self.canvas.update()
         
    def go_right(self, event):
        self.canvas.move(self.ship, 5, 0)
        self.canvas.update()
         
    def go_up(self, event):
        self.canvas.move(self.ship, 0, -5)
        self.canvas.update()
         
    def go_down(self, event):
        self.canvas.move(self.ship, 0, 5)
        self.canvas.update()
         
    def space_key(self, event=0):
        # only want the first two coords
        x, y = self.canvas.coords(self.ship)[:2]
        # just having shoot straight up
        self.bullets.append(Bullet(self.canvas, x, y, "red", (0, -10)))
     
    # spread shooting
    def go_b(self, event):
        # only want the first two coords
        x, y = self.canvas.coords(self.ship)[:2]        
        #up
        self.bullets.append(Bullet(self.canvas, x, y, "red", (0, -8)))
        #left
        self.bullets.append(Bullet(self.canvas, x, y, "red", (-8, 0)))
        #right
        self.bullets.append(Bullet(self.canvas, x, y, "red", (8, 0)))
 
    # triple shoot striaght up
    def go_v(self, event):
        # only want the first two coords
        x, y = self.canvas.coords(self.ship)[:2]        
        #up
        self.bullets.append(Bullet(self.canvas, x, y, "red", (0, -5)))
        self.bullets.append(Bullet(self.canvas, x - 50, y, "red", (0, -5)))
        self.bullets.append(Bullet(self.canvas, x + 50, y, "red", (0, -5)))
    
def main():
    root = tk.Tk()
    app = App(root)
    app.mainloop()
     
if __name__ == '__main__':
    main()

