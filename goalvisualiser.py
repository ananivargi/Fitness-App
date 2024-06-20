import tkinter as tk
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

#Import Matplotlib and modules
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# Parent class
class MainApp(tk.Tk):
    # Initialise window and user attributes
    def __init__(self):
        super().__init__()
        self.title("BodyWise Fitness App")
        self.geometry('1000x1200')
        self.resizable(False, False)
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
        self.show_frame(GoalVisualiserPage)

    def create_frames(self):
        self.frames[GoalVisualiserPage] = GoalVisualiserPage(parent=self, controller=self)
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

class GoalVisualiserPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg='#333333')

        self.goal_sleep = tk.IntVar()
        self.goal_calories = tk.IntVar()
        self.goal_steps = tk.IntVar()
        self.actual_sleep = tk.IntVar()
        self.actual_calories = tk.IntVar()
        self.actual_steps = tk.IntVar()

        tk.Label(self, text="Goal Visualiser", bg='#333333', fg="#468ce8", font=("Arial", 30)).grid(row=0, column=0, columnspan=4, pady=20)

        # Graph section
        self.figure, self.ax = plt.subplots(figsize=(10, 5))
        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas.get_tk_widget().grid(row=1, column=0, columnspan=4, padx=20, pady=20)

        # Goal and Actual inputs
        tk.Label(self, text="Enter Goals and Actual Values", bg='#333333', fg="#FFFFFF", font=("Arial", 16)).grid(row=2, column=0, columnspan=4, pady=20)

        tk.Label(self, text="Sleep Goal (hours):", bg='#333333', fg="#FFFFFF", font=("Arial", 14)).grid(row=3, column=0, padx=10, pady=5, sticky='e')
        tk.Entry(self, textvariable=self.goal_sleep, font=("Arial", 14)).grid(row=3, column=1, padx=10, pady=5, sticky='w')

        tk.Label(self, text="Calories Burned Goal:", bg='#333333', fg="#FFFFFF", font=("Arial", 14)).grid(row=4, column=0, padx=10, pady=5, sticky='e')
        tk.Entry(self, textvariable=self.goal_calories, font=("Arial", 14)).grid(row=4, column=1, padx=10, pady=5, sticky='w')

        tk.Label(self, text="Steps Goal:", bg='#333333', fg="#FFFFFF", font=("Arial", 14)).grid(row=5, column=0, padx=10, pady=5, sticky='e')
        tk.Entry(self, textvariable=self.goal_steps, font=("Arial", 14)).grid(row=5, column=1, padx=10, pady=5, sticky='w')

        tk.Label(self, text="Actual Sleep (hours):", bg='#333333', fg="#FFFFFF", font=("Arial", 14)).grid(row=3, column=2, padx=10, pady=5, sticky='e')
        tk.Entry(self, textvariable=self.actual_sleep, font=("Arial", 14)).grid(row=3, column=3, padx=10, pady=5, sticky='w')

        tk.Label(self, text="Actual Calories Burned:", bg='#333333', fg="#FFFFFF", font=("Arial", 14)).grid(row=4, column=2, padx=10, pady=5, sticky='e')
        tk.Entry(self, textvariable=self.actual_calories, font=("Arial", 14)).grid(row=4, column=3, padx=10, pady=5, sticky='w')

        tk.Label(self, text="Actual Steps:", bg='#333333', fg="#FFFFFF", font=("Arial", 14)).grid(row=5, column=2, padx=10, pady=5, sticky='e')
        tk.Entry(self, textvariable=self.actual_steps, font=("Arial", 14)).grid(row=5, column=3, padx=10, pady=5, sticky='w')

        tk.Button(self, text="Update Graph", bg="#468ce8", fg="#FFFFFF", font=("Arial", 16), command=self.update_graph).grid(row=6, column=0, columnspan=4, pady=20)

        back_button = tk.Button(self, text="Back", bg="#468ce8", fg="#FFFFFF", font=("Arial", 16))
        back_button.grid(row=7, column=0, columnspan=4, pady=20)


    def update_graph(self):
        goals = [self.goal_sleep.get(), self.goal_calories.get(), self.goal_steps.get()]
        actuals = [self.actual_sleep.get(), self.actual_calories.get(), self.actual_steps.get()]
        categories = ['Sleep (hours)', 'Calories Burned', 'Steps Taken']

        self.ax.clear()
        y_pos = np.arange(len(categories))

        self.ax.barh(y_pos - 0.2, goals, height=0.4, label='Goal', color='r')
        self.ax.barh(y_pos + 0.2, actuals, height=0.4, label='Actual', color='b')

        self.ax.set_yticks(y_pos)
        self.ax.set_yticklabels(categories)
        self.ax.invert_yaxis()
        self.ax.legend()
        self.ax.set_xlim(0, max(goals + actuals) * 1.1)

        self.canvas.draw()

app = MainApp()
app.mainloop()