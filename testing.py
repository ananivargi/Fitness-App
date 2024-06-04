import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def plot_graph():
    # Data for the bar graph
    categories = ['A', 'B', 'C', 'D', 'E']
    values = [23, 45, 56, 78, 32]

    # Create a bar graph
    plt.bar(categories, values)
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.title('Bar Graph')

    # Embed the graph into tkintear
    canvas = FigureCanvasTkAgg(plt.gcf(), master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()

root = tk.Tk()
root.title("Bar Graph Example")

# Button to plot the graph
plot_button = ttk.Button(root, text="Plot Graph", command=plot_graph)
plot_button.pack()

root.mainloop()
