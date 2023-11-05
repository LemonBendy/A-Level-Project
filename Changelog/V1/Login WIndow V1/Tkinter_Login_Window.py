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
import My_Validation
import sqlite3 as sq
from Mesh import mesh


   # Check if username is valid
def is_valid_username(username):
    try:
        My_Validation.is_valid_string(username)
    except:
        return False
        
    # Check if password is valid
def is_valid_password(password):
    try:
        My_Validation.is_valid_string(password)
    except:
        return False
        

class user_database:
    def __init__(self):
        self.self = self

    def create_table():
        try:
            conn = sq.connect("Changelog/V1/Login WIndow V1/login.db")
            c = conn.cursor()
            c.execute("""CREATE TABLE IF NOT EXISTS login(
                USERNAME        TEXT    PRIMARY KEY     NOT NULL,
                PASSWORD        TEXT                    NOT NULL,
                ADMIN_STATUS    BOOLEAN DEFAULT FALSE   NOT NULL,
                FACE_NUM        INT                     NOT NULL,
                DISTANCE        INT                     NOT NULL,
                )""")
            conn.commit()
            conn.close()
        except Exception as e:
            print(e)
            return False

    def insert_data(username, password, admin_status=False):
        try:
            conn = sq.connect("Changelog/V1/Login WIndow V1/login.db")
            c = conn.cursor()
            c.execute("INSERT INTO login VALUES (?,?,?)", (username, password, admin_status))
            conn.commit()
            conn.close()
        except Exception as e:
            print(e)
            return False
        
    def insert_meshvalues(face_num, min_confidence, max_confidence):
        try:
            conn = sq.connect("Changelog/V1/Login WIndow V1/login.db")
            c = conn.cursor()
            c.execute("INSERT INTO profile VALUES (?,?,?)", (face_num, min_confidence, max_confidence))
            conn.commit()
            conn.close()
        except Exception as e:
            print(e)
            return False

    def get_data(username):
        try:
            conn = sq.connect("Changelog/V1/Login WIndow V1/login.db")
            c = conn.cursor()
            c.execute("SELECT * FROM login WHERE USERNAME=?", (username,))
            rows = c.fetchall()
            conn.close()
            return rows
        except Exception as e:
            print(e)
            return False
    #function to get password from database
    def get_password(username):
        try:
            conn = sq.connect("Changelog/V1/Login WIndow V1/login.db")
            c = conn.cursor()
            c.execute("SELECT PASSWORD FROM login WHERE USERNAME=?", (username,))
            rows = c.fetchall()
            conn.close()
            return rows[0][0]
        except Exception as e:
            print(e)
            return False  
        
    #function to get admin status from database
    def get_admin_status(username):
        try:
            conn = sq.connect("Changelog/V1/Login WIndow V1/login.db")
            c = conn.cursor()
            c.execute("SELECT ADMIN_STATUS FROM login WHERE USERNAME=?", (username,))
            rows = c.fetchall()
            conn.close()
            return rows[0][0]
        except Exception as e:
            print(e)
            return False
        
    def insert_profile_values(face_num, min_confidence, max_confidence, username):
        try:
            conn = sq.connect("Changelog/V1/Login WIndow V1/login.db")
            c = conn.cursor()
            c.execute("INSERT INTO profile VALUES (?,?,?) WHERE USERNAME=?", (face_num, min_confidence, max_confidence), (username))
            conn.commit()
            conn.close()
        except Exception as e:
            print(e)
            return False
    
class LoginWindow: # Create a login window
    def __init__(self, window, window_title): # Initialise the login window
        self.window = window # Create a window
        self.username = ""
        self.window.title(window_title)
        self.window.geometry("400x300") # Set the window size
        self.window.resizable(0, 0)
        self.window.configure(bg="light blue") # Set the window background colour

        # Create a login form
        Label(window, text="Please enter login details below", bg="light blue").pack() # Create a label for the login form
        Label(window, text="", bg="light blue").pack() # Create a space between the label and the entry box

        # Username
        self.username = StringVar()

        Label(window, text="Username: ", bg="light blue").pack() # Create a label for the username entry box
        Entry(window, textvariable=self.username).pack() # Create an entry box for the username

        # Password that encrypts
        self.password = StringVar()
        Label(window, text="", bg="light blue").pack() 

        Label(window, text="Password: ", bg="light blue").pack() # Create a label for the password entry box
        Entry(window, textvariable=self.password, show="*").pack() # Create an entry box for the password

        Label(window, text="", bg="light blue").pack() # Create a space between the entry box and the login button


       # login button, register button and exit button side by side
        Button(window, text="Login", width=10, height=1, command=self.login).place(x=110, y=200)
        Button(window, text="Exit", width=10, height=1, command=lambda: sys.exit()).place(x=210, y=200)


    def user_register(self):
        messagebox.showinfo("Register info", "Unable to create account, please contact your system administrator")

    def login(self): # Create a login function
        # Get username and password
        username = self.username.get()
        password = self.password.get()
        # Check if username and password is valid
        user_database.get_data(username)
        if password == user_database.get_password(username):
            # check for admin status
            if user_database.get_admin_status(username) == 1:
                self.window.destroy()
                AdminWindow(Tk(), "Tkinter Admin Form")
            else:
                self.window.destroy()
                VariableWindow(Tk(), "Tkinter Variable Form", username)
        else:
            messagebox.showerror("Error", "Invalid username or password")

    # Create a register function    
    def register(self):
        self.window.destroy() #destroy login window
        RegisterWindow(Tk(), "Tkinter Register Form") #create register window


class RegisterWindow: # Create a register window
    def __init__(self, window, window_title): # Initialise the register window
        self.window = window # Create a window
        self.window.title(window_title)
        self.window.geometry("400x300") # Set the window size
        self.window.resizable(0, 0)
        self.window.configure(bg="light blue") # Set the window background colour

        # Create a register form
        Label(window, text="Please enter register details below", bg="light blue").pack() # Create a label for the register form
        Label(window, text="", bg="light blue").pack() # Create a space between the label and the entry box

        # Username
        self.username = StringVar()

        Label(window, text="Username: ", bg="light blue").pack() # Create a label for the username entry box
        Entry(window, textvariable=self.username).pack() # Create an entry box for the username

        # Password that encrypts
        self.password = StringVar()

        Label(window, text="Password: ", bg="light blue").pack() # Create a label for the password entry box
        Entry(window, textvariable=self.password, show="*").pack() # Create an entry box for the password

        Label(window, text="", bg="light blue").pack() # Create a space between the entry box and the login button

        # Login button
        Button(window, text="Register", width=10, height=1, command=self.register).pack()

        #exit button
        Button(window, text="Exit", width=10, height=1, command=lambda: sys.exit()).pack()

    def register(self): # Create a register function
        # Get username and password
        username = self.username.get()
        password = self.password.get()

        #put username and password into database
        if is_valid_username(username) and is_valid_password(password):
            user_database.insert_data(username, password)
            messagebox.showinfo("Register info", "Account created successfully")

class VariableWindow:
    def __init__(self, window, window_title, username):
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
        
    def save(self, username):
        face_num = self.face_num.get()
        min_confidence = self.min_confidence.get()
        print(face_num, min_confidence, username)
        mesh(face_num, min_confidence)
        #user_database.insert_profile_values(face_num, min_confidence, max_confidence, username)
            

class AdminWindow:
    def __init__(self, window, window_title):
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

    def create_account(self):
        RegisterWindow(Tk(), "Tkinter Register Form")


    def remove_account(self):
        pass


def create_table():
    try:
        conn = sq.connect("Changelog/V1/Login WIndow V1/login.db")
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS login(
            USERNAME        TEXT    PRIMARY KEY     NOT NULL,
            PASSWORD        TEXT                    NOT NULL,
            ADMIN_STATUS    BOOLEAN DEFAULT FALSE   NOT NULL
            )''')
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)
        return False

create_table()

#LoginWindow(Tk(), "Tkinter Login Form")
#VariableWindow(Tk(), "Tkinter Variable Form", "ben") #test variable window
# RegisterWindow(Tk(), "Tkinter Register Form")
# AdminWindow(Tk(), "Tkinter Admin Form")
#mainloop()


