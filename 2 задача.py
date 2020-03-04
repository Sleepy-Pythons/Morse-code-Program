import math
import tkinter

master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='white', height=600, width=600)
n = int(input())
p = []
for k in range(0, n):
    p.append((200 * math.cos(2 * math.pi * k / n) + 300,
              200 * math.sin(2 * math.pi * k / n) + 300))
if n % 2 == 0:    # шаг для звезд с четным количеством концов
    k = (n - 2) // 2
else:    # и с нечетным
    k = (n - 1) // 2
for i in range(1, n):
    for j in range(1, n + 1, k):
        canvas.create_line(p[(j * i - 1) % n], p[(j * i + k - 1) % n], fill='blue')
canvas.pack()
master.mainloop()