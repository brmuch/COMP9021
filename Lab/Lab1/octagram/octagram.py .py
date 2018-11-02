
# coding: utf-8

# In[77]:


'''
Draws a dodecadon with the colour of each sector alternating red and blue.
'''


from turtle import *

angle = 45

def draw_triangle(i, colour):
    color(colour)
    goto(vertices[i])
    begin_fill()
    goto(circles[i])
    goto(vertices[i + 1]) 
    end_fill()
 
    
def fill_in_triangle(i):
    home()
    pendown()
    color("yellow")
    begin_fill()
    goto(vertices[i])
    goto(vertices[i + 1]) 
    end_fill()
    penup()


vertices = []
circles = []
penup()
speed(8)

for i in range(8):
    right(i * angle)
    forward(100)
    vertices.append(pos())
    home()
    

for i in range(8):
    right(i*angle+22.5)
    forward(180)
    circles.append(pos())
    home()

vertices.append(vertices[0])
pendown()

for i in range(8):
    home()
    fill_in_triangle(i)
    colour = 'red' if i % 2 else 'blue'
    draw_triangle(i, colour)
    

