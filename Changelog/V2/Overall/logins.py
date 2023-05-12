# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# inital Login Window before username verification is applied           #
# Name: Ben Deaville                                                    #
# Known Bugs: none                                                      #
# Ideas to be added: auto selection of buttons so user can 'hit' enter  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
from tkinter import *
from tkinter import messagebox
import sys
import My_Validation
import Mesh


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

        # Check if username and password is valid using My Validation, then runs 
        if My_Validation.is_valid_username(username) and My_Validation.is_valid_password(password):
            messagebox.showinfo("Login Successful", "Welcome " + username + "!")
            self.window.destroy()
            print("Destroyed")
            Mesh.mesh()
        else:
            messagebox.showerror("Login Error", "Invalid username or password.\nPlease try again.")



    # Check if username is valid

# Create a window and pass it to the Application object
LoginWindow(Tk(), "Tkinter Login Form")

# Run the mainloop
mainloop()