from tkinter import *


def btn_clicked():
    print("Button Clicked")
    
    
def mainPage():
    window.destroy()
    import main


def dashboardPage():
    window.destroy()
    import dashboard 

window = Tk()

window.geometry("630x715")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 715,
    width = 630,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"img/background.png")
background = canvas.create_image(
    286.0, 265.5,
    image=background_img)

img0 = PhotoImage(file = f"img/img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = dashboardPage,
    relief = "flat")

b0.place(
    x = 85, y = 621,
    width = 466,
    height = 64)

img1 = PhotoImage(file = f"img/img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = mainPage,
    relief = "flat")

b1.place(
    x = 42, y = 11,
    width = 69,
    height = 41)

entry0_img = PhotoImage(file = f"img/img_textBox0.png")
entry0_bg = canvas.create_image(
    314.5, 197.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry0.place(
    x = 94.0, y = 166,
    width = 441.0,
    height = 60)

entry1_img = PhotoImage(file = f"img/img_textBox1.png")
entry1_bg = canvas.create_image(
    314.5, 310.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry1.place(
    x = 94.0, y = 279,
    width = 441.0,
    height = 60)

entry2_img = PhotoImage(file = f"img/img_textBox2.png")
entry2_bg = canvas.create_image(
    314.5, 561.0,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry2.place(
    x = 94.0, y = 530,
    width = 441.0,
    height = 60)

entry3_img = PhotoImage(file = f"img/img_textBox3.png")
entry3_bg = canvas.create_image(
    116.0, 440.0,
    image = entry3_img)

entry3 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry3.place(
    x = 90.0, y = 409,
    width = 52.0,
    height = 60)

entry4_img = PhotoImage(file = f"img/img_textBox4.png")
entry4_bg = canvas.create_image(
    306.0, 440.0,
    image = entry4_img)

entry4 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry4.place(
    x = 280.0, y = 409,
    width = 52.0,
    height = 60)

entry5_img = PhotoImage(file = f"img/img_textBox5.png")
entry5_bg = canvas.create_image(
    499.0, 440.0,
    image = entry5_img)

entry5 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry5.place(
    x = 473.0, y = 409,
    width = 52.0,
    height = 60)

window.resizable(False, False)
window.mainloop()
