
# coding: utf-8

# In[9]:


import turtle as t
import time

t.pensize(3)
t.penup()
t.goto(-100,170)
t.pendown()
t.color("red", "blue")
t.speed(5)
t.setheading(60)
t.begin_fill()

for _ in range(3):  
    t.forward(100)
    t.right(120)
    t.forward(100)
    t.right(300)
    t.color("blue")
    t.forward(100)
    t.right(120)
    t.forward(100)
    t.right(300)
    t.color("red")
    
end_fill()
time.sleep(1)

