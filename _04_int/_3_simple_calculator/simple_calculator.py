"""
* Write a Python program that asks the user for two numbers.

* Then ask the user if the would like to add, subtract, multiply, or divide.

* Use if-else statements to provide the desired math operation on the numbers
  and display the result.
"""



from tkinter import simpledialog, Tk, messagebox

window = Tk()
window.withdraw()
if __name__ == '__main__':
    num1 = simpledialog.askinteger(title="num1", prompt="enter a number.")
    num2 = simpledialog.askinteger(title="num1", prompt="enter another number.")
    sign = simpledialog.askstring(title="sign", prompt="Would you like add, subtract, divide, multiply your 2 number")
    if sign == "add":
        messagebox.showinfo(message="The sum of your 2 numbers is " + str(num1 + num2))
    elif sign == "subtract":
        messagebox.showinfo(message="The sum of your 2 numbers is " + str(num1 - num2))
    elif sign == "multiply":
        messagebox.showinfo(message="The sum of your 2 numbers is " + str(num1 * num2))
    elif sign == "divide":
        messagebox.showinfo(message="The sum of your 2 numbers is " + str(num1/num2))

