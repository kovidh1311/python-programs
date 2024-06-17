
import turtle
t = 0
x = turtle.Pen()
x.speed(0)
colours = ["red", "yellow", "blue", "green", "orange", "purple"]
for i in range(100000000):
    x.pencolor( colours[i % 5])
    x.forward(i)
    x.left(60)
    if i % 6 == 0 :
        x.left(20)
        
        
 
