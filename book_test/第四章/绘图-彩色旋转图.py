from turtle import *


def curvemove():
    for i in range(200):
        right(1)
        forward(1)


color('red', 'pink')
begin_fill()
left(140)
forward(110)
curvemove()
left(120)
curvemove()
forward(110)
end_fill()
penup()
goto(-17, 90)
write("我爱你", font=('simhei', 20))
mainloop()
done()
