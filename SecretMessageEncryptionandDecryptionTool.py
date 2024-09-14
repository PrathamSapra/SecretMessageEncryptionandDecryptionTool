from tkinter import *  # Imports all classes and functions from the Tkinter library for GUI development.
from tkinter import messagebox  # Imports the messagebox module from Tkinter for showing dialogs.
import base64  # Imports the base64 module for encoding and decoding data in base64 format.
import os  # Imports the os module for interacting with the operating system.

def decrypt():
    password = code.get()  # Retrieves the secret key entered by the user.

    if password == "1234":  # Checks if the entered password is correct.
        screen2 = Toplevel(screen)  # Creates a new top-level window.
        screen2.title("decryption")  # Sets the title of the new window.
        screen2.geometry("400x200")  # Sets the size of the new window.
        screen2.configure(bg="#00bd56")  # Sets the background color of the new window.

        message = text1.get(1.0, END)  # Retrieves the message from the text widget.
        decode_message = message.encode("ascii")  # Encodes the message in ASCII format.
        base64_bytes = base64.b64decode(decode_message)  # Decodes the base64-encoded message.
        decrypt = base64_bytes.decode("ascii")  # Decodes the bytes back to a string.

        # Creates a label to display the decryption title.
        Label(screen2, text="DECRYPT", font="arial", fg="white", bg="#00bd56").place(x=10, y=0)
        # Creates a text widget to display the decrypted message.
        text2 = Text(screen2, font="Rpbote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, decrypt)  # Inserts the decrypted message into the text widget.

    elif password == "":  # Checks if no password was entered.
        messagebox.showerror("encryption", "Input Password")  # Shows an error message.

    elif password != "1234":  # Checks if an incorrect password was entered.
        messagebox.showerror("encryption", "Invalid Password")  # Shows an error message.

def encrypt():
    password = code.get()  # Retrieves the secret key entered by the user.

    if password == "1234":  # Checks if the entered password is correct.
        screen1 = Toplevel(screen)  # Creates a new top-level window.
        screen1.title("encryption")  # Sets the title of the new window.
        screen1.geometry("400x200")  # Sets the size of the new window.
        screen1.configure(bg="#ed3833")  # Sets the background color of the new window.

        message = text1.get(1.0, END)  # Retrieves the message from the text widget.
        encode_message = message.encode("ascii")  # Encodes the message in ASCII format.
        base64_bytes = base64.b64encode(encode_message)  # Encodes the message in base64 format.
        encrypt = base64_bytes.decode("ascii")  # Decodes the bytes back to a string.

        # Creates a label to display the encryption title.
        Label(screen1, text="ENCRYPT", font="arial", fg="white", bg="#ed3833").place(x=10, y=0)
        # Creates a text widget to display the encrypted message.
        text2 = Text(screen1, font="Rpbote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, encrypt)  # Inserts the encrypted message into the text widget.

    elif password == "":  # Checks if no password was entered.
        messagebox.showerror("encryption", "Input Password")  # Shows an error message.

    elif password != "1234":  # Checks if an incorrect password was entered.
        messagebox.showerror("encryption", "Invalid Password")  # Shows an error message.

def main_screen():
    global screen  # Declares that 'screen' is a global variable.
    global code  # Declares that 'code' is a global variable.
    global text1  # Declares that 'text1' is a global variable.

    screen = Tk()  # Creates the main application window.
    screen.geometry("375x398")  # Sets the size of the main window.

    # Sets an icon for the application window.
    image_icon = PhotoImage(file="keys.png")  # Loads an image file for the icon.
    screen.iconphoto(False, image_icon)  # Sets the icon of the window.
    screen.title("PctApp")  # Sets the title of the main window.

    def reset():
        code.set("")  # Clears the secret key input field.
        text1.delete(1.0, END)  # Clears the text widget.

    # Creates a label for entering text for encryption and decryption.
    Label(text="Enter text for encryption and decryption", fg="black", font=("calibri", 13)).place(x=10, y=10)
    # Creates a text widget for entering the message.
    text1 = Text(font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=10, width=355, height=100)

    # Creates a label for entering the secret key.
    Label(text="Enter Secret Key for encryption and decryption", fg="black", font=("calibri", 13)).place(x=10, y=170)

    code = StringVar()  # Creates a variable to store the secret key.
    # Creates an entry widget for the secret key.
    Entry(textvariable=code, width=19, bd=0, font=("arial", 25), show="*").place(x=10, y=200)

    # Creates a button for encryption.
    Button(text="ENCRYPT", height="2", width=23, bg="#ed3833", fg="white", bd=0, command=encrypt).place(x=10, y=250)
    # Creates a button for decryption.
    Button(text="DECRYPT", height="2", width=23, bg="#00bd56", fg="white", bd=0, command=decrypt).place(x=200, y=250)
    # Creates a button to reset the fields.
    Button(text="RESET", height="2", width=50, bg="#1089ff", fg="white", bd=0, command=reset).place(x=10, y="300")

    screen.title("PctApp")  # Sets the title of the main window.

    screen.mainloop()  # Starts the Tkinter event loop, displaying the main window.

main_screen()  # Calls the main_screen function to run the application.
