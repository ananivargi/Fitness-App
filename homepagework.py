import tkinter as tk
from tkinter import messagebox

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("BodyWise Fitness App")
        self.geometry('800x800')
        self.configure(bg='#333333')
        self.name = ''
        self.age = ''
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
                    self.name = str(line.split(';')[2])
                    self.age = int(line.split(';')[3])
                    self.height = float(line.split(';')[4])
                    self.weight = float(line.split(';')[5])
                    self.vo2 = int(line.split(';')[6])

    def check_inputs(self, username, password, name, age, height, weight, vo2):
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
            if not 10 < vo2 < 100:
                return 'vo2 max'
        except ValueError:
            return 'vo2 max'
        else:
            with open('userlogininfo.txt', 'a') as f:
                f.write(f'{username};{password};{name};{age};{height};{weight};{vo2}\n')
            f.close()
        return None

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg='#333333')
        
        login_label = tk.Label(self, text="BodyWise", bg='#333333', fg="#468ce8", font=("Arial", 30))
        #login_label.place(relx = 0.5, rely = 0.5, anchor = 'center')
        username_label = tk.Label(self, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        self.username_entry = tk.Entry(self, font=("Arial", 16))
        password_label = tk.Label(self, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        self.password_entry = tk.Entry(self, show="*", font=("Arial", 16))
        login_button = tk.Button(self, text="Login", bg="#468ce8", fg="#FFFFFF", font=("Arial", 16), command=self.login)
        register_button = tk.Button(self, text="Register", bg="#468ce8", fg="#FFFFFF", font=("Arial", 16), command=self.register)

        login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
        username_label.grid(row=1, column=0)
        self.username_entry.grid(row=1, column=1, pady=20)
        password_label.grid(row=2, column=0)
        self.password_entry.grid(row=2, column=1, pady=20)
        login_button.grid(row=3, column=0, columnspan=2, pady=30)
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

        self.sidebar_frame = tk.Frame(self, bg='orange', width=50)
        self.sidebar_frame.pack(fill='y', side='right', anchor='e')
        
        self.sidebar_frame.bind('<Enter>', lambda e: self.expand())
        self.sidebar_frame.bind('<Leave>', lambda e: self.contract())

        self.home_button = tk.Button(self.sidebar_frame, text='', bg='orange', relief='flat', command=self.go_home)
        self.profile_button = tk.Button(self.sidebar_frame, text='', bg='orange', relief='flat', command=self.go_profile)
        self.goals_button = tk.Button(self.sidebar_frame, text='', bg='orange', relief='flat', command=self.go_goals)

        self.home_button.pack(pady=10)
        self.profile_button.pack(pady=50)
        self.goals_button.pack(pady=10)

        self.cur_width = 50
        self.max_width = 200
        self.min_width = 50
        self.expanded = False

        self.content_frame = tk.Frame(self, bg='#333333')
        self.content_frame.pack(side='left', fill='both', expand=True)

        self.welcome_label = tk.Label(self.content_frame, text="", bg='#333333', fg="#FFFFFF", font=("Arial", 24))
        self.welcome_label.pack(pady=20, padx=20, anchor="w")

        self.bmi_button = tk.Button(self.content_frame, text="Calculate BMI", bg='#333333', fg="#FFFFFF", font=("Arial", 24), command=self.calculate_bmi)
        self.bmi_button.pack(pady=20)

    def expand(self):
        if self.cur_width < self.max_width:
            self.cur_width += 10
            self.sidebar_frame.config(width=self.cur_width)
            self.sidebar_frame.after(5, self.expand)
        else:
            self.expanded = True
            self.fill()

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
            self.home_button.config(text='Home', font=("Arial", 14))
            self.profile_button.config(text='Profile', font=("Arial", 14))
            self.goals_button.config(text='Goals', font=("Arial", 14))
        else:
            self.home_button.config(text='', font=("Arial", 10))
            self.profile_button.config(text='', font=("Arial", 10))
            self.goals_button.config(text='', font=("Arial", 10))

    def update_welcome_message(self, name):
        self.welcome_label.config(text=f"Welcome, {name}")

    def calculate_bmi(self):
        try:
            height = float(self.controller.height) / 100  # Convert cm to meters
            weight = float(self.controller.weight)
            bmi = weight / (height ** 2)
            messagebox.showinfo("BMI", f"Your BMI is {bmi:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Invalid height or weight")

    def go_home(self):
        pass  # Implement the home functionality

    def go_profile(self):
        pass  # Implement the profile functionality

    def go_goals(self):
        pass  # Implement the goals functionality



class RegisterWindow(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg='#333333')

        self.register_frame = tk.Frame(self, bg='#333333')

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

        register_button = tk.Button(self.register_frame, text="Register", bg="#468ce8", fg="#FFFFFF", font=("Arial", 16), command=self.register_user)
        register_button.grid(row=7, column=0, columnspan=2, pady=20)

        self.register_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

    def register_user(self):
        username = self.new_username_entry.get()
        password = self.new_password_entry.get()
        name = self.name_entry.get()
        age = self.age_entry.get()
        height = self.height_entry.get()
        weight = self.weight_entry.get()
        vo2 = self.vo2_entry.get()

        invalid_input = self.controller.check_inputs(username, password, name, age, height, weight, vo2)
        if invalid_input is None:
            self.controller.show_frame(LoginPage)
        else:
            messagebox.showerror("Invalid Input", f"Please enter a valid {invalid_input}.")

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
