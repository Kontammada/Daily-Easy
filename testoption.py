import Tkinter as tk

class App(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.dict = {'Jan':range(1, 32), 'Fab':[1,2,3,4,5]}
        self.variable_a = tk.StringVar(self)
        self.variable_b = tk.StringVar(self)
        self.variable_a.trace('w', self.update_b)
        self.optionmenu_a = tk.OptionMenu(self, self.variable_a, *self.dict.keys())
        self.optionmenu_b = tk.OptionMenu(self, self.variable_b, *self.dict['Jan'])
        self.variable_a.set('Jan')
        self.variable_b.set(1)
        self.optionmenu_a.pack()
        self.optionmenu_b.pack()
        self.pack()
    def update_b(self, *args):
        value_a = self.dict[self.variable_a.get()]
        self.optionmenu_b.pack_forget()
        self.variable_b.set(1)
        self.optionmenu_b = tk.OptionMenu(self, self.variable_b, *value_a)
        self.optionmenu_b.pack()

root = tk.Tk()
app = App(root)
app.mainloop()
