import turtle
import math

# How many recursions you want the Koch line to have
line_depth = 6

# Size of the canvas
canv_length = 300

# Length of the base Koch line 
line_length = 900

# Whether you want to just write a koch line or the full koch snowflake
draw_snowflake = True

my_turtle = turtle.Turtle()
my_turtle.pencolor('white')
my_turtle.width(2)
my_turtle.hideturtle()

my_screen = turtle.Screen()
my_screen.screensize(canv_length, canv_length, '#2d2d2d')

my_turtle.penup()
my_turtle.backward(line_length / 2);
my_turtle.pendown()

# The total length of line that has been drawn
len_drawn = 0

def koch_line(length, level):
    global len_drawn
    if (level == 1):
        my_turtle.forward(length)
        len_drawn += length
    else:
        koch_line(length / 3, level - 1)
        my_turtle.left(60)
        koch_line(length / 3, level - 1)
        my_turtle.right(120)
        koch_line(length / 3, level - 1)
        my_turtle.left(60)
        koch_line(length / 3, level - 1)

def koch_snowflake(length, level):
    for i in range(3):
        koch_line(length, level)
        my_turtle.right(120)

if (draw_snowflake):
    my_turtle.left(90)
    my_turtle.penup()
    my_turtle.forward(canv_length / 2)
    my_turtle.pendown()
    my_turtle.right(90)
    koch_snowflake(line_length, line_depth)
else:
    koch_line(line_length, line_depth)
print(f'In all, we have drawn koch lines of total length {round(len_drawn, 2)}')
print('Done!')
turtle.done()
