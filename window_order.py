import tkinter as tk

class app(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)

        mybut = tk.Button(self, text="switch window", 
        command=lambda: self.switch_window(second))
        mybut.pack()

        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Save settings", command = lambda: popupmsg("Not supported just yet!"))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=quit)
        menubar.add_cascade(label="File", menu=filemenu)

        tk.Tk.config(self, menu=menubar)
        self.frames={}
        for F in (first, second):
            frame = F(container)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.switch_window(first)

    def switch_window(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class first(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        my_lbl = tk.Label(self, text="Page two")
        my_lbl.pack()

class second(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        my_lbl = tk.Label(self, text="Page one")
        my_lbl.pack()

if __name__ == "__main__":
    root = app()
    root.geometry("600x400")
    root.mainloop()