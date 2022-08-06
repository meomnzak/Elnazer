from tkinter import *


def btn_clicked():
    print("Button Clicked")

def examPage():
    window.destroy()
    import examData


def signPage():
    window.destroy()
    import sign
    

window = Tk()

window.geometry("1170x645")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 645,
    width = 1170,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"img/backgroundM.png")
background = canvas.create_image(
    937.5, 276.0,
    image=background_img)

img0 = PhotoImage(file = f"img/img0M.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = signPage,
    relief = "flat")

b0.place(
    x = 658, y = 537,
    width = 164,
    height = 35)

img1 = PhotoImage(file = f"img/img1M.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = examPage,
    relief = "flat")

b1.place(
    x = 79, y = 537,
    width = 203,
    height = 35)

window.resizable(False, False)
window.mainloop()
