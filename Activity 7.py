import turtle
import tkinter.simpledialog as simpledialog

# Setting up the window
window = turtle.Screen()
window.title("Turtle Graphics Illustration")
window.bgcolor("white")

# Creating a turtle
t = turtle.Turtle()

# Setting pen size to 3
t.pensize(3)

# Setting drawing color to blue
t.pencolor("blue")

# Moving the turtle forward by 100 units
t.forward(100)

# Turning the turtle right by 90 degrees
t.right(90)

# Moving the turtle forward by 50 units
t.forward(50)

# Turning the turtle left by 90 degrees
t.left(90)

# Lifting the pen up – no drawing when moving
t.penup()

# Moving the turtle to a specific location
t.goto(-50, 100)

# Putting the pen down – drawing when moving
t.pendown()

# Drawing a circle with radius of 25
t.circle(25)

# Drawing a dot with diameter 10
t.dot(10)

# Setting the turtle heading to 0 (East)
t.setheading(0)

# Changing the turtle color
t.color("red")

# Drawing a filled shape (e.g., a square)
t.begin_fill()
for _ in range(4):
    t.forward(50)
    t.left(90)
t.end_fill()

# Clearing the drawing
t.clear()

# Reseting the turtle's state
t.reset()

# Hiding the turtle
t.hideturtle()

# Displaying the turtle
t.showturtle()
