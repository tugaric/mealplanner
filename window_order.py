import tkinter as tk
import sqlite3
import get_sql_data as meal_db
from PIL import Image, ImageTk
from tkinter import ttk

class app(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        mybut = tk.Button(self, text="switch window", command=lambda: self.switch_window(second))
        mybut.pack()

# Menubar
        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Exit", command=quit)
        menubar.add_cascade(label="File", menu=filemenu)
        tk.Tk.config(self, menu=menubar)
        
        self.frames={}
        for F in (first, second):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.switch_window(first)

    def switch_window(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class first(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        # meal_list: A list of all the meals in the database
        # meal_ingredient: ingredients of the meal
        meals = meal_db.get_meals()
    
    # Treeview heading and column configuration
        columns = ("ingredient")
        my_tree = ttk.Treeview(self, columns=columns)
        # Configure heading names
        my_tree.heading("#0", text="meal")
        my_tree.heading("ingredient", text="ingredient")
        # configure column width
        my_tree.column("#0", width=150)
        
    # returns the id of this row
        for meal in meals:        # List[Tuple] => meal_ingredient = [("spaghetti", "pasta"), ("spaghetti", "haché"), ...
            meal_row = my_tree.insert(parent="", index=tk.END, text=meal.meal_name)
            for ingredient in meal.meal_ingredients:
                my_tree.insert(parent=meal_row, index=tk.END, values=(ingredient))
    # pack widget
        my_tree.pack()

class second(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        my_lbl = tk.Label(self, text="Page one")
        my_lbl.pack()
        my_button = tk.Button(self, text='Switch button', command=lambda: controller.switch_window(first))
        my_button.pack()

# create a treeview inside of a frame
class my_treeview(tk.Frame):
    def __init__(self, parent, column_name):
        super().__init__(parent)
        # columns = column_name
        self.tree = ttk.Treeview(self)
        self.tree.heading("#0", text=column_name)
        self.tree.pack()
        self.pack()

if __name__ == "__main__":
    root = app()
    root.geometry("600x400")
    root.mainloop()