import turtle as t
def triangle(x):
    t.speed(100000)
    for i in range(3):
        t.forward(x)
        t.left(120)
        
def recure(x):
        k=t.position()
        triangle(x)
        triangle(x/2)
        if(x>10):
            recure(x//2)
            
        t.forward(x/2)
        triangle(x/2)
        if(x>10):
            recure(x//2)
        t.penup()
        t.left(120)
        t.forward(x/2)
        t.right(120)
        t.pendown()
        triangle(x/2)
    
        if(x>10):
            recure(x//2)
        t.setposition(k)
    
def main():
    t.hideturtle()
    t.tracer(1,0.25)
    x=700
    t.penup()
    t.setposition(-300,-300)
    t.pendown()
    recure(x)
    

main()
