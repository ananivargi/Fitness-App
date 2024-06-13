import tkinter as tk
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

class MainApp(tk.Tk):
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
        self.frames[ProfilePage] = ProfilePage(parent=self, controller=self)
        self.frames[bmiPage] = bmiPage(parent=self, controller=self)
        self.frames[vo2maxPage] = vo2maxPage(parent=self, controller=self)
        for frame in self.frames.values():
            frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, page_class):
        frame = self.frames[page_class]
        frame.tkraise()

    def check_login(self, username, password):
        value = ''
        with open('userlogininfo.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                if line.split(';')[0] == username:
                    value += 'username'
                    if line.split(';')[1] == password:
                        value += 'password'
        return value

    def set_user_info(self, username):
        with open('userlogininfo.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                if line.split(';')[0] == username:
                    self.username = (line.split(';')[0])
                    self.password = line.split(';')[1]
                    self.name = (str(line.split(';')[2])).capitalize()
                    self.age = int(line.split(';')[3])
                    self.gender = (line.split(';')[4])
                    self.height = float(line.split(';')[5])
                    self.weight = float(line.split(';')[6])
                    self.vo2 = int(line.split(';')[7])

    def check_inputs(self, username, password, name, age, gender, height, weight, vo2):
        if not name.isalpha():
            return 'name'
        try:
            if not 5 < int(age) < 105:
                return 'age'
        except ValueError:
            return 'age'
        try:
            if not 50 < float(height) < 220:
                return 'height'
        except ValueError:
            return 'height'
        try:
            if not 20 < float(height) < 500:
                return 'weight'
        except ValueError:
            return 'weight'
        try:
            if not 10 < int(vo2) < 100:
                return 'vo2 max'
        except ValueError:
            return 'vo2 max'
        else:
            with open('userlogininfo.txt', 'a') as f:
                f.write(f'{username};{password};{name};{age};{gender};{height};{weight};{vo2}\n')
            f.close()
        return None

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg='#333333')
        
        login_label = tk.Label(self, text="BodyWise", bg='#333333', fg="#468ce8", font=("Proxima Nova", 30))
        login_label.grid(row=0, column=0, columnspan=2, pady=40)
        
        username_label = tk.Label(self, text="Username", bg='#333333', fg="#FFFFFF", font=("Proxima Nova", 16))
        username_label.grid(row=1, column=0, padx=20)
        self.username_entry = tk.Entry(self, font=("Proxima Nova", 16))
        self.username_entry.grid(row=1, column=1, pady=20)
        
        password_label = tk.Label(self, text="Password", bg='#333333', fg="#FFFFFF", font=("Proxima Nova", 16))
        password_label.grid(row=2, column=0, padx=20)

        self.password_entry = tk.Entry(self, show="*", font=("Proxima Nova", 16))
        self.password_entry.grid(row=2, column=1, pady=20)

        
        login_button = tk.Button(self, text="Login", bg="#468ce8", fg="#FFFFFF", font=("Proxima Nova", 16), command=self.login)
        login_button.grid(row=3, column=0, columnspan=2, pady=30)
        
        register_button = tk.Button(self, text="Register", bg="#468ce8", fg="#FFFFFF", font=("Proxima Nova", 16), command=self.register)
        register_button.grid(row=4, column=0, columnspan=2, pady=10)
        
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        user_info = self.controller.check_login(username, password)
        if user_info == 'usernamepassword':
            self.controller.set_user_info(username)
            self.controller.frames[HomePage].update_welcome_message(self.controller.name)
            self.controller.show_frame(HomePage)
        else:
            messagebox.showerror("Login Failed", "Please enter a valid username and password.")

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
        
        register_label = tk.Label(self, text="Register", bg='#333333', fg="#468ce8", font=("Proxima Nova", 30))
        register_label.grid(row=0, column=0, columnspan=2, pady=20)
        
        username_label = tk.Label(self, text="Username", bg='#333333', fg="#FFFFFF", font=("Proxima Nova", 16))
        username_label.grid(row=1, column=0, padx=20, pady=10, sticky='w')
        self.username_entry = tk.Entry(self, font=("Proxima Nova", 16))
        self.username_entry.grid(row=1, column=1, padx=20, pady=10)
        
        password_label = tk.Label(self, text="Password", bg='#333333', fg="#FFFFFF", font=("Proxima Nova", 16))
        password_label.grid(row=2, column=0, padx=20, pady=10, sticky='w')
        self.password_entry = tk.Entry(self, show="*", font=("Proxima Nova", 16))
        self.password_entry.grid(row=2, column=1, padx=20, pady=10)
        
        name_label = tk.Label(self, text="Name", bg='#333333', fg="#FFFFFF", font=("Proxima Nova", 16))
        name_label.grid(row=3, column=0, padx=20, pady=10, sticky='w')
        self.name_entry = tk.Entry(self, font=("Proxima Nova", 16))
        self.name_entry.grid(row=3, column=1, padx=20, pady=10)
        
        age_label = tk.Label(self, text="Age", bg='#333333', fg="#FFFFFF", font=("Proxima Nova", 16))
        age_label.grid(row=4, column=0, padx=20, pady=10, sticky='w')
        self.age_entry = tk.Entry(self, font=("Proxima Nova", 16))
        self.age_entry.grid(row=4, column=1, padx=20, pady=10)
        
        gender_label = tk.Label(self, text="Gender", bg='#333333', fg="#FFFFFF", font=("Proxima Nova", 16))
        gender_label.grid(row=5, column=0, padx=20, pady=10, sticky='w')
        self.gender_var = tk.StringVar()
        self.gender_combobox = ttk.Combobox(self, textvariable=self.gender_var, font=("Proxima Nova", 16), state='readonly')
        self.gender_combobox['values'] = ('Male', 'Female')
        self.gender_combobox.grid(row=5, column=1, padx=20, pady=10)
        
        height_label = tk.Label(self, text="Height (cm)", bg='#333333', fg="#FFFFFF", font=("Proxima Nova", 16))
        height_label.grid(row=6, column=0, padx=20, pady=10, sticky='w')
        self.height_entry = tk.Entry(self, font=("Proxima Nova", 16))
        self.height_entry.grid(row=6, column=1, padx=20, pady=10)
        
        weight_label = tk.Label(self, text="Weight (kg)", bg='#333333', fg="#FFFFFF", font=("Proxima Nova", 16))
        weight_label.grid(row=7, column=0, padx=20, pady=10, sticky='w')
        self.weight_entry = tk.Entry(self, font=("Proxima Nova", 16))
        self.weight_entry.grid(row=7, column=1, padx=20, pady=10)
        
        vo2_label = tk.Label(self, text="VO2 Max", bg='#333333', fg="#FFFFFF", font=("Proxima Nova", 16))
        vo2_label.grid(row=8, column=0, padx=20, pady=10, sticky='w')
        self.vo2_entry = tk.Entry(self, font=("Proxima Nova", 16))
        self.vo2_entry.grid(row=8, column=1, padx=20, pady=10)

        register_button = tk.Button(self, text="Register", bg="#468ce8", fg="#FFFFFF", font=("Proxima Nova", 16), command=self.register)
        register_button.grid(row=9, column=0, columnspan=2, pady=20)

        back_button = tk.Button(self, text="Back", bg="#468ce8", fg="#FFFFFF", font=("Proxima Nova", 14), command=self.go_back)
        back_button.grid(row=10, column=0, columnspan=2, pady=10)

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        name = self.name_entry.get()
        age = self.age_entry.get()
        gender = self.gender_var.get()
        height = self.height_entry.get()
        weight = self.weight_entry.get()
        vo2 = self.vo2_entry.get()
        
        error_field = self.controller.check_inputs(username, password, name, age, gender, height, weight, vo2)
        if error_field:
            messagebox.showerror("Invalid Input", f"Please enter a valid {error_field}.")
        else:
            messagebox.showinfo("Registration Successful", "You have been registered successfully!")
            self.controller.show_frame(LoginPage)

    def go_back(self):
        self.controller.show_frame(LoginPage)

class ProfilePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg='#333333')
        
        self.profile_label = tk.Label(self, text="Profile", bg='#333333', fg="#468ce8", font=("Proxima Nova", 30))
        self.profile_label.grid(row=0, column=0, columnspan=2, pady=20)
        
        self.info_text = tk.Text(self, font=("Proxima Nova", 16), width=50, height=15)
        self.info_text.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        self.info_text.configure(state='disabled')
        
        back_button = tk.Button(self, text="Back", bg="#468ce8", fg="#FFFFFF", font=("Proxima Nova", 14), command=self.go_back)
        back_button.grid(row=2, column=0, columnspan=2, pady=10)

    def show_info(self):
        self.info_text.configure(state='normal')
        self.info_text.delete("1.0", tk.END)
        user_info = f"""
        Username: {self.controller.username}
        Name: {self.controller.name}
        Age: {self.controller.age}
        Gender: {self.controller.gender}
        Height: {self.controller.height} cm
        Weight: {self.controller.weight} kg
        VO2 Max: {self.controller.vo2}
        """
        self.info_text.insert(tk.END, user_info)
        self.info_text.configure(state='disabled')

    def go_back(self):
        self.controller.show_frame(HomePage)

class bmiPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg='#333333')
        
        bmi_label = tk.Label(self, text="BMI Calculator", bg='#333333', fg="#468ce8", font=("Proxima Nova", 30))
        bmi_label.grid(row=0, column=0, columnspan=2, pady=20)
        
        height_label = tk.Label(self, text="Height (cm)", bg='#333333', fg="#FFFFFF", font=("Proxima Nova", 16))
        height_label.grid(row=1, column=0, padx=20, pady=10, sticky='w')
        self.height_entry = tk.Entry(self, font=("Proxima Nova", 16))
        self.height_entry.grid(row=1, column=1, padx=20, pady=10)
        
        weight_label = tk.Label(self, text="Weight (kg)", bg='#333333', fg="#FFFFFF", font=("Proxima Nova", 16))
        weight_label.grid(row=2, column=0, padx=20, pady=10, sticky='w')
        self.weight_entry = tk.Entry(self, font=("Proxima Nova", 16))
        self.weight_entry.grid(row=2, column=1, padx=20, pady=10)
        
        calculate_button = tk.Button(self, text="Calculate", bg="#468ce8", fg="#FFFFFF", font=("Proxima Nova", 16), command=self.calculate_bmi)
        calculate_button.grid(row=3, column=0, columnspan=2, pady=20)
        
        self.result_label = tk.Label(self, text="", bg='#333333', fg="#FFFFFF", font=("Proxima Nova", 16))
        self.result_label.grid(row=4, column=0, columnspan=2, pady=10)
        
        back_button = tk.Button(self, text="Back", bg="#468ce8", fg="#FFFFFF", font=("Proxima Nova", 14), command=self.go_back)
        back_button.grid(row=5, column=0, columnspan=2, pady=10)

    def calculate_bmi(self):
        try:
            height = float(self.height_entry.get()) / 100
            weight = float(self.weight_entry.get())
            bmi = weight / (height ** 2)
            self.result_label.config(text=f"Your BMI is {bmi:.2f}")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid height and weight values.")

    def go_back(self):
        self.controller.show_frame(HomePage)

class vo2maxPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg='#333333')
        
        vo2max_label = tk.Label(self, text="VO2 Max Calculator", bg='#333333', fg="#468ce8", font=("Proxima Nova", 30))
        vo2max_label.grid(row=0, column=0, columnspan=2, pady=20)
        
        distance_label = tk.Label(self, text="Distance (m)", bg='#333333', fg="#FFFFFF", font=("Proxima Nova", 16))
        distance_label.grid(row=1, column=0, padx=20, pady=10, sticky='w')
        self.distance_entry = tk.Entry(self, font=("Proxima Nova", 16))
        self.distance_entry.grid(row=1, column=1, padx=20, pady=10)
        
        time_label = tk.Label(self, text="Time (min)", bg='#333333', fg="#FFFFFF", font=("Proxima Nova", 16))
        time_label.grid(row=2, column=0, padx=20, pady=10, sticky='w')
        self.time_entry = tk.Entry(self, font=("Proxima Nova", 16))
        self.time_entry.grid(row=2, column=1, padx=20, pady=10)
        
        calculate_button = tk.Button(self, text="Calculate", bg="#468ce8", fg="#FFFFFF", font=("Proxima Nova", 16), command=self.calculate_vo2max)
        calculate_button.grid(row=3, column=0, columnspan=2, pady=20)
        
        self.result_label = tk.Label(self, text="", bg='#333333', fg="#FFFFFF", font=("Proxima Nova", 16))
        self.result_label.grid(row=4, column=0, columnspan=2, pady=10)
        
        back_button = tk.Button(self, text="Back", bg="#468ce8", fg="#FFFFFF", font=("Proxima Nova", 14), command=self.go_back)
        back_button.grid(row=5, column=0, columnspan=2, pady=10)

    def calculate_vo2max(self):
        try:
            distance = float(self.distance_entry.get())
            time = float(self.time_entry.get())
            vo2max = 15 * (distance / time)
            self.result_label.config(text=f"Your VO2 Max is {vo2max:.2f}")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid distance and time values.")

    def go_back(self):
        self.controller.show_frame(HomePage)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
