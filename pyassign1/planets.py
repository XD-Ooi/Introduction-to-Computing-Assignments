"""
Author: 黄新迪 1700094621 元培学院
Python作业 Assign1 (Nov/6/2018)
"""

import turtle

def planet(t, color, size):
    """Create a planet with:
        t: name of planet, custom color, and custom size."""
    t.speed(0)
    t.pu()
    t.shape("circle")
    t.color(color)
    t.pencolor(color)
    t.shapesize(size,size)
    t.showturtle()

def orbit(t,r,step,x,y,num):
    """Let the planet orbit around the sun with:
        t: name of planet, r: radius from the center, 
        step: rank of relative speed among other planets,
        (x,y): initial position, and 
        num: input from global."""
    z = (num * step) % 361
    
    if z == 0 or z == 360:
        t.setpos(x,y)
        t.seth(0)
        t.right(45)
        t.pd()
    elif (0 < z <= 90) or (180 < z <= 270):
        t.circle(r,step)
    elif (90 < z <= 180) or (270 < z < 360):
        t.circle(r/3,step)
            
def main():
    turtle.screensize(500,500)
    turtle.bgcolor("black")
     
    mercury = turtle.Turtle()
    venus = turtle.Turtle()
    earth = turtle.Turtle()
    mars = turtle.Turtle()
    jupiter = turtle.Turtle()
    saturn = turtle.Turtle()
    sun = turtle.Turtle()
    
    planet(sun,"yellow",1.5)
    planet(mercury, "cornflowerblue", 0.4)
    planet(venus, "gold", 0.4)
    planet(earth, "aquamarine", 0.4)
    planet(mars, "red", 0.4)
    planet(jupiter, "lemon chiffon", 0.8)
    planet(saturn, "orange", 0.8)
    
    for num in range(10000):
        orbit(mercury,80,9,-60,-20,num)
        orbit(venus,110,6,-80,-30,num)
        orbit(earth,140,5,-100,-40,num)
        orbit(mars,170,3,-120,-50,num)
        orbit(jupiter,250,2,-180,-70,num)
        orbit(saturn,300,1,-210,-90,num)

if __name__ == '__main__':           
    main()
    
