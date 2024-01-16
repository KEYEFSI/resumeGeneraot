
from tkinter import *
from tkinter import messagebox
import sqlite3
background = '#5ED2E5'

def userinterface():
    screen =Tk()
    screen.title("User Display")
    screen.geometry('900x500+300+200')
    screen.config(bg='#5ED2E5')
    screen.resizable(False,False)

    img = PhotoImage(file='logo.png')
    Label(screen, image=img, bg='#5ED2E5').place(x=200, y=5)
    Button( width=39, pady=7, text='Create Resume',bg='#065A8D', fg='white', border=0,
           font=('Microsoft Times New Roman', 9, 'bold'),command=inputcontext).place(x=70, y=400)
    Button(width=39, pady=7, text='View Resume', bg='#065A8D', fg='white', border=0,
           font=('Microsoft Times New Roman', 9, 'bold')).place(x=520, y=400)
    screen.mainloop()

def inputcontext():
    window = Tk()
    window.title("CREATE RESUME")
    window.geometry('750x900+500+0')
    window.config(bg='#5ED2E5')
    window.resizable(False, False)
    frame = Frame(window, width=700, height=870, bg=background)
    frame.place(x=10, y=10)

    heading = Label(frame,text='CREATE RESUME', fg='black', bg='#5ED2E5',
                    font=('Microsoft Times New Roman', 16, 'bold'))
    heading.place(x=300, y=10)



    #First information
    label = Label(frame,text='CONTACT INFORMATION', fg='black', bg='#5ED2E5',
                    font=('Microsoft Arial', 13, 'bold'))
    label.place(x=25, y=75)

    #fullname
    def on_enter(e):
        fullname.delete(0, 'end')

    def on_leave(e):
        if fullname.get() == '':
            fullname.insert(0, 'FULL NAME')
        else:
            fullname.insert(0, '')
    fullname = Entry(frame, width=25, fg='black', border=0, bg='#5ED2E5', font=('Microsoft Times New Roman', 11))
    fullname.place(x=30, y=100)
    fullname.insert(0, 'FULL NAME')
    fullname.bind('<FocusIn>', on_enter)
    fullname.bind('<FocusOut>', on_leave)
    Frame(frame, width=220, height=2, bg='#065A8D').place(x=25, y=120)

    # Phone Number
    def on_enter(e):
        phonenumber.delete(0, 'end')

    def on_leave(e):
        if phonenumber.get() == '':
            phonenumber.insert(0, 'PHONE NUMBER')
        else:
            phonenumber.insert(0, '')

    phonenumber = Entry(frame, width=25, fg='black', border=0, bg='#5ED2E5', font=('Microsoft Times New Roman', 11))
    phonenumber.place(x=30, y=130)
    phonenumber.insert(0, 'PHONE NUMBER')
    phonenumber.bind('<FocusIn>', on_enter)
    phonenumber.bind('<FocusOut>', on_leave)
    Frame(frame, width=220, height=2, bg='#065A8D').place(x=25, y=150)

    # eMAIL ADS
    def on_enter(e):
        email.delete(0, 'end')

    def on_leave(e):
        if email.get() == '':
            email.insert(0, 'EMAIL ADDRESS')
        else:
            email.insert(0, '')

    email = Entry(frame, width=25, fg='black', border=0, bg='#5ED2E5', font=('Microsoft Times New Roman', 11))
    email.place(x=30, y=160)
    email.insert(0, 'EMAIL ADDRESS')
    email.bind('<FocusIn>', on_enter)
    email.bind('<FocusOut>', on_leave)
    Frame(frame, width=220, height=2, bg='#065A8D').place(x=25, y=180)

    # Job or specialization
    def on_enter(e):
        job.delete(0, 'end')

    def on_leave(e):
        if job.get() == '':
            job.insert(0, 'JOB OR SPECIALIZATION')
        else:
            job.insert(0, '')

    job = Entry(frame, width=25, fg='black', border=0, bg='#5ED2E5', font=('Microsoft Times New Roman', 11))
    job.place(x=30, y=190)
    job.insert(0, 'JOB OR SPECIALIZATION')
    job.bind('<FocusIn>', on_enter)
    job.bind('<FocusOut>', on_leave)
    Frame(frame, width=220, height=2, bg='#065A8D').place(x=25, y=210)

    # address
    def on_enter(e):
        address.delete(0, 'end')

    def on_leave(e):
        if address.get() == '':
            address.insert(0, 'ADDRESS')
        else:
            address.insert(0, '')

    address = Entry(frame, width=25, fg='black', border=0, bg='#5ED2E5', font=('Microsoft Times New Roman', 11))
    address.place(x=30, y=220)
    address.insert(0, 'ADDRESS')
    address.bind('<FocusIn>', on_enter)
    address.bind('<FocusOut>', on_leave)
    Frame(frame, width=220, height=2, bg='#065A8D').place(x=25, y=240)

    #about me
    label = Label(frame, text='ABOUT ME', fg='black', bg='#5ED2E5',
                  font=('Microsoft Arial', 13, 'bold'))
    label.place(x=400, y=75)

    def on_enter(e):
        about.delete(0, 'end')

    def on_leave(e):
        if about.get() == '':
            about.insert(0, 'ABOUT ME')
        else:
            about.insert(0, '')


    about = Entry(frame, width=50, fg='black', border=0,bg=background, font=('Microsoft Times New Roman', 10))
    about.place(x=400, y=100)
    about.insert(0, 'ABOUT ME')
    about.bind('<FocusIn>', on_enter)
    about.bind('<FocusOut>', on_leave)
    Frame(frame, width=300, height=2, bg='#065A8D').place(x=400, y=120)
    #

    #EXPERINCES
    label = Label(frame, text='WORK EXPERIENCE/S', fg='black', bg='#5ED2E5',
                  font=('Microsoft Arial', 13, 'bold'))
    label.place(x=30, y=270)
    #exp1
    def on_enter(e):
        exp1.delete(0, 'end')

    def on_leave(e):
        if exp1.get() == '':
            exp1.insert(0, 'FIRST WORK EXPERIENCE')
        else:
            exp1.insert(0, '')


    exp1 = Entry(frame, width=50, fg='black', border=0,bg=background, font=('Microsoft Times New Roman', 10))
    exp1.place(x=30, y=300)
    exp1.insert(0, 'FIRST WORK EXPERIENCE')
    exp1.bind('<FocusIn>', on_enter)
    exp1.bind('<FocusOut>', on_leave)
    Frame(frame, width=300, height=2, bg='#065A8D').place(x=30, y=320)
    #date1
    def on_enter(e):
        date1.delete(0, 'end')

    def on_leave(e):
        if date1.get() == '':
            date1.insert(0, 'DATE RANGE')
        else:
            date1.insert(0, '')

    date1 = Entry(frame, width=50, fg='black', border=0, bg=background, font=('Microsoft Times New Roman', 10))
    date1.place(x=30, y=330)
    date1.insert(0, 'DATE RANGE')
    date1.bind('<FocusIn>', on_enter)
    date1.bind('<FocusOut>', on_leave)
    Frame(frame, width=300, height=2, bg='#065A8D').place(x=30, y=350)

    #exp2
    def on_enter(e):
        exp2.delete(0, 'end')

    def on_leave(e):
        if exp2.get() == '':
            exp2.insert(0, 'SECOND WORK EXPERIENCE')
        else:
            exp2.insert(0, '')


    exp2 = Entry(frame, width=50, fg='black', border=0,bg=background, font=('Microsoft Times New Roman', 10))
    exp2.place(x=30, y=370)
    exp2.insert(0, 'SECOND WORK EXPERIENCE')
    exp2.bind('<FocusIn>', on_enter)
    exp2.bind('<FocusOut>', on_leave)
    Frame(frame, width=300, height=2, bg='#065A8D').place(x=30, y=390)
    #date2
    def on_enter(e):
        date2.delete(0, 'end')

    def on_leave(e):
        if date2.get() == '':
            date2.insert(0, 'DATE RANGE')
        else:
            date2.insert(0, '')

    date2 = Entry(frame, width=50, fg='black', border=0, bg=background, font=('Microsoft Times New Roman', 10))
    date2.place(x=30, y=400)
    date2.insert(0, 'DATE RANGE')
    date2.bind('<FocusIn>', on_enter)
    date2.bind('<FocusOut>', on_leave)
    Frame(frame, width=300, height=2, bg='#065A8D').place(x=30, y=420)

    #exp3
    def on_enter(e):
        exp3.delete(0, 'end')

    def on_leave(e):
        if exp3.get() == '':
            exp3.insert(0, 'THIRD WORK EXPERIENCE')
        else:
            exp3.insert(0, '')


    exp3 = Entry(frame, width=50, fg='black', border=0,bg=background, font=('Microsoft Times New Roman', 10))
    exp3.place(x=30, y=450)
    exp3.insert(0, 'THIRD WORK EXPERIENCE')
    exp3.bind('<FocusIn>', on_enter)
    exp3.bind('<FocusOut>', on_leave)
    Frame(frame, width=300, height=2, bg='#065A8D').place(x=30, y=470)
    #date3
    def on_enter(e):
        date3.delete(0, 'end')

    def on_leave(e):
        if date3.get() == '':
            date3.insert(0, 'DATE RANGE')
        else:
            date3.insert(0, '')

    date3 = Entry(frame, width=50, fg='black', border=0, bg=background, font=('Microsoft Times New Roman', 10))
    date3.place(x=30, y=480)
    date3.insert(0, 'DATE RANGE')
    date3.bind('<FocusIn>', on_enter)
    date3.bind('<FocusOut>', on_leave)
    Frame(frame, width=300, height=2, bg='#065A8D').place(x=30, y=500)

    # Skill
    label = Label(frame, text='SKILLS', fg='black', bg='#5ED2E5',
                  font=('Microsoft Arial', 13, 'bold'))
    label.place(x=400, y=270)

    # skill1
    def on_enter(e):
        skill1.delete(0, 'end')

    def on_leave(e):
        if skill1.get() == '':
            skill1.insert(0, 'SKILLS')
        else:
            skill1.insert(0, '')

    skill1 = Entry(frame, width=50, fg='black', border=0, bg=background, font=('Microsoft Times New Roman', 10))
    skill1.place(x=400, y=300)
    skill1.insert(0, 'SKILLS')
    skill1.bind('<FocusIn>', on_enter)
    skill1.bind('<FocusOut>', on_leave)
    Frame(frame, width=300, height=2, bg='#065A8D').place(x=400, y=320)

    # skill2
    def on_enter(e):
        skill2.delete(0, 'end')

    def on_leave(e):
        if skill2.get() == '':
            skill2.insert(0, 'SKILLS')
        else:
            skill2.insert(0, '')

    skill2 = Entry(frame, width=50, fg='black', border=0, bg=background, font=('Microsoft Times New Roman', 10))
    skill2.place(x=400, y=330)
    skill2.insert(0, 'SKILLS')
    skill2.bind('<FocusIn>', on_enter)
    skill2.bind('<FocusOut>', on_leave)
    Frame(frame, width=300, height=2, bg='#065A8D').place(x=400, y=350)

    # skill3
    def on_enter(e):
        skill3.delete(0, 'end')

    def on_leave(e):
        if skill3.get() == '':
            skill3.insert(0, 'SKILLS')
        else:
            skill3.insert(0, '')

    skill3 = Entry(frame, width=50, fg='black', border=0, bg=background, font=('Microsoft Times New Roman', 10))
    skill3.place(x=400, y=360)
    skill3.insert(0, 'SKILLS')
    skill3.bind('<FocusIn>', on_enter)
    skill3.bind('<FocusOut>', on_leave)
    Frame(frame, width=300, height=2, bg='#065A8D').place(x=400, y=380)

    # skill4
    def on_enter(e):
        skill4.delete(0, 'end')

    def on_leave(e):
        if skill4.get() == '':
            skill4.insert(0, 'SKILLS')
        else:
            skill4.insert(0, '')

    skill4 = Entry(frame, width=50, fg='black', border=0, bg=background, font=('Microsoft Times New Roman', 10))
    skill4.place(x=400, y=390)
    skill4.insert(0, 'SKILLS')
    skill4.bind('<FocusIn>', on_enter)
    skill4.bind('<FocusOut>', on_leave)
    Frame(frame, width=300, height=2, bg='#065A8D').place(x=400, y=410)

    # skill5
    def on_enter(e):
        skill5.delete(0, 'end')

    def on_leave(e):
        if skill5.get() == '':
            skill5.insert(0, 'SKILLS')
        else:
            skill5.insert(0, '')

    skill5 = Entry(frame, width=50, fg='black', border=0, bg=background, font=('Microsoft Times New Roman', 10))
    skill5.place(x=400, y=420)
    skill5.insert(0, 'SKILLS')
    skill5.bind('<FocusIn>', on_enter)
    skill5.bind('<FocusOut>', on_leave)
    Frame(frame, width=300, height=2, bg='#065A8D').place(x=400, y=440)

    # EDUCATION
    label = Label(frame, text='EDUCATION', fg='black', bg='#5ED2E5',
                  font=('Microsoft Arial', 13, 'bold'))
    label.place(x=30, y=540)

    # Primary Education
    def on_enter(e):
        primary.delete(0, 'end')

    def on_leave(e):
        if primary.get() == '':
            primary.insert(0, 'PRIMARY EDUCATION')
        else:
            primary.insert(0, '')

    primary = Entry(frame, width=50, fg='black', border=0, bg=background, font=('Microsoft Times New Roman', 10))
    primary.place(x=30, y=570)
    primary.insert(0, 'PRIMARY EDUCATION')
    primary.bind('<FocusIn>', on_enter)
    primary.bind('<FocusOut>', on_leave)
    Frame(frame, width=300, height=2, bg='#065A8D').place(x=30, y=590)

    #YEAR
    def on_enter(e):
        primary_year.delete(0, 'end')

    def on_leave(e):
        if primary_year.get() == '':
            primary_year.insert(0, 'YEAR START AND ENDS')
        else:
            primary_year.insert(0, '')

    primary_year = Entry(frame, width=50, fg='black', border=0, bg=background, font=('Microsoft Times New Roman', 10))
    primary_year.place(x=30, y=600)
    primary_year.insert(0, 'YEAR START AND ENDS')
    primary_year.bind('<FocusIn>', on_enter)
    primary_year.bind('<FocusOut>', on_leave)
    Frame(frame, width=300, height=2, bg='#065A8D').place(x=30, y=620)

    # Secondary Education
    def on_enter(e):
        secondary.delete(0, 'end')

    def on_leave(e):
        if secondary.get() == '':
            secondary.insert(0, 'SECONDARY EDUCATION')
        else:
            secondary.insert(0, '')

    secondary = Entry(frame, width=50, fg='black', border=0, bg=background, font=('Microsoft Times New Roman', 10))
    secondary.place(x=30, y=640)
    secondary.insert(0, 'SECONDARY EDUCATION')
    secondary.bind('<FocusIn>', on_enter)
    secondary.bind('<FocusOut>', on_leave)
    Frame(frame, width=300, height=2, bg='#065A8D').place(x=30, y=660)

    # YEAR
    def on_enter(e):
        secondary_year.delete(0, 'end')

    def on_leave(e):
        if secondary_year.get() == '':
            secondary_year.insert(0, 'YEAR START AND ENDS')
        else:
            secondary_year.insert(0, '')

    secondary_year = Entry(frame, width=50, fg='black', border=0, bg=background, font=('Microsoft Times New Roman', 10))
    secondary_year.place(x=30, y=670)
    secondary_year.insert(0, 'YEAR START AND ENDS')
    secondary_year.bind('<FocusIn>', on_enter)
    secondary_year.bind('<FocusOut>', on_leave)
    Frame(frame, width=300, height=2, bg='#065A8D').place(x=30, y=690)

    # Tertiary Education
    def on_enter(e):
        tertiary.delete(0, 'end')

    def on_leave(e):
        if tertiary.get() == '':
            tertiary.insert(0, 'TERTIARY EDUCATION')
        else:
            tertiary.insert(0, '')

    tertiary = Entry(frame, width=50, fg='black', border=0, bg=background, font=('Microsoft Times New Roman', 10))
    tertiary.place(x=30, y=720)
    tertiary.insert(0, 'TERTIARY EDUCATION')
    tertiary.bind('<FocusIn>', on_enter)
    tertiary.bind('<FocusOut>', on_leave)
    Frame(frame, width=300, height=2, bg='#065A8D').place(x=30, y=740)

    # YEAR
    def on_enter(e):
        tertiary_year.delete(0, 'end')

    def on_leave(e):
        if tertiary_year.get() == '':
            tertiary_year.insert(0, 'YEAR START AND ENDS')
        else:
            tertiary_year.insert(0, '')

    tertiary_year = Entry(frame, width=50, fg='black', border=0, bg=background, font=('Microsoft Times New Roman', 10))
    tertiary_year.place(x=30, y=750)
    tertiary_year.insert(0, 'YEAR START AND ENDS')
    tertiary_year.bind('<FocusIn>', on_enter)
    tertiary_year.bind('<FocusOut>', on_leave)
    Frame(frame, width=300, height=2, bg='#065A8D').place(x=30, y=770)

    #button for selecting Template
    Button(frame, width=50, pady=5, text='View Resume', bg='#065A8D', fg='white', border=0,
           font=( 'Microsoft Times New Roman', 15, 'bold')).place(x=65, y=800)


    window.mainloop()
#main
def login():
    root = Tk()
    root.title('Resume Generator')
    root.geometry('900x500+300+200')
    root.configure(bg="#5ED2E5")
    root.resizable(False, False)

    #create acc interface
    def create():
        screen = Toplevel(root)
        screen.title("Create an Account")
        screen.geometry('900x500+300+200')
        screen.configure(bg="#5ED2E5")
        screen.resizable(False, False)

        img = PhotoImage(file='logo.png')
        Label(screen, image=img, bg='#5ED2E5').place(x=400, y=20)
        frame = Frame(screen, width=350, height=400, bg="#5ED2E5")
        frame.place(x=50, y=100)

        #databse insertion
        def created():
            username = user.get()
            pin = password.get()
            cpin = cpassword.get()

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

        #user
        def on_enter(e):
            user.delete(0, 'end')

        def on_leave(e):
            if user.get() == '':
                user.insert(0, 'Username')
            else:
                user.insert(0, '')

        heading = Label(frame, text='Create an Account', fg='#065A8D', bg='#5ED2E5', font=('Microsoft Times New Roman', 23, 'bold'))
        heading.place(x=5, y=5)
        # username
        user = Entry(frame, width=25, fg='black', border=0, bg='#5ED2E5', font=('Microsoft Times New Roman', 11))
        user.place(x=30, y=80)
        user.insert(0, 'Username')
        user.bind('<FocusIn>', on_enter)
        user.bind('<FocusOut>', on_leave)

        Frame(frame, width=295, height=2, bg='#065A8D').place(x=25, y=107)

        # pass
        def on_enter(e):
            password.delete(0, 'end')

        def on_leave(e):
            if password.get() == '':
                password.insert(0, 'Password')
            else:
                password.insert(0, '')

        password = Entry(frame, width=25, fg='black', border=0, bg='#5ED2E5', font=('Microsoft Times New Roman', 11))
        password.place(x=30, y=150)
        password.insert(0, 'Password')
        password.bind('<FocusIn>', on_enter)
        password.bind('<FocusOut>', on_leave)

        Frame(frame, width=295, height=2, bg='#065A8D').place(x=25, y=177)
        #Cpassword
        def on_enter(e):
            cpassword.delete(0, 'end')

        def on_leave(e):
            if cpassword.get() == '':
                cpassword.insert(0, 'Confirm Password')
            else:
                cpassword.insert(0, '')

        cpassword = Entry(frame, width=25, fg='black', border=0, bg='#5ED2E5', font=('Microsoft Times New Roman', 11))
        cpassword.place(x=30, y=220)
        cpassword.insert(0, 'Confirm Password')
        cpassword.bind('<FocusIn>', on_enter)
        cpassword.bind('<FocusOut>', on_leave)

        Frame(frame, width=295, height=2, bg='#065A8D').place(x=25, y=247)
        Button(frame, width=39, pady=7, text='Create Account', bg='#065A8D', fg='white', border=0,
               font=('Microsoft Times New Roman', 9, 'bold'), command=created).place(x=30, y=277)
        label = Label(frame, text="I have an account?", fg='#065A8D', bg="#5ED2E5",
                      font=('Microsoft Times New Roman', 9)).place(x=75, y=340)

        logsign = Button(frame, width=6, text='Log in', border=0, bg='#5ED2E5', cursor='hand2', fg='white',
                        command=screen.destroy)
        logsign.place(x=215, y=340)
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
                screen = Toplevel(root)
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
                    root.destroy()
                    userinterface()
                else:
                    messagebox.showerror("Error", "Invalid Username and Password")

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"SQLite error: {e}")

        finally:
            if conn:
                conn.close()

    # Specify the correct file extension (e.g., '.png') in the file path
    img = PhotoImage(file='logo.png')

    Label(root, image=img, bg='#5ED2E5').place(x=50, y=20)
    frame = Frame(root, width=350, height=350, bg="#5ED2E5")
    frame.place(x=480, y=100)

    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        if user.get() == '':
            user.insert(0, 'Username')
        else:
            user.insert(0, '')

    heading = Label(frame, text='Log in', fg="#065A8D", bg='#5ED2E5', font=('Microsoft Times New Roman', 23, 'bold'))
    heading.place(x=100, y=5)
    # username
    user = Entry(frame, width=25, fg='black', border=0, bg='#5ED2E5', font=('Microsoft Times New Roman', 11))
    user.place(x=30, y=80)
    user.insert(0, 'Username')
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)

    Frame(frame, width=295, height=2, bg='#065A8D').place(x=25, y=107)

    # pass
    def on_enter(e):
        password.delete(0, 'end')

    def on_leave(e):
        if password.get() == '':
            password.insert(0, 'Password')
        else:
            password.insert(0, '')
            password.config(show="*")


    password = Entry(frame, width=25, fg='black', border=0, bg='#5ED2E5', font=('Microsoft Times New Roman', 11))
    password.place(x=30, y=150)
    password.insert(0, 'Password')
    password.bind('<FocusIn>', on_enter)
    password.bind('<FocusOut>', on_leave)

    Frame(frame, width=295, height=2, bg='#065A8D').place(x=25, y=177)





    Button(frame, width=39, pady=7, text='Log in', bg='#065A8D', fg='white', border=0,font=('Microsoft Times New Roman', 9, 'bold'), command=signin).place(x=30, y=204)
    label = Label(frame, text="Don't have account?", fg='#065A8D', bg="#5ED2E5",font=('Microsoft Times New Roman', 9)).place(x=75, y=270)

    signup = Button(frame, width=6, text='Sign up', border=0, bg='#5ED2E5', cursor='hand2', fg='white', command=create)
    signup.place(x=215, y=270)





    root.mainloop()


login()
