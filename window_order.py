import tkinter as tk
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
        filemenu.add_command(label="Save settings", command = lambda: popupmsg("Not supported just yet!"))
        filemenu.add_separator()
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
    # Treeview
        columns = ("ingredient")

        my_tree = ttk.Treeview(self, columns=columns)
        my_tree.heading("#0", text="meal")
        my_tree.heading("ingredient", text="ingredient")
        
        # returns the id of this row
        meal_row = my_tree.insert(parent="", index=tk.END, text="Pizza")
        my_tree.insert(meal_row, index=tk.END, values=("cheese",))
        my_tree.insert(meal_row, index=tk.END, values=("tomato sauce",))
        my_tree.pack()

class second(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        my_lbl = tk.Label(self, text="Page one")
        my_lbl.pack()
        my_button = tk.Button(self, text='Switch button', command=lambda: controller.switch_window(first))
        my_button.pack()

if __name__ == "__main__":
    root = app()
    root.geometry("600x400")
    root.mainloop()