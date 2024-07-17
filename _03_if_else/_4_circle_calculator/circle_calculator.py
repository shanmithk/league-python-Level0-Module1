# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.
import math
from tkinter import simpledialog, messagebox, Tk

window = Tk()
window.withdraw()


if __name__ == '__main__':
    radii = simpledialog.askinteger(title="area", prompt="Enter a radius for a circle.")
    calc = simpledialog.askstring(title="perim", prompt="Would you like to find the area or circumference of the circle.")
    area = radii * radii * math.pi
    circum = 2 * math.pi * radii
    if calc == "area":
        messagebox.showinfo(message="The area of your circle is " + str(area))
    elif calc == "circumference":
        messagebox.showinfo(message="The circumference of your circle is " + str(circum))




#Area = πr^2
#Circumference = 2πr
