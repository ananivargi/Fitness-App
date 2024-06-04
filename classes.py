import tkinter as tk
from tkinter import messagebox

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("BodyWise Fitness App")
        self.geometry('340x440')
        self.configure(bg='#333333')

        self.frames = {}
        self.create_frames()
        self.show_frame(LoginPage)

    def create_frames(self):
        self.frames[LoginPage] = LoginPage(parent=self, controller=self)
        self.frames[HomePage] = HomePage(parent=self, controller=self)
        self.frames[RegisterWindow] = RegisterWindow(parent=self, controller = self)

        for frame in self.frames.values():
            frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, page_class):
        frame = self.frames[page_class]
        frame.tkraise()

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg='#333333')
        
        login_label = tk.Label(self, text="BodyWise", bg='#333333', fg="#468ce8", font=("Arial", 30))
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
        if check_login(username, password) == 'usernamepassword':
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
        label = tk.Label(self, text=f"Welcome, user", bg='#333333', fg="#FFFFFF", font=("Arial", 24))
        label.pack(pady=20)
        logout_button = tk.Button(self, text="Logout", bg="#468ce8", fg="#FFFFFF", font=("Arial", 16), command=lambda: controller.show_frame(LoginPage))
        logout_button.pack(pady=10)
        #get height and weight from file (put as user info in Main class. Use to display BMI w/ a recommendation.)
        #separate data visualiser page; target goal. current. 

class RegisterWindow(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
       # self.title("Register")
       # self.geometry('340x440')
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

        height_label = tk.Label(self.register_frame, text="Height", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        height_label.grid(row=4, column=0)
        self.height_entry = tk.Entry(self.register_frame, font=("Arial", 16))
        self.height_entry.grid(row=4, column=1, pady=10)

        weight_label = tk.Label(self.register_frame, text="Weight", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        weight_label.grid(row=5, column=0)
        self.weight_entry = tk.Entry(self.register_frame, font=("Arial", 16))
        self.weight_entry.grid(row=5, column=1, pady=10)

        vo2_max_label = tk.Label(self.register_frame, text="VO2 Max", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        vo2_max_label.grid(row=6, column=0)
        self.vo2_max_entry = tk.Entry(self.register_frame, font=("Arial", 16))
        self.vo2_max_entry.grid(row=6, column=1, pady=10)

        register_button = tk.Button(self.register_frame, text="Register", bg="#468ce8", fg="#FFFFFF", font=("Arial", 16), command=self.register_user)
        register_button.grid(row=7, column=0, columnspan=2, pady=10)

        self.register_frame.pack()

    def register_user(self):
        username = self.new_username_entry.get()
        password = self.new_password_entry.get()
        name = self.name_entry.get()
        age = self.age_entry.get()
        height = self.height_entry.get()
        weight = self.weight_entry.get()
        vo2_max = self.vo2_max_entry.get()

        if username and password and name and age and height and weight and vo2_max:
            if 'username' in check_login(username, password):
                messagebox.showerror("Registration Failed", "Username already exists")
            else:
                #Find out whether there is an error in the field and store in a variable to print relevant error message
                error = check_inputs(username, password, name, age, height, weight, vo2_max)
                print(error)
                if not(error):
                    messagebox.showinfo("Registration Successful", "Welcome, {}".format(username))
                    #self.destroy()
                    self.controller.show_frame(HomePage)
                else:
                    messagebox.showerror("Registration Failed", f"Invalid input for {error} field. ")
        else:
            messagebox.showerror("Registration Failed", "Please fill in all fields")

# Functions for login and user data management
def check_login(username, password):
    value = ''
    with open('userlogininfo.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            if line.split(';')[0] == username:
                value += 'username'
                if line.split(';')[1] == password:
                    value += 'password'
    return value

def check_inputs(username, password, name, age, height, weight, vo2):
    if not isinstance(name, str):
        return 'name'
    #elif not isinstance(age, int) or not(5<age<105):
      #  return 'age'
    #elif not isinstance(height, float) or type(height) != 'int':
      #  return 'height'
    #elif not isinstance(weight,'float') or not(20<weight<500):
     #   return 'weight'
    #elif not isinstance(vo2, int) or not(5<vo2<100):
     #   return 'vo2'
    else:
        #Add data fields to text file if all valid
        with open('userlogininfo.txt', 'a') as f:
          f.write(f'{username};{password};{name};{age};{height};{weight};{vo2}\n')
        f.close()
    #return None

        

# Run the application
if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
