import Tkinter as tk

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.text = tk.Text(self)
        self.button = tk.Button(self, text="Get", command=self.on_button)
        self.button.pack()
        self.text.pack()

    def on_button(self):
        print self.text.get('1.0', 'end-1c')

app = SampleApp()
app.mainloop()
