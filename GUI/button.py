from tkinter import *

window = Tk()
window.geometry("300x200")

def change_text():
    label.config(text="Button Clicked!")

label = Label(window, text="Hello")
label.pack(pady=10)

button = Button(window, text="Click Me", command=change_text)
button.pack()


window.mainloop()

