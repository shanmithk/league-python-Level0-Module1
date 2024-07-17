from tkinter import simpledialog, Tk, messagebox

if __name__ == '__main__':
    window = Tk()
    window.withdraw
    birthday = simpledialog.askstring(title="birthday", prompt="What is your birthday?(for example, 09/24)")

    if birthday == "06/17" or birthday == "6/17":
        message = "I wish you a very happy birthday."
        messagebox.showinfo(title="bday", message=message)
    else:
        message = "I wish you a very happy unbirthday!"
        messagebox.showinfo(title="bday", message=message)
