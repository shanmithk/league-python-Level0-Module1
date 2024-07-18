"""
* Write a Python program that asks the user for two numbers.

* Display the sum of the two numbers to the user
"""
from tkinter import simpledialog, Tk, messagebox

window = Tk()
window.withdraw()
if __name__ == '__main__':
    num1 = simpledialog.askinteger(title="num1", prompt="Enter a number.")
    num2 = simpledialog.askinteger(title="num1", prompt="Enter another number.")
    sum = num1 + num2
    messagebox.showinfo(message="The sum of your 2 numbers is " + str(sum))
