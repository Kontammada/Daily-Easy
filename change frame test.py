import Tkinter as tk
class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)###
        container = tk.Frame(self)###
        container.pack(side="top", fill="both", expand=True)###
        self.frames = {}###
        
        for F in (MainPage, New, StartPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, c):
        '''Show a frame for the given class'''
        frame = self.frames[c]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        ###just a label
        photo = tk.PhotoImage(file = "frame.gif")
        label = tk.Label(self, image = photo)
        label.image = photo #save reference of photo

        button1 = tk.Button(self, image = photo,command=lambda: controller.show_frame(MainPage),
                            )
        button1.pack()


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent) 
        label = tk.Label(self, text="This is page 1")
        label.pack(side="top", fill="x", pady=10)
        main_button = tk.Button(self, text="Back to Intro", command=lambda: controller.show_frame(StartPage))
        button2 = tk.Button(self, text="New", command=lambda: controller.show_frame(New))
        button3 = tk.Button(self, text="Go to the start page", command=lambda: controller.show_frame(StartPage))
        
        main_button.pack()
        button2.pack()
        button3.pack()


class New(tk.Frame):
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent) 
        label = tk.Label(self, text="New Ja!!!")
        label.pack(side="top", fill="x", pady=10)
        main_button = tk.Button(self, text="Go to the main page", command=lambda: controller.show_frame(MainPage))
        main_button.pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
