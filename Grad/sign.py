from tkinter import *


def btn_clicked():
    print("Button Clicked")
    
    



window = Tk()

window.geometry("605x550")
window.configure(bg = "#e5e5e5")
canvas = Canvas(
    window,
    bg = "#e5e5e5",
    height = 550,
    width = 605,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"img/a1.png")
background = canvas.create_image(
    403.0, 304.0,
    image=background_img)

img0 = PhotoImage(file = f"img/a2.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 151, y = 353,
    width = 300,
    height = 45)

entry0_img = PhotoImage(file = f"img/a3.png")
entry0_bg = canvas.create_image(
    299.0, 199.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#68daff",
    highlightthickness = 0)

entry0.place(
    x = 161.0, y = 177,
    width = 276.0,
    height = 43)

entry1_img = PhotoImage(file = f"img/a4.png")
entry1_bg = canvas.create_image(
    299.0, 274.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#68daff",
    highlightthickness = 0)

entry1.place(
    x = 161.0, y = 252,
    width = 276.0,
    height = 43)

window.resizable(False, False)
window.mainloop()
