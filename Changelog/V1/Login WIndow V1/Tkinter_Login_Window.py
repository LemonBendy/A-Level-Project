# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# inital Login Window before username verification is applied           #
# Name: Ben Deaville                                                    #
# Known Bugs: none                                                      #
# Ideas to be added: auto selection of buttons so user can 'hit' enter  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
from V1\Face_Meshing\Mesh import *
from tkinter import *
from tkinter import messagebox
import sys
import My_Validation
import sqlite3 as sq
class database:
    def __init__(self):
        self.self = self

    def create_table(self):
        try:
            conn = sq.connect("login.db")
            c = conn.cursor()
            c.execute("""CREATE TABLE IF NOT EXISTS login (
                USERNAME        TEXT    PRIMARY KEY     NOT NULL,
                PASSWORD        TEXT                    NOT NULL,
                ADMIN_STATUS    BOOLEAN DEFAULT FALSE   NOT NULL""")
            conn.commit()
            conn.close()
        except Exception() as e:
            print(e)
            return False
l
    def insert_data(self, username, password, admin_status=False):
        try:
            conn = sq.connect("login.db")
            c = conn.cursor()
            c.execute("INSERT INTO login VALUES (?,?,?)", (username, password, admin_status))
            conn.commit()
            conn.close()
        except Exception() as e:
            print(e)
            return False 

class LoginWindow: # Create a login window
    def __init__(self, window, window_title): # Initialise the login window
        self.window = window # Create a window
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

        Label(window, text="Password: ", bg="light blue").pack() # Create a label for the password entry box
        Entry(window, textvariable=self.password, show="*").pack() # Create an entry box for the password

        Label(window, text="", bg="light blue").pack() # Create a space between the entry box and the login button

        # Login button
        Button(window, text="Login", width=10, height=1, command=self.login).pack() 

        #exit button
        Button(window, text="Exit", width=10, height=1, command=lambda: sys.exit()).pack()


    def login(self): # Create a login function
        # Get username and password
        username = self.username.get()
        password = self.password.get()

        # Check if username and password is valid
        if self.is_valid_username(username) and self.is_valid_password(password):
            messagebox.showinfo("Login info", "Welcome " + username + "!")
            Mesh.mesh()
        else:
            messagebox.showerror("Login error", "Invalid username or password")

    # Check if username is valid
    def is_valid_username(self, username):
        try:
            My_Validation.is_valid_string(username)
        except:
            return False
        
    # Check if password is valid
    def is_valid_password(self, password):
        try:
            My_Validation.is_valid_string(password)
        except:
            return False
        
# Create a window and pass it to the Application object
LoginWindow(Tk(), "Tkinter Login Form")

# Run the mainloop
mainloop()


