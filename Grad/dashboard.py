from tkinter import *


def btn_clicked():
    print("Button Clicked")
    
    
def camera_clicked():
    import cam



def attendance_clicked():
    #window.destroy()
    import attend

window = Tk()

window.geometry("1040x733")
window.configure(bg = "#4d9982")
canvas = Canvas(
    window,
    bg = "#4d9982",
    height = 733,
    width = 1040,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"img/b1.png")
background = canvas.create_image(
    520.0, 366.5,
    image=background_img)

img0 = PhotoImage(file = f"img/b2.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = camera_clicked,
    relief = "flat")

b0.place(
    x = 57, y = 195,
    width = 24,
    height = 24)

img1 = PhotoImage(file = f"img/b3.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 61, y = 307,
    width = 24,
    height = 24)

img2 = PhotoImage(file = f"img/b4.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = 60, y = 145,
    width = 24,
    height = 24)

img3 = PhotoImage(file = f"img/b5.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b3.place(
    x = 153, y = 495,
    width = 66,
    height = 36)

img4 = PhotoImage(file = f"img/b6.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = attendance_clicked,
    relief = "flat")

b4.place(
    x = 61, y = 251,
    width = 19,
    height = 24)

window.resizable(False, False)
window.mainloop()
