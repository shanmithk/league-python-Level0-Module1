"""
* Write a python program that asks the user a minimum of 3 riddles.

* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got
  correct
"""
from tkinter import simpledialog, Tk, messagebox

if __name__ == '__main__':
    score = 0
    window = Tk()
    window.withdraw()
    rid1 = simpledialog.askstring(title="rid1", prompt="What is more useful when it is broken?")
    if rid1 == "egg":
        score = score + 1
    rid2 = simpledialog.askstring(title="rid1", prompt="David's father has three sons: Snap, Crackle, and _____")
    if rid2 == "david":
        score = score + 1
    rid3 = simpledialog.askstring(title="rid1", prompt="What belongs to you but is used more by others?")
    if rid3 == "name":
        score = score + 1
    messagebox.showinfo(message="Your final score is " + str(score))


