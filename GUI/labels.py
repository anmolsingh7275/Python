# from tkinter import *

# window = Tk()

# label = Label(window, text="Hello World", font = {'Arial',40})
# label.place(x=0, y=0)

# window.mainloop()

from tkinter import *

window = Tk()
window.title("Label All Options Example")
window.geometry("400x300")
window.config(bg="lightblue")

# Load image (must be .png or .gif)
icon = PhotoImage(file= r"blackwallpaper.png")

label = Label(
    window,
    text="Hello Anmol",
    font=("Arial", 20, "bold"),
    fg="white",
    bg="black",
    padx=20,
    pady=20,
    image=icon,
    compound="top"   # image on top, text below
)

label.pack(pady=40)

window.mainloop()
