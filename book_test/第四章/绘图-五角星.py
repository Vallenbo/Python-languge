import turtle
import turtle as t  # 导入海龟绘图,重名为t

t.pensize(5)
t.pencolor("yellow")
t.fillcolor("red")
t.begin_fill()
for _ in range(5):
    t.forward(200)
    t.right(144)

t.end_fill()
t.penup()
t.goto(-150, -120)
t.color("violet")
t.write("五角星", font=('simhei',30))
t.mainloop()
