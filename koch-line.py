import turtle

# How many recursions you want the Koch line to have
line_depth = 6

# Size of the canvas
canv_length = 300

# Length of the base Koch line 
line_length = 900

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
len_drawn = [0]

def koch_line(length, level):
    if (level == 1):
        my_turtle.forward(length)
        len_drawn[0] += length
    else:
        koch_line(length / 3, level - 1)
        my_turtle.left(60)
        koch_line(length / 3, level - 1)
        my_turtle.right(120)
        koch_line(length / 3, level - 1)
        my_turtle.left(60)
        koch_line(length / 3, level - 1)

koch_line(line_length, line_depth)
print(f'In all, we have drawn koch lines of total length {round(len_drawn[0], 2)}')
print('Done!')
turtle.done()
