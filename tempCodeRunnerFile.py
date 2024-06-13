#Import Tkinter and modules 

import tkinter as tk
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

# Parent class
class MainApp(tk.Tk):
    # Initialise window and user attributes
    def __init__(self):
        super().__init__()
        self.title("BodyWise Fitness App")
        self.geometry('800x800')
        self.configure(bg='#333333')
        self.username = ''
        self.password = ''
        self.name = ''
        self.age = ''
        self.gender = ''
        self.height = ''
        self.weight = ''
        self.vo2 = ''
        self.frames = {}
        self.create_frames()
        self.show_frame(LoginPage)

    def create_frames(self):
        self.frames[LoginPage] = LoginPage(parent=self, controller=self)
        self.frames[HomePage] = HomePage(parent=self, controller=self)
        self.frames[RegisterWindow] = RegisterWindow(parent=self, controller=self)
        self.frames[ProfilePage] = ProfilePage(parent=self,controller=self)
        self.frames[bmiPage] = bmiPage(parent=self,controller=self)
        self.frames[vo2maxPage] = vo2maxPage(parent = self, controller=self)
        for frame in self.frames.values():
            # Create grid for each frame
            frame.grid(row=0, column=0, sticky="nsew")

    # Show required frame when called 
    def show_frame(self, page_class):
        frame = self.frames[page_class]
        frame.tkraise()

    def check_login(self, username, password):
        '''
        Checks that username exists in data file and corresponds to given password.
        Takes entered username and password and returns a string that dictates if the
        username and password is correct
        '''
        value = ''
        with open('userlogininfo.txt', 'r') as f:
            lines = f.readlines()
            # Iterate through each line in file 
            for line in lines:
                # Check username matches with given username 
                if line.split(';')[0] == username:
                    value += 'username'
                    # Check the corresponding password
                    if line.split(';')[1] == password:
                        value += 'password'
        return value

    # Get attributes from text file
    def set_user_info(self, username):
        with open('userlogininfo.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                if line.split(';')[0] == username:
                    self.username = (line.split(';')[0])
                    self.password = line.split(';')[1]
                    self.name = str(line.split(';')[2]).capitalize()
                    self.age = int(line.split(';')[3])
                    self.gender = (line.split(';')[4])
                    self.height = float(line.split(';')[5])
                    self.weight = float(line.split(';')[6])
                    self.vo2 = int(line.split(';')[7])
    
    # Check all fields are valid 
    def check_inputs(self, username, password, name, age, gender, height, weight, vo2):
        '''
        Checks all fields are valid:
        Name --> Must only contain letters
        Age --> Must be between 5 and 105
        Height --> Must be between 50 and 220 cm
        Weight --> Must be between 20 and 500 kg 
        Vo2 Max --> Must be between 10 and 90
        Returns name of first invalid field (None returned if no error)
        Writes data line to userdata text file
        '''
        if not name.isalpha():
            return 'name'
        try:
            if not 5 <= int(age) <= 105:
                return 'age'
        except ValueError:
            return 'age'
        try:
            if not 50 <= float(height) <= 220:
                return 'height'
        except ValueError:
            return 'height'
        try:
            if not 20 <= float(height) <= 500:
                return 'weight'
        except ValueError:
            return 'weight'
        try:
            if not 10 <= int(vo2) <= 90:
                return 'vo2 max'
        except ValueError:
            return 'vo2 max'
        else:
            with open('userlogininfo.txt', 'a') as f:
                # Write data line to file
                f.write(f'{username};{password};{name};{age};{gender};{height};{weight};{vo2}\n')
            f.close()
        return None

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg='#333333')
        
        login_label = tk.Label(self, text="BodyWise", bg='#333333', fg="#468ce8", font=("Arial", 30))
        login_label.grid(row=0, column=0, columnspan=2, pady=40)
        
        username_label = tk.Label(self, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        username_label.grid(row=1, column=0, padx=20)
        self.username_entry = tk.Entry(self, font=("Arial", 16))
        self.username_entry.grid(row=1, column=1, pady=20)
        
        password_label = tk.Label(self, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        password_label.grid(row=2, column=0, padx=20)

        self.password_entry = tk.Entry(self, show="*", font=("Arial", 16))
        self.password_entry.grid(row=2, column=1, pady=20)

        
        login_button = tk.Button(self, text="Login", bg="#468ce8", fg="#FFFFFF", font=("Arial", 16), command=self.login)
        login_button.grid(row=3, column=0, columnspan=2, pady=30)
        
        register_button = tk.Button(self, text="Register", bg="#468ce8", fg="#FFFFFF", font=("Arial", 16), command=self.register)
        register_button.grid(row=4, column=0, columnspan=2, pady=10)
        
    def login(self):
        '''
        Checks username and password is valid by calling 'check login' method
        Show Home Page if valid else ask user to enter valid details
        '''
        username = self.username_entry.get()
        password = self.password_entry.get()
        user_info = self.controller.check_login(username, password)
        if user_info == 'usernamepassword':
            self.controller.set_user_info(username)
            self.controller.frames[HomePage].update_welcome_message(self.controller.name)
            self.controller.show_frame(HomePage)
        else:
            messagebox.showerror("Login Failed", "Please enter a valid username and password.")

    # Show register frame
    def register(self):
        self.controller.show_frame(RegisterWindow)

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg='#333333')

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=0)  # Sidebar column
        self.grid_columnconfigure(1, weight=1)  # Main content column

        # Sidebar
        self.sidebar_frame = tk.Frame(self, bg='#468ce8', width=50, height=800)  # Sidebar frame
        self.sidebar_frame.grid(row=0, column=0, rowspan=2, sticky="ns")
        self.sidebar_frame.grid_propagate(False)

        self.profile_button = tk.Button(self.sidebar_frame, text='', bg='#468ce8', relief='flat', command=self.go_profile)
        self.bmi_button = tk.Button(self.sidebar_frame, text='', bg='#468ce8', relief='flat', command=self.go_bmi)
        self.vo2max_button = tk.Button(self.sidebar_frame, text='', bg='#468ce8', relief='flat', command=self.go_vo2max)

        self.profile_button.grid(row=0, column=0, pady=10)
        self.bmi_button.grid(row=1, column=0, pady=50)
        self.vo2max_button.grid(row=2, column=0, pady=10)

        self.sidebar_frame.bind('<Enter>', lambda e: self.expand())
        self.sidebar_frame.bind('<Leave>', lambda e: self.contract())

        # Main content
        self.content_frame = tk.Frame(self, bg='#333333')
        self.content_frame.grid(row=0, column=1, sticky="nsew", rowspan=2)

        # Welcome label
        self.welcome_label = tk.Label(self.content_frame, text="", bg='#333333', fg="#FFFFFF", font=("Proxima Nova", 24))
        self.welcome_label.pack(pady=50)

        self.cur_width = 50
        self.max_width = 200
        self.min_width = 50
        self.expanded = False

    # Expand sidebar
    def expand(self):
        if self.cur_width < self.max_width:
            self.cur_width += 10
            self.sidebar_frame.config(width=self.cur_width)
            self.sidebar_frame.after(5, self.expand)
        else:
            self.expanded = True
            self.fill()

    # Contract sidebar
    def contract(self):
        if self.cur_width > self.min_width:
            self.cur_width -= 10
            self.sidebar_frame.config(width=self.cur_width)
            self.sidebar_frame.after(5, self.contract)
        else:
            self.expanded = False
            self.fill()

    def fill(self):
        if self.expanded:
            self.profile_button.config(text='Profile', font=("Proxima Nova", 14))
            self.bmi_button.config(text='BMI Calculator', font=("Proxima Nova", 14))
            self.vo2max_button.config(text='VO2 Max Range', font=("Proxima Nova", 14))
        else:
            self.profile_button.config(text='', font=("Proxima Nova", 10))
            self.bmi_button.config(text='', font=("Proxima Nova", 10))
            self.vo2max_button.config(text='', font=("Proxima Nova", 10))

    def update_welcome_message(self, name):
        self.welcome_label.config(text=f"Welcome, {name}")

    def go_profile(self):
        self.controller.frames[ProfilePage].show_info()
        self.controller.show_frame(ProfilePage)

    def go_bmi(self):
        self.controller.show_frame(bmiPage)

    def go_vo2max(self):
        self.controller.frames[vo2maxPage].find_range()
        self.controller.show_frame(vo2maxPage)



class RegisterWindow(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg='#333333')

        self.register_frame = tk.Frame(self, bg='#333333')

        # Enable field to get user data 

        new_username_label = tk.Label(self.register_frame, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        new_username_label.grid(row=0, column=0)
        self.new_username_entry = tk.Entry(self.register_frame, font=("Arial", 16))
        self.new_username_entry.grid(row=0, column=1, pady=10)

        new_password_label = tk.Label(self.register_frame, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        new_password_label.grid(row=1, column=0)
        self.new_password_entry = tk.Entry(self.register_frame, show="*", font=("Arial", 16))
        self.new_password_entry.grid(row=1, column=1, pady=10)

        name_label = tk.Label(self.register_frame, text="Name", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        name_label.grid(row=2, column=0)
        self.name_entry = tk.Entry(self.register_frame, font=("Arial", 16))
        self.name_entry.grid(row=2, column=1, pady=10)

        age_label = tk.Label(self.register_frame, text="Age", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        age_label.grid(row=3, column=0)
        self.age_entry = tk.Entry(self.register_frame, font=("Arial", 16))
        self.age_entry.grid(row=3, column=1, pady=10)

        height_label = tk.Label(self.register_frame, text="Height (cm)", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        height_label.grid(row=4, column=0)
        self.height_entry = tk.Entry(self.register_frame, font=("Arial", 16))
        self.height_entry.grid(row=4, column=1, pady=10)

        weight_label = tk.Label(self.register_frame, text="Weight (kg)", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        weight_label.grid(row=5, column=0)
        self.weight_entry = tk.Entry(self.register_frame, font=("Arial", 16))
        self.weight_entry.grid(row=5, column=1, pady=10)

        vo2_label = tk.Label(self.register_frame, text="VO2 Max", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        vo2_label.grid(row=6, column=0)
        self.vo2_entry = tk.Entry(self.register_frame, font=("Arial", 16))
        self.vo2_entry.grid(row=6, column=1, pady=10)

        gender_label = tk.Label(self.register_frame, text="Gender", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        gender_label.grid(row=7, column=0)
        self.gender_combobox = ttk.Combobox(self.register_frame, font=("Arial", 16), state="readonly")
        self.gender_combobox['values'] = ('Male', 'Female')
        self.gender_combobox.grid(row=7, column=1, pady=10)

        register_button = tk.Button(self.register_frame, text="Register", bg="#468ce8", fg="#FFFFFF", font=("Arial", 16), command=self.register_user)
        register_button.grid(row=8, column=0, columnspan=2, pady=20)

        self.register_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

    def register_user(self):
        username = self.new_username_entry.get()
        password = self.new_password_entry.get()
        name = self.name_entry.get()
        age = self.age_entry.get()
        height = self.height_entry.get()
        weight = self.weight_entry.get()
        vo2 = self.vo2_entry.get()
        gender = self.gender_combobox.get()

        invalid_input = self.controller.check_inputs(username, password, name, age, gender, height, weight, vo2)
        if invalid_input is None:
            messagebox.showinfo("Registration Successful", "Welcome, {}".format(username))
            self.controller.show_frame(HomePage)
        else:
            messagebox.showerror("Invalid Input", f"Please enter a valid {invalid_input}.")



class ProfilePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg='#333333')
        
    def show_info(self):
    # Get the current user information
        name = self.controller.name
        age = self.controller.age
        gender = self.controller.gender
        height = self.controller.height
        weight = self.controller.weight
        vo2 = self.controller.vo2
        profile_label = tk.Label(self, text="Profile", bg='#333333', fg="#468ce8", font=("Arial", 30))
        profile_label.grid(row=0, column=0, columnspan=2, pady=20)

        self.name_label = tk.Label(self, text="Name:", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        self.name_label.grid(row=1, column=0, sticky="w", padx=20)
        self.name_entry = tk.Entry(self, font=("Arial", 16))
        self.name_entry.grid(row=1, column=1, pady=10)
        self.name_entry.insert(0, name)  

        self.age_label = tk.Label(self, text="Age:", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        self.age_label.grid(row=2, column=0, sticky="w", padx=20)
        self.age_entry = tk.Entry(self, font=("Arial", 16))
        self.age_entry.grid(row=2, column=1, pady=10)
        self.age_entry.insert(0, age)  # Insert the current age into the field

        self.gender_label = tk.Label(self, text="Gender", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        self.gender_label.grid(row=3, column=0)
        self.gender_combobox = ttk.Combobox(self, font=("Arial", 16), state="readonly")
        self.gender_combobox['values'] = ('Male', 'Female')
        self.gender_combobox.grid(row=3, column=1, pady=10)
        self.gender_combobox.set(gender)


        self.height_label = tk.Label(self, text="Height (cm):", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        self.height_label.grid(row=4, column=0, sticky="w", padx=20)
        self.height_entry = tk.Entry(self, font=("Arial", 16))
        self.height_entry.grid(row=4, column=1, pady=10)
        self.height_entry.insert(0, str(height))  # Insert the current height into the field

        self.weight_label = tk.Label(self, text="Weight (kg):", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        self.weight_label.grid(row=5, column=0, sticky="w", padx=20)
        self.weight_entry = tk.Entry(self, font=("Arial", 16))
        self.weight_entry.grid(row=5, column=1, pady=10)
        self.weight_entry.insert(0, str(weight))  # Insert the current weight into the field

        self.vo2_label = tk.Label(self, text="VO2 Max:", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        self.vo2_label.grid(row=6, column=0, sticky="w", padx=20)
        self.vo2_entry = tk.Entry(self, font=("Arial", 16))
        self.vo2_entry.grid(row=6, column=1, pady=10)
        self.vo2_entry.insert(0, str(vo2))  # Insert the current VO2 into the field

        submit_button = tk.Button(self, text="Submit Changes", command=self.update_profile)
        submit_button.grid(row=8, column=0, columnspan=2)
        back_button = tk.Button(self, text="Back", bg="#468ce8", fg="#FFFFFF", font=("Arial", 16), command=self.back_to_home)
        back_button.grid(row= 15, column = 0, columnspan = 1)
        
    def back_to_home(self):
        self.controller.show_frame(HomePage)

    def update_profile(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        gender = self.gender_combobox.get()
        height = self.height_entry.get()
        weight = self.weight_entry.get()
        vo2 = self.vo2_entry.get()
        # Update user information
        updated_line = f'{self.controller.username};{self.controller.password};{name};{age};{gender};{height};{weight};{vo2}\n'
        with open('userlogininfo.txt', 'r+') as f:
            lines = f.readlines()
            f.seek(0)
            for line in lines:
                if line.split(';')[0] == self.controller.username:
                    f.write(updated_line)
                else:
                    f.write(line)

        # Update profile page with new information
        self.controller.set_user_info(self.controller.username)
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, name)
        self.age_entry.delete(0, tk.END)
        self.age_entry.insert(0, age)
        self.gender_combobox.delete(0, tk.END)
        self.gender_combobox.insert(0, gender)
        self.height_entry.delete(0, tk.END)
        self.height_entry.insert(0, height)
        self.weight_entry.delete(0, tk.END)
        self.weight_entry.insert(0, weight)
        self.vo2_entry.delete(0, tk.END)
        self.vo2_entry.insert(0, vo2)

        # Show a message box to confirm the changes
        messagebox.showinfo("Changes Saved", "Your profile has been updated successfully.")

class bmiPage(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg='#333333')
        self.bmi_button = tk.Button(self,text="Calculate BMI", bg='#333333', fg="#FFFFFF", font=("Arial", 24), command=self.calculate_bmi)
        self.bmi_button.grid(row=5, column=0, pady=20, padx=20)
        self.original_image = Image.open('bmirangeimage.png').resize((800,100))
        self.bmi_range_image = ImageTk.PhotoImage(self.original_image)
        self.pic_label = ttk.Label(self, image=self.bmi_range_image)
        self.pic_label.grid()
        
        self.pointer_image = Image.open('gaugepointer.png').resize((80,50))
        self.bmipointer_range_image = ImageTk.PhotoImage(self.pointer_image)
        self.pointer_label = ttk.Label(self, image=self.bmipointer_range_image)

        back_button = tk.Button(self, text="Back", bg="#468ce8", fg="#FFFFFF", font=("Arial", 16), command=self.back_to_home)
        back_button.grid(row= 15, column = 0, columnspan = 1)
        
    def back_to_home(self):
        self.controller.show_frame(HomePage)
        
        
    def calculate_bmi(self):
        height_m = self.controller.height / 100
        weight_kg = self.controller.weight
        bmi = round(weight_kg / (height_m ** 2), 1) # round to 1 dp
        if bmi < 18.5:
            self.pointer_label.place(x = 50, y = 50) 
        elif 18.5 <= bmi <= 24.9:
            self.pointer_label.place(x = 220, y = 50) 
        elif 25 <= bmi <= 29.9:
            self.pointer_label.place(x = 380, y = 50 )
        elif 30 <= bmi <= 39.9:
            self.pointer_label.place(x = 520, y = 50)
        else:
            self.pointer_label.place(x = 690, y = 50)


        #messagebox.showinfo("BMI", f"Your BMI is: {bmi:.f}")
    
class vo2maxPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg='#333333') 
        back_button = tk.Button(self, text="Back", bg="#468ce8", fg="#FFFFFF", font=("Arial", 16), command=self.back_to_home)
        back_button.grid(row= 5, column = 0, columnspan = 1)
        
    def back_to_home(self):
        self.controller.show_frame(HomePage)
   
    def find_range(self):
        if self.controller.age < 18:
            self.vo2max_label = tk.Label(self, text="", bg='#333333', fg="#FFFFFF", font=("Arial", 24))
            self.vo2max_label.pack(pady=20)
            self.vo2max_label.config(text=f"Unfortunately you must be older than 18 years old for your Vo2 Max Range to be determined.")
            
        else:
            category = ''
            if self.controller.gender == 'Female':
                f = open('vo2maxwomen.txt', 'r')
            else:
                f = open('vo2maxmen.txt','r')
            lines = f.readlines()
            for line in lines:
                #Check if age category matches 
                if int(line.split(';')[0].split('-')[0]) <= int(self.controller.age) <= int(line.split(';')[0].split('-')[1]):
                    category = 'very poor'
                    #Check which vo2 max category matches and give a rating based on position in file 
                    for i in range(6):
                        if int(line.split(';')[i+1].split('-')[0]) <= float(self.controller.vo2) <= int(line.split(';')[i+1].split('-')[1]):
                            category = self.find_category(i)
                            break
                    

                
                    
            self.vo2max_label = tk.Label(self, text="", bg='#333333', fg="#FFFFFF", font=("Arial", 24))
            self.vo2max_label.pack(pady=20)
            self.vo2max_label.config(text=f"Your VO2 Max is {self.controller.vo2} which is {category} for {self.controller.age} years old.")

    def find_category(self,number):
        #Determine the category based on the category in the file 
        if number == 0:
            return 'excellent'
        elif number == 1:
            return 'good'
        elif number == 2:
            return 'above average'
        elif number ==3:
            return 'average'
        elif number == 4:
            return 'below average'
        else:
            return 'poor'


  


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
