# Import relevant libraries
import tkinter as tk
from tkinter import messagebox

#Check user information
def check_login(username, password):
    ''' 
    Function receives the username and password entered in the 
    login box and determines whether both individually are valid 
    (they exist as part of one entry in the text file containing 
    user information)
    '''
    # Initialise variable that stores whether username/password found
    value = ''
    # Open user information file
    f = open('userlogininfo.txt', 'r')
    lines = f.readlines()
    # Iterate through each line in file
    for line in lines:
        # Check if the first item in line matches the username
        if line.split(';')[0] == username:
            value += 'username'
            # Check if second item in line matches password
            if line.split(';')[1] == password:
                value += 'password'
    f.close()
    # Return which fields matched file entry
    return value
            
            
def new_user(username,password,name, age, height, weight, vo2):
    '''
    Creates a new entry in the text file for new user profile
    '''
    f = open('userlogininfo.txt', 'a')
    f.write(f'{username};{password};{age};{height};{weight};{vo2}\n')
    f.close()
    
def check_valid_fields(username,password,name, age, height, weight, vo2):
    '''
    Checks whether the given info for each field is valid.
    Username mustn't have any spaces, name must only be letters
    Age must be number, at least 10
    
    '''
    pass


def login():
    username = username_entry.get()
    password = password_entry.get()

    if check_login(username, password) == 'usernamepassword':
        #messagebox.showinfo("Login Successful", "Welcome, {}".format(username))
        login_frame.pack_forget()
        home_frame.pack()
    else:
        messagebox.showerror("Login Failed", "Please enter a valid username and password.")

def register():
    def register_user():
        username = new_username_entry.get()
        password = new_password_entry.get()
        name = name_entry.get()
        age = age_entry.get()
        height = height_entry.get()
        weight = weight_entry.get()
        vo2_max = vo2_max_entry.get()

        if username and password and name and age and height and weight and vo2_max:
            if 'username' in check_login(username, password):
                messagebox.showerror("Registration Failed", "Username already exists")
            else:
                new_user(username,password,name,age,height, weight, vo2_max)

                messagebox.showinfo("Registration Successful", "Welcome, {}".format(username))
                # Clear the entry fields after registration
                new_username_entry.delete(0, tk.END)
                new_password_entry.delete(0, tk.END)
                name_entry.delete(0, tk.END)
                age_entry.delete(0, tk.END)
                height_entry.delete(0, tk.END)
                weight_entry.delete(0, tk.END)
                vo2_max_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Registration Failed", "Please fill in all fields")
    # Create a new window for registration
    register_window = tk.Toplevel(window)
    register_window.title("Register")
    register_window.geometry('340x440')
    register_window.configure(bg='#333333')

    register_frame = tk.Frame(register_window, bg='#333333')

    new_username_label = tk.Label(register_frame, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    new_username_label.grid(row=0, column=0)
    new_username_entry = tk.Entry(register_frame, font=("Arial", 16))
    new_username_entry.grid(row=0, column=1, pady=10)

    new_password_label = tk.Label(register_frame, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    new_password_label.grid(row=1, column=0)
    new_password_entry = tk.Entry(register_frame, show="*", font=("Arial", 16))
    new_password_entry.grid(row=1, column=1, pady=10)

    name_label = tk.Label(register_frame, text="Name", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    name_label.grid(row=2, column=0)
    name_entry = tk.Entry(register_frame, font=("Arial", 16))
    name_entry.grid(row=2, column=1, pady=10)

    age_label = tk.Label(register_frame, text="Age", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    age_label.grid(row=3, column=0)
    age_entry = tk.Entry(register_frame, font=("Arial", 16))
    age_entry.grid(row=3, column=1, pady=10)

    height_label = tk.Label(register_frame, text="Height", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    height_label.grid(row=4, column=0)
    height_entry = tk.Entry(register_frame, font=("Arial", 16))
    height_entry.grid(row=4, column=1, pady=10)
    
    weight_label = tk.Label(register_frame, text="Weight", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    weight_label.grid(row=4, column=0)
    weight_entry = tk.Entry(register_frame, font=("Arial", 16))
    weight_entry.grid(row=4, column=1, pady=10)

    vo2_max_label = tk.Label(register_frame, text="VO2 Max", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    vo2_max_label.grid(row=5, column=0)
    vo2_max_entry = tk.Entry(register_frame, font=("Arial", 16))
    vo2_max_entry.grid(row=5, column=1, pady=10)

    register_button = tk.Button(register_frame, text="Register", bg="#468ce8", fg="#FFFFFF", font=("Arial", 16), command=register_user)
    register_button.grid(row=6, column=0, columnspan=2, pady=10)

    register_frame.pack()

# Create main window
window = tk.Tk()
window.title("BodyWise Fitness App")
window.geometry('340x440')
window.configure(bg='#333333')

login_frame = tk.Frame(bg='#333333')

# Creating widgets
login_label = tk.Label(login_frame, text="BodyWise", bg='#333333', fg="#468ce8", font=("Arial", 30))
username_label = tk.Label(login_frame, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
username_entry = tk.Entry(login_frame, font=("Arial", 16))
password_entry = tk.Entry(login_frame, show="*", font=("Arial", 16))
password_label = tk.Label(login_frame, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))

#Login Button
login_button = tk.Button(login_frame, text="Login", bg="#468ce8", fg="#FFFFFF", font=("Arial", 16), command=login)

# Register Button
register_button = tk.Button(login_frame, text="Register", bg="#468ce8", fg="#FFFFFF", font=("Arial", 16), command=register)

# Placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)
register_button.grid(row=4, column=0, columnspan=2, pady=10)

home_frame = tk.Frame(bg='#223322')
home_frame_label = tk.Label(home_frame, text="Welcome to the Homepage!")
home_frame_label.pack(pady=20)

login_frame.pack()
home_frame.forget()

window.mainloop()
