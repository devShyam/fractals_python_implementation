import turtle as t
n=2

def mini(x):
    if(x/n >4):
        tree(x/n)
        t.left(60)
        
def sett(k):
    t.penup()
    t.setposition(k)
    t.pendown()
    
def branch(x):
     s=t.position()
     t.forward(3*x/4)
     

def tree(x):
    t.pensize(width=x/10)
    
    s=t.position()
    t.right(22.5)
    branch(x)
    if(3*x/4 >10):
        tree(3*x/4)
    sett(s)
    t.pensize(width=x/10)
    t.left(45)
    
    branch(x)
    if(3*x/4 >10):
        tree(3*x/4)
    t.right(22.5)
    sett(s)

    
    
def main():
    i=150
    t.tracer(1,0.25)
    t.hideturtle()
    sett([0,-300])
    s=t.position()
    t.left(90)
    t.pensize(width=i/9)
    t.forward(i)
    tree(i)
    
    
        
       
main()
