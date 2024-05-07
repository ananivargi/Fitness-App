import tkinter as tk
from tkinter import messagebox

# Dictionary to store user credentials
userLogin = {}

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username in userLogin and userLogin[username] == password:
        messagebox.showinfo("Login Successful", "Welcome, {}".format(username))
    else:
        messagebox.showerror("Login Failed", "Please enter a valid username and password.")

def register():
    username = username_entry.get()
    password = password_entry.get()

    if username and password:
        if username in userLogin:
            messagebox.showerror("Registration Failed", "Username already exists")
        else:
            userLogin[username] = password
            messagebox.showinfo("Registration Successful", "Welcome, {}".format(username))
    else:
        messagebox.showerror("Registration Failed", "Please enter both username and password")

# Create main window
window = tk.Tk()
window.title("BodyWise Fitness App")
window.geometry('340x440')
window.configure(bg='#333333')


frame = tk.Frame(bg='#333333')

# Creating widgets
login_label = tk.Label(
    frame, text="BodyWise Fitness App", bg='#33bbff', fg="#FFFFFF", font=("Arial", 30))
username_label = tk.Label(
    frame, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
username_entry = tk.Entry(frame, font=("Arial", 16))
password_entry = tk.Entry(frame, show="*", font=("Arial", 16))
password_label = tk.Label(
    frame, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))

#Login Button
login_button = tk.Button(
    frame, text="Login", bg="#33bbff", fg="#FFFFFF", font=("Arial", 16), command=login)

# Register Button
register_button = tk.Button(
    frame, text="Register", bg="#33bbff", fg="#FFFFFF", font=("Arial", 16), command=register)


# Placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)
register_button.grid(row=4, column=0, columnspan=2, pady=10)

frame.pack()

window.mainloop()


