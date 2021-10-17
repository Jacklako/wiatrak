from turtle import*
from math import sqrt
speed(0)
b= 25
x= b/2
for i in range (6):
    fillcolor('red')
    begin_fill()
    b= 25
    
    fd (10*b)
    b*sqrt(2)
    rt(90)
    fd (3*b)
    rt (180-45)
    fd (3*b*sqrt(2))
    fd (2*b*sqrt(2))
    lt(180-45)
    fd (3*b)
    rt (180-45)
    fd(b*sqrt(2))
    end_fill()
    lt(45)
    fd(4*b)
    lt (180)
    rt (60)

rt (30)
for j in range (6):
    fillcolor('green')
    begin_fill()
    fd (10*x)
    b*sqrt(2)
    lt(90)
    fd (3*x)
    lt (180-45)
    fd (3*x*sqrt(2))
    fd (2*x*sqrt(2))
    rt(180-45)
    fd (3*x)
    lt (180-45)
    fd(x*sqrt(2))
    end_fill()
    rt(45)
    fd(4*x)
    rt (180)
    rt (60)

    
