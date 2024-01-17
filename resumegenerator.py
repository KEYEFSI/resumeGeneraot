from tkinter import *
from tkinter import messagebox
import sqlite3
from datetime import date
from tkinter import filedialog
import os
from tkinter.ttk import Combobox
from pathlib import Path
from tkinter import messagebox
import sqlite3



def userinterface():
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(
        r"C:\Users\ADMIN\Desktop\3E FILES\RESUMEGENERATOR\pythonProject2\user_interface\build\assets\frame0")
    def createresume():
        window.destroy()
        inputcontext()
    def backlogin():
        window.destroy()
        login()
    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    window = Tk()

    window.geometry("800x400")
    window.configure(bg="#FFFFFF")

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=400,
        width=800,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
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
        276.0,
        112.0,
        image=image_image_2
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=createresume,
        relief="flat"
    )
    button_1.place(
        x=244.0,
        y=180.0,
        width=339.0,
        height=123.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=backlogin,
        relief="flat"
    )
    button_2.place(
        x=735.0,
        y=0.0,
        width=65.0,
        height=62.0
    )
    window.resizable(False, False)
    window.mainloop()

def viewresume():
    window = Tk()
    window.title("CREATE RESUME")
    window.geometry('800x1000+500+0')
    window.config(bg='#5ED2E5')
    window.resizable(False, False)
    img = PhotoImage(file='resume1.png')
    frame = Frame(window, width=700, height=1170, bg=img)
    frame.place(x=10, y=10)

    heading = Label(frame, text='CREATE RESUME', fg='black', bg='#5ED2E5',
                    font=('Microsoft Times New Roman', 16, 'bold'))
    heading.place(x=300, y=10)


def inputcontext():
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(
        r"C:\Users\ADMIN\Desktop\3E FILES\RESUMEGENERATOR\pythonProject2\inputcredentials\build\assets\frame0")
    def save():
        saving_info()
        window.destroy()
        viewresume()
    def create_table(conn):
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS resume (
                name TEXT,
                phone_number TEXT,
                email TEXT,
                job TEXT,
                place_address TEXT,
                firstwork TEXT,
                firstdate TEXT,
                secondwork TEXT,
                seconddate TEXT,
                thirdwork TEXT,
                thirddate TEXT,
                aboutme TEXT,
                skills1 TEXT,
                skills2 TEXT,
                skills3 TEXT,
                skills4 TEXT,
                skills5 TEXT,
                skills6 TEXT,
                primaryeduc TEXT,
                primarydate TEXT,
                secondaryeduc TEXT,
                secondarydate TEXT,
                tertiaryeduc TEXT,
                tertiarydate TEXT 
            )
        ''')
        conn.commit()


    def insert_data(conn, data):
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO resume VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', data)
        conn.commit()

    def update_data(conn, name, new_data):
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE resume
            SET phone_number=?, email=?, job=?, place_address=?, firstwork=?, firstdate=?, 
                secondwork=?, seconddate=?, thirdwork=?, thirddate=?, aboutme=?, skills1=?, 
                skills2=?, skills3=?, skills4=?, skills5=?, skills6=?, primaryeduc=?, primarydate=?, 
                secondaryeduc=?, secondarydate=?, tertiaryeduc=?, tertiarydate=?
            WHERE name=?
        ''', (*new_data, name))
        conn.commit()

    def saving_info():
        name = fullname.get()
        phone_number = phonenumber.get()
        email = emailadd.get()
        job = work.get()
        place_address = address.get()
        firstwork = exp1.get()
        firstdate = date1.get()
        secondwork = exp2.get()
        seconddate = date2.get()
        thirdwork = exp3.get()
        thirddate = date3.get()
        aboutme = about.get()
        skills1 = skill1.get()
        skills2 = skill2.get()
        skills3 = skill3.get()
        skills4 = skill4.get()
        skills5 = skill5.get()
        skills6 = skill6.get()
        primaryeduc = primary.get()
        primarydate = primary_year.get()
        secondaryeduc = secondary.get()
        secondarydate = secondary_year.get()
        tertiaryeduc = tertiary.get()
        tertiarydate = tertiary_year.get()

        db_path = Path('resumecredentials.db')
        conn = sqlite3.connect(db_path)

        create_table(conn)

        resume_data = (name, phone_number, email, job, place_address, firstwork, firstdate,
            secondwork, seconddate, thirdwork, thirddate, aboutme, skills1, skills2,
            skills3, skills4, skills5, skills6, primaryeduc, primarydate, secondaryeduc,
            secondarydate, tertiaryeduc, tertiarydate
        )

        cursor = conn.cursor()
        cursor.execute('SELECT * FROM resume WHERE name=?', (name,))
        existing_record = cursor.fetchone()

        if existing_record:
            update_data(conn, name, resume_data[1:])
        else:
            insert_data(conn, resume_data)

        conn.close()
        messagebox.showinfo("", "Record inserted successfully!")

    def backtointerface():
        window.destroy()
        userinterface()
    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    window = Tk()

    window.geometry("1200x850")
    window.configure(bg="#FFFFFF")

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=850,
        width=1200,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        600.0,
        428.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        95.0,
        419.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        95.0,
        471.0,
        image=image_image_3
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        588.0,
        627.0,
        image=image_image_4
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        588.0,
        293.0,
        image=image_image_5
    )

    image_image_6 = PhotoImage(
        file=relative_to_assets("image_6.png"))
    image_6 = canvas.create_image(
        152.0,
        67.0,
        image=image_image_6
    )

    image_image_7 = PhotoImage(
        file=relative_to_assets("image_7.png"))
    image_7 = canvas.create_image(
        214.0,
        668.0,
        image=image_image_7
    )

    image_image_8 = PhotoImage(
        file=relative_to_assets("image_8.png"))
    image_8 = canvas.create_image(
        213.0,
        335.0,
        image=image_image_8
    )

    image_image_9 = PhotoImage(
        file=relative_to_assets("image_9.png"))
    image_9 = canvas.create_image(
        967.0,
        497.0,
        image=image_image_9
    )

    canvas.create_text(
        116.0,
        191.0,
        anchor="nw",
        text="BASIC INFORMATION",
        fill="#FFFFFF",
        font=("OverpassRoman Bold", 24 * -1)
    )

    canvas.create_text(
        870.0,
        324.0,
        anchor="nw",
        text="WORK EXPERIENCES",
        fill="#000000",
        font=("OverpassRoman Bold", 24 * -1)
    )

    canvas.create_text(
        129.0,
        540.0,
        anchor="nw",
        text="OBJECTIVES",
        fill="#000000",
        font=("OverpassRoman Bold", 24 * -1)
    )

    canvas.create_text(
        79.0,
        240.0,
        anchor="nw",
        text="FULL NAME",
        fill="#1E1E1E",
        font=("OverpassRoman Bold", 12 * -1)
    )

    canvas.create_text(
        812.0,
        379.0,
        anchor="nw",
        text="TYPE OF WORK",
        fill="#1E1E1E",
        font=("OverpassRoman Bold", 12 * -1)
    )

    canvas.create_text(
        404.0,
        490.0,
        anchor="nw",
        text="PRIMARY EDUCATION",
        fill="#1E1E1E",
        font=("OverpassRoman Bold", 12 * -1)
    )

    canvas.create_text(
        404.0,
        600.0,
        anchor="nw",
        text="SECONDARY EDUCATION",
        fill="#1E1E1E",
        font=("OverpassRoman Bold", 12 * -1)
    )

    canvas.create_text(
        404.0,
        704.0,
        anchor="nw",
        text="TERTIARY EDUCATION",
        fill="#1E1E1E",
        font=("OverpassRoman Bold", 12 * -1)
    )

    canvas.create_text(
        812.0,
        479.0,
        anchor="nw",
        text="TYPE OF WORK",
        fill="#1E1E1E",
        font=("OverpassRoman Bold", 12 * -1)
    )

    canvas.create_text(
        812.0,
        579.0,
        anchor="nw",
        text="TYPE OF WORK",
        fill="#1E1E1E",
        font=("OverpassRoman Bold", 12 * -1)
    )

    canvas.create_text(
        851.0,
        428.0,
        anchor="nw",
        text="DATE",
        fill="#1E1E1E",
        font=("OverpassRoman Bold", 12 * -1)
    )

    canvas.create_text(
        475.0,
        571.0,
        anchor="nw",
        text="DATE",
        fill="#1E1E1E",
        font=("OverpassRoman Bold", 12 * -1)
    )

    canvas.create_text(
        475.0,
        678.0,
        anchor="nw",
        text="DATE",
        fill="#1E1E1E",
        font=("OverpassRoman Bold", 12 * -1)
    )

    canvas.create_text(
        475.0,
        785.0,
        anchor="nw",
        text="DATE",
        fill="#1E1E1E",
        font=("OverpassRoman Bold", 12 * -1)
    )

    canvas.create_text(
        851.0,
        528.0,
        anchor="nw",
        text="DATE",
        fill="#1E1E1E",
        font=("OverpassRoman Bold", 12 * -1)
    )

    canvas.create_text(
        851.0,
        628.0,
        anchor="nw",
        text="DATE",
        fill="#1E1E1E",
        font=("OverpassRoman Bold", 12 * -1)
    )

    canvas.create_text(
        79.0,
        290.0,
        anchor="nw",
        text="PHONE NUMBER",
        fill="#1E1E1E",
        font=("OverpassRoman Bold", 12 * -1)
    )

    canvas.create_text(
        79.0,
        340.0,
        anchor="nw",
        text="EMAIL ADDRESS",
        fill="#1E1E1E",
        font=("OverpassRoman Bold", 12 * -1)
    )

    canvas.create_text(
        79.0,
        390.0,
        anchor="nw",
        text="JOB OR SPECIALICATION",
        fill="#1E1E1E",
        font=("OverpassRoman Bold", 12 * -1)
    )

    canvas.create_text(
        79.0,
        440.0,
        anchor="nw",
        text="ADDRESS",
        fill="#1E1E1E",
        font=("OverpassRoman Bold", 12 * -1)
    )

    canvas.create_text(
        444.0,
        118.0,
        anchor="nw",
        text="INPUT CREDENTIALS",
        fill="#FFFFFF",
        font=("OverpassRoman Bold", 36 * -1)
    )

    image_image_10 = PhotoImage(
        file=relative_to_assets("image_10.png"))
    image_10 = canvas.create_image(
        95.0,
        269.0,
        image=image_image_10
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        217.0,
        690.5,
        image=entry_image_1
    )
    about = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    about.place(
        x=91.0,
        y=579.0,
        width=252.0,
        height=221.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        227.0,
        270.0,
        image=entry_image_2
    )
    fullname = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    fullname.place(
        x=127.0,
        y=255.0,
        width=200.0,
        height=28.0
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        499.0,
        262.0,
        image=entry_image_3
    )
    skill1 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    skill1.place(
        x=429.0,
        y=242.0,
        width=140.0,
        height=38.0
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        687.0,
        262.0,
        image=entry_image_4
    )
    skill4 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    skill4.place(
        x=617.0,
        y=242.0,
        width=140.0,
        height=38.0
    )

    entry_image_5 = PhotoImage(
        file=relative_to_assets("entry_5.png"))
    entry_bg_5 = canvas.create_image(
        499.0,
        320.5,
        image=entry_image_5
    )
    skill2 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    skill2.place(
        x=428.5,
        y=301.0,
        width=141.0,
        height=37.0
    )

    entry_image_6 = PhotoImage(
        file=relative_to_assets("entry_6.png"))
    entry_bg_6 = canvas.create_image(
        687.0,
        320.5,
        image=entry_image_6
    )
    skill5 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    skill5.place(
        x=616.5,
        y=301.0,
        width=141.0,
        height=37.0
    )

    entry_image_7 = PhotoImage(
        file=relative_to_assets("entry_7.png"))
    entry_bg_7 = canvas.create_image(
        499.0,
        378.0,
        image=entry_image_7
    )
    skill3 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    skill3.place(
        x=429.0,
        y=358.0,
        width=140.0,
        height=38.0
    )

    entry_image_8 = PhotoImage(
        file=relative_to_assets("entry_8.png"))
    entry_bg_8 = canvas.create_image(
        687.0,
        378.0,
        image=entry_image_8
    )
    skill6 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    skill6.place(
        x=617.0,
        y=358.0,
        width=140.0,
        height=38.0
    )

    entry_image_9 = PhotoImage(
        file=relative_to_assets("entry_9.png"))
    entry_bg_9 = canvas.create_image(
        974.5,
        409.5,
        image=entry_image_9
    )
    exp1 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    exp1.place(
        x=868.5,
        y=394.0,
        width=212.0,
        height=29.0
    )

    entry_image_10 = PhotoImage(
        file=relative_to_assets("entry_10.png"))
    entry_bg_10 = canvas.create_image(
        608.5,
        532.0,
        image=entry_image_10
    )
    primary = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    primary.place(
        x=474.0,
        y=507.0,
        width=269.0,
        height=48.0
    )

    entry_image_11 = PhotoImage(
        file=relative_to_assets("entry_11.png"))
    entry_bg_11 = canvas.create_image(
        608.5,
        639.0,
        image=entry_image_11
    )
    secondary = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    secondary.place(
        x=474.0,
        y=614.0,
        width=269.0,
        height=48.0
    )

    entry_image_12 = PhotoImage(
        file=relative_to_assets("entry_12.png"))
    entry_bg_12 = canvas.create_image(
        608.5,
        746.0,
        image=entry_image_12
    )
    tertiary = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    tertiary.place(
        x=474.0,
        y=721.0,
        width=269.0,
        height=48.0
    )

    entry_image_13 = PhotoImage(
        file=relative_to_assets("entry_13.png"))
    entry_bg_13 = canvas.create_image(
        974.5,
        509.5,
        image=entry_image_13
    )
    exp2 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    exp2.place(
        x=868.5,
        y=494.0,
        width=212.0,
        height=29.0
    )

    entry_image_14 = PhotoImage(
        file=relative_to_assets("entry_14.png"))
    entry_bg_14 = canvas.create_image(
        974.5,
        609.5,
        image=entry_image_14
    )
    exp3 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    exp3.place(
        x=868.5,
        y=594.0,
        width=212.0,
        height=29.0
    )

    entry_image_15 = PhotoImage(
        file=relative_to_assets("entry_15.png"))
    entry_bg_15 = canvas.create_image(
        978.5,
        459.0,
        image=entry_image_15
    )
    date1 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    date1.place(
        x=876.0,
        y=444.0,
        width=205.0,
        height=28.0
    )

    entry_image_16 = PhotoImage(
        file=relative_to_assets("entry_16.png"))
    entry_bg_16 = canvas.create_image(
        638.0,
        577.0,
        image=entry_image_16
    )
    primary_year = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    primary_year.place(
        x=528.0,
        y=562.0,
        width=220.0,
        height=28.0
    )

    entry_image_17 = PhotoImage(
        file=relative_to_assets("entry_17.png"))
    entry_bg_17 = canvas.create_image(
        638.0,
        684.0,
        image=entry_image_17
    )
    secondary_year = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    secondary_year.place(
        x=528.0,
        y=669.0,
        width=220.0,
        height=28.0
    )

    entry_image_18 = PhotoImage(
        file=relative_to_assets("entry_18.png"))
    entry_bg_18 = canvas.create_image(
        638.0,
        791.0,
        image=entry_image_18
    )
    tertiary_year = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    tertiary_year.place(
        x=528.0,
        y=776.0,
        width=220.0,
        height=28.0
    )

    entry_image_19 = PhotoImage(
        file=relative_to_assets("entry_19.png"))
    entry_bg_19 = canvas.create_image(
        978.5,
        559.0,
        image=entry_image_19
    )
    date2 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    date2.place(
        x=876.0,
        y=544.0,
        width=205.0,
        height=28.0
    )

    entry_image_20 = PhotoImage(
        file=relative_to_assets("entry_20.png"))
    entry_bg_20 = canvas.create_image(
        978.5,
        659.0,
        image=entry_image_20
    )
    date3 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    date3.place(
        x=876.0,
        y=644.0,
        width=205.0,
        height=28.0
    )

    entry_image_21 = PhotoImage(
        file=relative_to_assets("entry_21.png"))
    entry_bg_21 = canvas.create_image(
        227.0,
        320.0,
        image=entry_image_21
    )
    phonenumber = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    phonenumber.place(
        x=127.0,
        y=305.0,
        width=200.0,
        height=28.0
    )

    entry_image_22 = PhotoImage(
        file=relative_to_assets("entry_22.png"))
    entry_bg_22 = canvas.create_image(
        227.0,
        370.0,
        image=entry_image_22
    )
    emailadd = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    emailadd.place(
        x=127.0,
        y=355.0,
        width=200.0,
        height=28.0
    )

    entry_image_23 = PhotoImage(
        file=relative_to_assets("entry_23.png"))
    entry_bg_23 = canvas.create_image(
        227.0,
        470.0,
        image=entry_image_23
    )
    address = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    address.place(
        x=127.0,
        y=455.0,
        width=200.0,
        height=28.0
    )

    entry_image_24 = PhotoImage(
        file=relative_to_assets("entry_24.png"))
    entry_bg_24 = canvas.create_image(
        227.0,
        420.0,
        image=entry_image_24
    )
    work = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    work.place(
        x=127.0,
        y=405.0,
        width=200.0,
        height=28.0
    )

    image_image_11 = PhotoImage(
        file=relative_to_assets("image_11.png"))
    image_11 = canvas.create_image(
        95.0,
        367.0,
        image=image_image_11
    )

    image_image_12 = PhotoImage(
        file=relative_to_assets("image_12.png"))
    image_12 = canvas.create_image(
        95.0,
        319.0,
        image=image_image_12
    )

    image_image_13 = PhotoImage(
        file=relative_to_assets("image_13.png"))
    image_13 = canvas.create_image(
        92.0,
        546.0,
        image=image_image_13
    )

    image_image_14 = PhotoImage(
        file=relative_to_assets("image_14.png"))
    image_14 = canvas.create_image(
        87.0,
        203.0,
        image=image_image_14
    )

    image_image_15 = PhotoImage(
        file=relative_to_assets("image_15.png"))
    image_15 = canvas.create_image(
        840.0,
        334.0,
        image=image_image_15
    )

    image_image_16 = PhotoImage(
        file=relative_to_assets("image_16.png"))
    image_16 = canvas.create_image(
        845.0,
        457.0,
        image=image_image_16
    )

    image_image_17 = PhotoImage(
        file=relative_to_assets("image_17.png"))
    image_17 = canvas.create_image(
        454.0,
        577.0,
        image=image_image_17
    )

    image_image_18 = PhotoImage(
        file=relative_to_assets("image_18.png"))
    image_18 = canvas.create_image(
        454.0,
        684.0,
        image=image_image_18
    )

    image_image_19 = PhotoImage(
        file=relative_to_assets("image_19.png"))
    image_19 = canvas.create_image(
        454.0,
        791.0,
        image=image_image_19
    )

    image_image_20 = PhotoImage(
        file=relative_to_assets("image_20.png"))
    image_20 = canvas.create_image(
        845.0,
        557.0,
        image=image_image_20
    )

    image_image_21 = PhotoImage(
        file=relative_to_assets("image_21.png"))
    image_21 = canvas.create_image(
        845.0,
        657.0,
        image=image_image_21
    )

    image_image_22 = PhotoImage(
        file=relative_to_assets("image_22.png"))
    image_22 = canvas.create_image(
        834.0,
        413.0,
        image=image_image_22
    )

    image_image_23 = PhotoImage(
        file=relative_to_assets("image_23.png"))
    image_23 = canvas.create_image(
        834.0,
        513.0,
        image=image_image_23
    )

    image_image_24 = PhotoImage(
        file=relative_to_assets("image_24.png"))
    image_24 = canvas.create_image(
        834.0,
        613.0,
        image=image_image_24
    )

    canvas.create_text(
        468.0,
        449.0,
        anchor="nw",
        text="EDUCATION",
        fill="#FFFFFF",
        font=("OverpassRoman Bold", 24 * -1)
    )

    canvas.create_text(
        556.0,
        200.0,
        anchor="nw",
        text="SKILLS",
        fill="#FFFFFF",
        font=("OverpassRoman Bold", 24 * -1)
    )

    image_image_25 = PhotoImage(
        file=relative_to_assets("image_25.png"))
    image_25 = canvas.create_image(
        429.0,
        460.0,
        image=image_image_25
    )

    image_image_26 = PhotoImage(
        file=relative_to_assets("image_26.png"))
    image_26 = canvas.create_image(
        424.0,
        537.0,
        image=image_image_26
    )

    image_image_27 = PhotoImage(
        file=relative_to_assets("image_27.png"))
    image_27 = canvas.create_image(
        424.0,
        644.0,
        image=image_image_27
    )

    image_image_28 = PhotoImage(
        file=relative_to_assets("image_28.png"))
    image_28 = canvas.create_image(
        424.0,
        751.0,
        image=image_image_28
    )

    image_image_29 = PhotoImage(
        file=relative_to_assets("image_29.png"))
    image_29 = canvas.create_image(
        528.0,
        206.0,
        image=image_image_29
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=backtointerface,
        relief="flat"
    )
    button_1.place(
        x=1118.0,
        y=2.0,
        width=82.0,
        height=80.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=save,
        relief="flat"
    )
    button_3.place(
        x=798.0,
        y=712.0,
        width=387.0,
        height=121.0
    )



    #First information

    #fullname
    def on_enter(e):
        fullname.delete(0, 'end')

    def on_leave(e):
        if fullname.get() == '':
            fullname.insert(0, 'FULL NAME')
        else:
            fullname.insert(0, '')

    fullname.insert(0, 'FULL NAME')
    fullname.bind('<FocusIn>', on_enter)
    fullname.bind('<FocusOut>', on_leave)


    # Phone Number
    def on_enter(e):
        phonenumber.delete(0, 'end')

    def on_leave(e):
        if phonenumber.get() == '':
            phonenumber.insert(0, 'PHONE NUMBER')
        else:
            phonenumber.insert(0, '')


    phonenumber.insert(0, 'PHONE NUMBER')
    phonenumber.bind('<FocusIn>', on_enter)
    phonenumber.bind('<FocusOut>', on_leave)

    # eMAIL ADS
    def on_enter(e):
        emailadd.delete(0, 'end')

    def on_leave(e):
        if emailadd.get() == '':
            emailadd.insert(0, 'EMAIL ADDRESS')
        else:
            emailadd.insert(0, '')


    emailadd.insert(0, 'EMAIL ADDRESS')
    emailadd.bind('<FocusIn>', on_enter)
    emailadd.bind('<FocusOut>', on_leave)

    # Job or specialization
    def on_enter(e):
        work.delete(0, 'end')

    def on_leave(e):
        if work.get() == '':
            work.insert(0, 'JOB OR SPECIALIZATION')
        else:
            work.insert(0, '')

    work.insert(0, 'JOB OR SPECIALIZATION')
    work.bind('<FocusIn>', on_enter)
    work.bind('<FocusOut>', on_leave)


    # address
    def on_enter(e):
        address.delete(0, 'end')

    def on_leave(e):
        if address.get() == '':
            address.insert(0, 'ADDRESS')
        else:
            address.insert(0, '')


    address.insert(0, 'ADDRESS')
    address.bind('<FocusIn>', on_enter)
    address.bind('<FocusOut>', on_leave)


    #about me

    def on_enter(e):
        about.delete(0, 'end')

    def on_leave(e):
        if about.get() == '':
            about.insert(0, 'ABOUT ME')
        else:
            about.insert(0, '')


    about.insert(0, 'ABOUT ME')
    about.bind('<FocusIn>', on_enter)
    about.bind('<FocusOut>', on_leave)

    #

    #EXPERINCES

    #exp1
    def on_enter(e):
        exp1.delete(0, 'end')

    def on_leave(e):
        if exp1.get() == '':
            exp1.insert(0, 'WORK EXPERIENCE')
        else:
            exp1.insert(0, '')



    exp1.insert(0, 'WORK EXPERIENCE')
    exp1.bind('<FocusIn>', on_enter)
    exp1.bind('<FocusOut>', on_leave)

    #date1
    def on_enter(e):
        date1.delete(0, 'end')

    def on_leave(e):
        if date1.get() == '':
            date1.insert(0, 'DATE RANGE')
        else:
            date1.insert(0, '')


    date1.insert(0, 'DATE RANGE')
    date1.bind('<FocusIn>', on_enter)
    date1.bind('<FocusOut>', on_leave)


    #exp2
    def on_enter(e):
        exp2.delete(0, 'end')

    def on_leave(e):
        if exp2.get() == '':
            exp2.insert(0, 'WORK EXPERIENCE')
        else:
            exp2.insert(0, '')



    exp2.insert(0, 'WORK EXPERIENCE')
    exp2.bind('<FocusIn>', on_enter)
    exp2.bind('<FocusOut>', on_leave)

    #date2
    def on_enter(e):
        date2.delete(0, 'end')

    def on_leave(e):
        if date2.get() == '':
            date2.insert(0, 'DATE RANGE')
        else:
            date2.insert(0, '')


    date2.insert(0, 'DATE RANGE')
    date2.bind('<FocusIn>', on_enter)
    date2.bind('<FocusOut>', on_leave)

    #exp3
    def on_enter(e):
        exp3.delete(0, 'end')

    def on_leave(e):
        if exp3.get() == '':
            exp3.insert(0, 'WORK EXPERIENCE')
        else:
            exp3.insert(0, '')



    exp3.insert(0, 'WORK EXPERIENCE')
    exp3.bind('<FocusIn>', on_enter)
    exp3.bind('<FocusOut>', on_leave)
    #date3
    def on_enter(e):
        date3.delete(0, 'end')

    def on_leave(e):
        if date3.get() == '':
            date3.insert(0, 'DATE RANGE')
        else:
            date3.insert(0, '')


    date3.insert(0, 'DATE RANGE')
    date3.bind('<FocusIn>', on_enter)
    date3.bind('<FocusOut>', on_leave)

    # Skill

    # skill1
    def on_enter(e):
        skill1.delete(0, 'end')

    def on_leave(e):
        if skill1.get() == '':
            skill1.insert(0, 'SKILLS')
        else:
            skill1.insert(0, '')


    skill1.insert(0, 'SKILLS')
    skill1.bind('<FocusIn>', on_enter)
    skill1.bind('<FocusOut>', on_leave)


    # skill2
    def on_enter(e):
        skill2.delete(0, 'end')

    def on_leave(e):
        if skill2.get() == '':
            skill2.insert(0, 'SKILLS')
        else:
            skill2.insert(0, '')


    skill2.insert(0, 'SKILLS')
    skill2.bind('<FocusIn>', on_enter)
    skill2.bind('<FocusOut>', on_leave)


    # skill3
    def on_enter(e):
        skill3.delete(0, 'end')

    def on_leave(e):
        if skill3.get() == '':
            skill3.insert(0, 'SKILLS')
        else:
            skill3.insert(0, '')


    skill3.insert(0, 'SKILLS')
    skill3.bind('<FocusIn>', on_enter)
    skill3.bind('<FocusOut>', on_leave)


    # skill4
    def on_enter(e):
        skill4.delete(0, 'end')

    def on_leave(e):
        if skill4.get() == '':
            skill4.insert(0, 'SKILLS')
        else:
            skill4.insert(0, '')


    skill4.insert(0, 'SKILLS')
    skill4.bind('<FocusIn>', on_enter)
    skill4.bind('<FocusOut>', on_leave)


    # skill5
    def on_enter(e):
        skill5.delete(0, 'end')

    def on_leave(e):
        if skill5.get() == '':
            skill5.insert(0, 'SKILLS')
        else:
            skill5.insert(0, '')


    skill5.insert(0, 'SKILLS')
    skill5.bind('<FocusIn>', on_enter)
    skill5.bind('<FocusOut>', on_leave)

    # skill5
    def on_enter(e):
        skill6.delete(0, 'end')

    def on_leave(e):
        if skill6.get() == '':
            skill5.insert(0, 'SKILLS')
        else:
            skill6.insert(0, '')

    skill6.insert(0, 'SKILLS')
    skill6.bind('<FocusIn>', on_enter)
    skill6.bind('<FocusOut>', on_leave)


    # EDUCATION

    # Primary Education
    def on_enter(e):
        primary.delete(0, 'end')

    def on_leave(e):
        if primary.get() == '':
            primary.insert(0, 'PRIMARY EDUCATION')
        else:
            primary.insert(0, '')


    primary.insert(0, 'PRIMARY EDUCATION')
    primary.bind('<FocusIn>', on_enter)
    primary.bind('<FocusOut>', on_leave)


    #YEAR
    def on_enter(e):
        primary_year.delete(0, 'end')

    def on_leave(e):
        if primary_year.get() == '':
            primary_year.insert(0, 'YEAR START AND ENDS')
        else:
            primary_year.insert(0, '')


    primary_year.insert(0, 'YEAR START AND ENDS')
    primary_year.bind('<FocusIn>', on_enter)
    primary_year.bind('<FocusOut>', on_leave)


    # Secondary Education
    def on_enter(e):
        secondary.delete(0, 'end')

    def on_leave(e):
        if secondary.get() == '':
            secondary.insert(0, 'SECONDARY EDUCATION')
        else:
            secondary.insert(0, '')


    secondary.insert(0, 'SECONDARY EDUCATION')
    secondary.bind('<FocusIn>', on_enter)
    secondary.bind('<FocusOut>', on_leave)


    # YEAR
    def on_enter(e):
        secondary_year.delete(0, 'end')

    def on_leave(e):
        if secondary_year.get() == '':
            secondary_year.insert(0, 'YEAR START AND ENDS')
        else:
            secondary_year.insert(0, '')


    secondary_year.insert(0, 'YEAR START AND ENDS')
    secondary_year.bind('<FocusIn>', on_enter)
    secondary_year.bind('<FocusOut>', on_leave)


    # Tertiary Education
    def on_enter(e):
        tertiary.delete(0, 'end')

    def on_leave(e):
        if tertiary.get() == '':
            tertiary.insert(0, 'TERTIARY EDUCATION')
        else:
            tertiary.insert(0, '')


    tertiary.insert(0, 'TERTIARY EDUCATION')
    tertiary.bind('<FocusIn>', on_enter)
    tertiary.bind('<FocusOut>', on_leave)


    # YEAR
    def on_enter(e):
        tertiary_year.delete(0, 'end')

    def on_leave(e):
        if tertiary_year.get() == '':
            tertiary_year.insert(0, 'YEAR START AND ENDS')
        else:
            tertiary_year.insert(0, '')


    tertiary_year.insert(0, 'YEAR START AND ENDS')
    tertiary_year.bind('<FocusIn>', on_enter)
    tertiary_year.bind('<FocusOut>', on_leave)


    #button for selecting Template

    window.resizable(False, False)
    window.mainloop()





#main
def login():
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(
        r"C:\Users\ADMIN\Desktop\3E FILES\RESUMEGENERATOR\pythonProject2\build\assets\frame0")


    def create():
        window.destroy()

        def back():
            screen.destroy()
            login()
        def created():
            username = usercreate.get()
            pin = passwordcreate.get()
            cpin = cpasswordcreate.get()

            try:
                if pin == cpin:
                    # Connect to SQLite database (creates the database file if it doesn't exist)
                    conn = sqlite3.connect("user_resume.db")
                    cursor = conn.cursor()

                    # Create the 'users' table if it doesn't exist
                    cursor.execute('''
                            CREATE TABLE IF NOT EXISTS users (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                username TEXT,
                                password TEXT
                            )
                        ''')

                    # Insert data into the 'users' table
                    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, pin))

                    # Commit changes and close the connection
                    conn.commit()
                    conn.close()

                    messagebox.showinfo("", "Record inserted successfully!")
                else:
                    messagebox.showerror("", "Password did not match!")


            except sqlite3.Error as e:
                messagebox.showerror("", f"SQLite error: {e}")

        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(
            r"C:\Users\ADMIN\Desktop\3E FILES\RESUMEGENERATOR\pythonProject2\create_interface\build\assets\frame0")

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        screen = Tk()
        screen.geometry("800x400")
        screen.configure(bg="#FFFFFF")

        canvas = Canvas(
            screen,
            bg="#FFFFFF",
            height=400,
            width=800,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        canvas.place(x=0, y=0)
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
        usercreate = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        usercreate.place(
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
        passwordcreate = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        passwordcreate.place(
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
            image=entry_image_3)
        cpasswordcreate = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        cpasswordcreate.place(
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
            command=back,
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
            command=created,
            relief="flat"
        )
        button_2.place(
            x=516.0,
            y=294.0,
            width=262.0,
            height=50.0
        )
        screen.resizable(False, False)

        # user
        def on_enter(e):
            usercreate.delete(0, 'end')

        def on_leave(e):
            if usercreate.get() == '':
                usercreate.insert(0, 'Username')
            else:
                usercreate.insert(0, '')

        # username
        usercreate.insert(0, 'Username')
        usercreate.bind('<FocusIn>', on_enter)
        usercreate.bind('<FocusOut>', on_leave)

        # pass
        def on_enter(e):
            passwordcreate.delete(0, 'end')

        def on_leave(e):
            if passwordcreate.get() == '':
                passwordcreate.insert(0, 'Password')
            else:
                passwordcreate.insert(0, '')

        passwordcreate.insert(0, 'Password')
        passwordcreate.bind('<FocusIn>', on_enter)
        passwordcreate.bind('<FocusOut>', on_leave)

        # Cpassword
        def on_enter(e):
            cpasswordcreate.delete(0, 'end')

        def on_leave(e):
            if cpasswordcreate.get() == '':
                cpasswordcreate.insert(0, 'Confirm Password')
            else:
                cpasswordcreate.insert(0, '')

        cpasswordcreate.insert(0, 'Confirm Password')
        cpasswordcreate.bind('<FocusIn>', on_enter)
        cpasswordcreate.bind('<FocusOut>', on_leave)
        screen.mainloop()

    #login
    def signin():
        # database change the host user password database basta gamit nito ay php(xampp)

        try:
            # Connect to SQLite database (creates the database file if it doesn't exist)
            conn = sqlite3.connect("user_resume.db")
            cursor = conn.cursor()

            username = user.get()
            pin = password.get()

            # Check if the user is an admin
            if username.lower() == 'admin' and pin == 'password':
                screen = Toplevel(window)
                screen.title("Administrator")
                screen.geometry('1000x950+300+0')
                screen.config(bg='#5ED2E5')
                screen.resizable(False, False)

                Label(screen, text='Hello Everyone!').pack()
                screen.mainloop()
            else:
                # Authenticate against the users table
                sql = "SELECT * FROM users WHERE username = ? AND password = ?"
                cursor.execute(sql, (username, pin))
                results = cursor.fetchall()

                if results:
                    messagebox.showinfo("", "Login Successfully!")
                    window.destroy()
                    userinterface()
                else:
                    messagebox.showerror("Error", "Invalid Username and Password")

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"SQLite error: {e}")

        finally:
            if conn:
                conn.close()


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    window = Tk()

    window.geometry("800x400")
    window.configure(bg="#FFFFFF")

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=400,
        width=800,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
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
        147.0,
        59.0,
        image=image_image_2
    )

    canvas.create_text(
        92.0,
        135.0,
        anchor="nw",
        text="LOG IN",
        fill="#06314C",
        font=("Unlock Regular", 32 * -1)
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        261.5,
        200.5,
        image=entry_image_1
    )
    user = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    user.place(
        x=159.5,
        y=183.0,
        width=204.0,
        height=33.0
    )

    canvas.create_text(
        165.0,
        169.0,
        anchor="nw",
        text="USERNAME",
        fill="#000000",
        font=("PaytoneOne Regular", 12 * -1)
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        261.5,
        253.5,
        image=entry_image_2
    )
    password = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    password.place(
        x=159.5,
        y=236.0,
        width=204.0,
        height=33.0
    )

    canvas.create_text(
        165.0,
        223.0,
        anchor="nw",
        text="PASSWORD",
        fill="#000000",
        font=("PaytoneOne Regular", 12 * -1)
    )

    canvas.create_text(
        117.0,
        328.0,
        anchor="nw",
        text="Don’t have an account?",
        fill="#000000",
        font=("PaytoneOne Regular", 14 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        command=create)
    button_1.place(
        x=285.0,
        y=328.0,
        width=89.0,
        height=30.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=signin,
        relief="flat"
    )
    button_2.place(
        x=128.0,
        y=274.0,
        width=271.0,
        height=54.0
    )

    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        if user.get() == '':
            user.insert(0, 'Username')
        else:
            user.insert(0, '')

    # username

    user.insert(0, 'Username')
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)


    # pass
    def on_enter(e):
        password.delete(0, 'end')

    def on_leave(e):
        if password.get() == '':
            password.insert(0, 'Password')
        else:
            password.insert(0, '')
            password.config(show="*")

    password.insert(0, 'Password')
    password.bind('<FocusIn>', on_enter)
    password.bind('<FocusOut>', on_leave)

    window.resizable(False, False)
    window.mainloop()


login()