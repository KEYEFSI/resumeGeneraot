
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\ADMIN\Desktop\3E FILES\RESUMEGENERATOR\pythonProject2\create_interface\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("800x400")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 400,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    400.0,
    200.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    374.0,
    53.0,
    image=image_image_2
)

canvas.create_text(
    356.0,
    106.0,
    anchor="nw",
    text="CREATE ACCOUNT",
    fill="#06314C",
    font=("Unlock Regular", 32 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    646.5,
    176.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=544.5,
    y=159.0,
    width=204.0,
    height=33.0
)

canvas.create_text(
    550.0,
    147.0,
    anchor="nw",
    text="USERNAME",
    fill="#000000",
    font=("PaytoneOne Regular", 12 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    644.5,
    225.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=542.5,
    y=208.0,
    width=204.0,
    height=33.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    646.5,
    273.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=544.5,
    y=256.0,
    width=204.0,
    height=33.0
)

canvas.create_text(
    550.0,
    195.0,
    anchor="nw",
    text="PASSWORD",
    fill="#000000",
    font=("PaytoneOne Regular", 12 * -1)
)

canvas.create_text(
    549.0,
    243.0,
    anchor="nw",
    text="CONFIRM PASSWORD",
    fill="#000000",
    font=("PaytoneOne Regular", 12 * -1)
)

canvas.create_text(
    527.0,
    354.0,
    anchor="nw",
    text="I have an account",
    fill="#000000",
    font=("PaytoneOne Regular", 14 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=676.0,
    y=354.0,
    width=102.0,
    height=30.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=516.0,
    y=294.0,
    width=262.0,
    height=50.0
)
window.resizable(False, False)
window.mainloop()