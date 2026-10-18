import time
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("300x250")
root.title("Kitchen Timer")

minute = StringVar()
second = StringVar()

minute.set("00")
second.set("00")

# Labels
minuteLabel = Label(root, textvariable=minute, width=3, font=("Arial", 25))
minuteLabel.place(x=80, y=20)

secondLabel = Label(root, textvariable=second, width=3, font=("Arial", 25))
secondLabel.place(x=130, y=20)

def soft():
    temp = 180
    while temp > -1:
        mins, secs = divmod(temp, 60)

        minute.set(f"{mins:2d}")
        second.set(f"{secs:2d}")

        root.update()
        time.sleep(1)

        if temp == 0:
            messagebox.showinfo("Egg Status", "Eggs are done cooking!")

        temp -= 1

def medium():
    temp = 300
    while temp > -1:
        mins, secs = divmod(temp, 60)

        minute.set(f"{mins:2d}")
        second.set(f"{secs:2d}")

        root.update()
        time.sleep(1)

        if temp == 0:
            messagebox.showinfo("Egg Status", "Eggs are done cooking!")

        temp -= 1

def hard():
    temp = 600
    while temp > -1:
        mins, secs = divmod(temp, 60)

        minute.set(f"{mins:2d}")
        second.set(f"{secs:2d}")

        root.update()
        time.sleep(1)

        if temp == 0:
            messagebox.showinfo("Egg Status", "Eggs are done cooking!")

        temp -= 1

softButton = Button(root, text="Soft Boiled (3 mins)", width=15, font=("Arial", 10), command=soft)
softButton.place(x=65, y=60)

mediumButton = Button(root, text="Medium (5 mins)", width=15, font=("Arial", 10), command=medium)
mediumButton.place(x=65, y=100)

hardButton = Button(root, text="Hard Boiled (10 mins)", width=15, font=("Arial", 10), command=hard)
hardButton.place(x=65, y=140)

root.mainloop()