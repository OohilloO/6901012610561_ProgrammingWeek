class Balloon:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
    def show(self):
        line(self.x, self.y, self.x, self.y + 100)
        ellipse(self.x, self.y, self.r, self.r)
    def move(self):
        if self.y > width / 2:
            self.y = self.y - 2
        else:
            self.y = self.y - 4

b = Balloon(400, 600, 50)
def setup():
    size(1000, 1000)
def draw():
    background(255)
    b.show()
    b.move()
#บอลลูนลอยขึ้น เร็วขึ้นเมื่อพ้นกึ่งกลาง

balloons = []
def setup():
    size(1000, 1000)
    x_coords = [100, 200, 400, 500, 600]
    y_coords = [900, 850, 600, 700, 950]
    i = 0
    while i < len(x_coords):
        balloons.append(Balloon(x_coords[i], y_coords[i], 50))
        i = i + 1
#บอลลูน 5 ลูกลอยพร้อมกัน

import turtle
t = turtle.Turtle()
t.forward(100)
t.left(90)
turtle.done()

import tkinter as tk
root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()
canvas.create_oval(200, 50, 400, 250, fill="orange")
root.mainloop()

import matplotlib.pyplot as plt
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
plt.plot(days, [30, 31, 32, 30, 30, 31, 33])
plt.show()
#กราฟอุณหภูมิ (สไลด์ใช้ 4 สัปดาห์ x 7 วัน ด้วย 2D array)