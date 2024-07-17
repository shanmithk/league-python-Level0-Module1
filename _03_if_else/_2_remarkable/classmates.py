from tkinter import simpledialog, messagebox, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    name = simpledialog.askstring(title="input", prompt="What is your name")
    if name == "joe":
        messagebox.showinfo(message="You are cool")
    if name == "shanmith":
        messagebox.showinfo(message="You are awsome")
    if name == "rob":
        messagebox.showinfo(message="You are amazing")




