from tkinter import *

# ---------- Functions ----------

def submit():
    username = entry.get()
    print("Hello", username)

def delete():
    entry.delete(0, END)

def backspace():
    entry.delete(len(entry.get())-1, END)

# ---------- Window ----------

window = Tk()
window.title("Entry Widget Example")
window.geometry("600x200")

# ---------- Entry ----------

entry = Entry(
    window,
    font=("Arial", 40),
    bg="black",
    fg="white"
)

entry.insert(0, "Spongebob")   # default text
entry.pack(side=LEFT)

# ---------- Buttons ----------

submit_button = Button(window, text="Submit", command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window, text="Delete", command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window, text="Backspace", command=backspace)
backspace_button.pack(side=RIGHT)

# ---------- Main Loop ----------

window.mainloop()
