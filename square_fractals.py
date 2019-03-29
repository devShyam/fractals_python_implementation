import turtle as t

def square(x):
    for i in range(4):
        t.forward(x)
        t.left(90)

def recursion(x):
    k=t.position()
    square(x)
   
    square(x/3)
    if(x>10):
        recursion(x/3)
    t.penup()    
    t.forward(2*x/3)
    t.pendown()
    square(x/3)
    if(x>10):
        recursion(x/3)
        
    t.penup()
    t.left(90)
    t.forward(2*x/3)
    t.left(90)
    t.forward(2*x/3)
    t.left(180)
    t.pendown()
    
    
    square(x/3)
    if(x>10):
        recursion(x/3)
    t.penup()    
    t.forward(2*x/3)
    t.pendown()
    square(x/3)
    if(x>10):
        recursion(x/3)
    t.penup()
    t.setposition(k)
    t.pendown()

def main():
    t.speed(10000)
    t.penup()
    t.setposition(-300,-300)
    t.pendown()
    recursion(500)
main()
