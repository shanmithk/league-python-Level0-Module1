import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    fred = turtle.Turtle()
    fred.shape("turtle")
    # Ask the user what shape they want to draw and store it in a variable
    shape = simpledialog.askstring(title="choose", prompt="Would you like to draw a triangle, square, or circle?")
    # Draw the shape requested by the user using if-elif-else statements
    if shape == "triangle":
        for i in range(3):
            fred.forward(100)
            fred.left(120)
    elif shape == "square":
        for i in range(4):
            fred.forward(100)
            fred.left(90)
    elif shape == "circle":
        fred.circle(50)
    # Call the turtle .done() method
    turtle.done()
