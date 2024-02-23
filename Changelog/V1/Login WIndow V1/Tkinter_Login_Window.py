# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# inital Login Window before username verification is applied           #
# Name: Ben Deaville                                                    #
# Known Bugs: none                                                      #
# Ideas to be added: auto selection of buttons so user can 'hit' enter  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#from V1\Face_Meshing\Mesh import *
from tkinter import *
from tkinter import messagebox
import sys
import My_Validation as validation
import sqlite3 as sq
from FilterTest import process_video


def is_valid_username(username: str) -> bool:
    """Checks if the username is valid (no special characters)"""
    return validation.is_valid_string(username)


def is_valid_password(password: str) -> bool:
    """Checks if the password is valid (no special characters)"""
    return validation.is_valid_string(password)


class DatabaseManager:
    """Handles operations that manage the database for the login windows"""
    def __init__(self):
        self.connection = sq.connect("Changelog/V1/Login WIndow V1/login.db")
        self.cursor = self.connection.cursor()

    def executeCommit(self, query: str, *args: list[tuple[any]]) -> None:
        """Executes a query and commits it"""
        self.cursor.execute(query, *args)
        self.connection.commit()

    def create_table(self) -> None:
        """Creates the table in the database, returns True if successful, False if not"""
        self.executeCommit("""CREATE TABLE IF NOT EXISTS login(
            USERNAME        TEXT    PRIMARY KEY     NOT NULL,
            PASSWORD        TEXT                    NOT NULL,
            ADMIN_STATUS    BOOLEAN DEFAULT FALSE   NOT NULL,
            FACE_NUM        INT                     NOT NULL
        )""")

    def insert_data(self, username: str, password: str, admin_status: bool = False, face_num: int = 1) -> None:
        """Inserts data into the database"""
        self.executeCommit("INSERT INTO login VALUES (?,?,?,?)", (username, password, admin_status, face_num))

    def insert_meshvalues(self, face_num: int) -> None:
        """Inserts a user's face number into the database"""
        self.executeCommit("INSERT INTO profile VALUES (?)", (face_num))

    def get_data(self, username: str) -> list[any]:
        """Gets the data from the database"""
        self.executeCommit("SELECT * FROM login WHERE USERNAME=?", (username,))
        rows = self.cursor.fetchall()
        return rows

    def get_password(self, username: str) -> str:
        """Gets the password hash from the database"""
        self.executeCommit("SELECT PASSWORD FROM login WHERE USERNAME=?", (username,))
        rows = self.cursor.fetchall()
        return rows[0][0]

    def is_admin(self, username: str) -> bool:
        """Returns a boolean for if the user is an admin or not"""
        self.executeCommit("SELECT ADMIN_STATUS FROM login WHERE USERNAME=?", (username,))
        rows = self.cursor.fetchall()
        return rows[0][0] == 1

    def insert_profile_values(self, face_num: int, username) -> None:
        """Inserts the profile values into the database"""
        self.executeCommit("INSERT INTO profile VALUES (?) WHERE USERNAME=?", (face_num,), (username))


database = DatabaseManager()

class LoginWindow:
    """Creates a window for the user to log in"""
    def __init__(self, window, window_title):
        """Initialise the login window"""
        self.window = window  # Create a window
        self.window.title(window_title)
        self.window.geometry("400x300")  # Set the window size
        self.window.resizable(0, 0)
        self.window.configure(bg="light blue")  # Set the window background colour

        # Create a login form
        Label(window, text="Please enter login details below", bg="light blue").pack()  # Create a label for the login form
        Label(window, text="", bg="light blue").pack()  # Create a space between the label and the entry box

        # Username

        Label(window, text="Username: ", bg="light blue").pack()  # Create a label for the username entry box
        self.username = Entry(window, textvariable=self.username)  # Create an entry box for the username
        self.username.pack()

        # Password that encrypts
        Label(window, text="", bg="light blue").pack()

        Label(window, text="Password: ", bg="light blue").pack()  # Create a label for the password entry box
        self.password = Entry(window, textvariable=self.password, show="*")  # Create an entry box for the password
        self.password.pack()

        Label(window, text="", bg="light blue").pack()  # Create a space between the entry box and the login button

        # login button, register button and exit button side by side
        Button(window, text="Login", width=10, height=1, command=self.login).place(x=110, y=200)
        Button(window, text="Exit", width=10, height=1, command=lambda: sys.exit()).place(x=210, y=200)

    def account_failed(self) -> None:
        """Shows a warning that the account could not be created"""
        messagebox.showinfo("Register info", "Unable to create account, please contact your system administrator")

    def login(self) -> None:
        """Checks the entered username and password against the database"""
        # Get username and password
        username = self.username.get()
        password = self.password.get()
        # Check if username and password is valid
        if password != database.get_password(username):
            messagebox.showerror("Error", "Invalid username or password")
            return
        # Check for admin status
        if database.is_admin(username):
            self.window.destroy()
            AdminWindow(Tk(), "Tkinter Admin Form")
        else:
            self.window.destroy()
            VariableWindow(Tk(), "Tkinter Variable Form", username)

    # Create a register function
    def register(self) -> None:
        self.window.destroy()  # Destroy login window
        RegisterWindow(Tk(), "Tkinter Register Form")  # Create register window


class RegisterWindow:  # Create a register window
    def __init__(self, window, window_title):
        """Initialise the register window"""
        self.window = window  # Create a window
        self.window.title(window_title)
        self.window.geometry("400x300")  # Set the window size
        self.window.resizable(0, 0)
        self.window.configure(bg="light blue")  # Set the window background colour

        # Create a register form
        Label(window, text="Please enter register details below", bg="light blue").pack()  # Create a label for the register form
        Label(window, text="", bg="light blue").pack()  # Create a space between the label and the entry box

        # Username
        Label(window, text="Username: ", bg="light blue").pack()  # Create a label for the username entry box
        self.username = Entry(window)  # Create an entry box for the username
        self.username.pack()

        # Password
        Label(window, text="Password: ", bg="light blue").pack()  # Create a label for the password entry box
        self.password = Entry(window, show="*")  # Create an entry box for the password
        self.password.pack()

        Label(window, text="", bg="light blue").pack()  # Create a space between the entry box and the login button

        # Login button
        Button(window, text="Register", width=10, height=1, command=self.register).pack()

        # Exit button
        Button(window, text="Exit", width=10, height=1, command=lambda: sys.exit()).pack()

    def register(self) -> None:
        """Registers the user"""
        # Get username and password
        username = self.username.get()
        password = self.password.get()
        print(username, password)

        # Check if username and password is valid

        # Put username and password into database
        database.insert_data(username, password, False, 1)
        messagebox.showinfo("Register info", "Account created successfully")


class VariableWindow:
    def __init__(self, window, window_title, username):
        """Initialise the variable window"""
        self.window = window
        self.window.title(window_title)
        self.window.geometry("500x400")
        self.window.resizable(0, 0)
        self.window.configure(bg="light yellow")

        Label(window, text="Edit the Face Tracking Variables here", bg="light yellow").pack()
        Label(window, text="", bg="light yellow").pack()

        # Face Tracking Variables
        self.face_num = IntVar()
        self.min_confidence = DoubleVar()
        self.max_confidence = DoubleVar()
        self.username = username

        Label(window, text="Face Number: ", bg="light yellow").pack()
        Scale(window, from_=1, to=5, orient=HORIZONTAL, relief=RAISED, variable=self.face_num).pack()

        Label(window, text="Minimum Confidence: ", bg="light yellow").pack()
        Scale(window, from_=0.0, to=1.0, orient=HORIZONTAL, resolution=0.1, variable=self.min_confidence).pack()

        Label(window, text="", bg="light yellow").pack()
        Button(window, text="Save", width=10, height=1, command=lambda: self.save(username)).pack()

    def save(self, username: str) -> None:
        face_num = self.face_num.get()
        min_confidence = self.min_confidence.get()
        print(face_num, min_confidence, username)
        self.window.destroy()
        process_video(face_num)
        #user_database.insert_profile_values(face_num, min_confidence, max_confidence, username)


class AdminWindow:
    """Shows a window with the admin specific UI"""
    def __init__(self, window, window_title):
        """Initialise the admin window"""
        self.window = window
        self.window.title(window_title)
        self.window.geometry("400x300")
        self.window.resizable(0, 0)
        self.window.configure(bg="light blue")

        # Title Admin Text
        Label(window, text="Admin", bg="magenta").pack()

        # Buttons to create account, remove account and exit
        Button(window, text="Create Account", width=10, height=1, command=self.create_account).pack()
        Button(window, text="Remove Account", width=10, height=1, command=self.remove_account).pack()
        Button(window, text="Exit", width=10, height=1, command=lambda: sys.exit()).pack()

    def create_account(self) -> None:
        """Shows the 'create account' window"""
        RegisterWindow(Tk(), "Tkinter Register Form")

    def remove_account(self) -> None:
        ...


LoginWindow(Tk(), "Tkinter Login Form")
# VariableWindow(Tk(), "Tkinter Variable Form", "ben")  #test variable window
# RegisterWindow(Tk(), "Tkinter Register Form")
# AdminWindow(Tk(), "Tkinter Admin Form")
mainloop()


