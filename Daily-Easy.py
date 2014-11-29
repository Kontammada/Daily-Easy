import Tkinter as tk
import os
import datetime



class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)###
        container = tk.Frame(self)###
        container.pack(side="top", fill="both", expand=True)###
        self.frames = {}###
        for F in (MainPage, Work, House,  New, StartPage):
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
        button1 = tk.Button(self, image = photo,command=lambda: controller.show_frame(MainPage))
        button1.pack()
        work_dir = os.getcwd()
        check = os.listdir(work_dir)
        if 'Note-Data' not in check:
            os.mkdir("Note-Data")



class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent) 
        label = tk.Label(self, text="This is page 1")
        label.pack(side="top", fill="x", pady=10)
        main_button = tk.Button(self, text="Back to Intro", command=lambda: controller.show_frame(StartPage))
        button2 = tk.Button(self, text="New", command=lambda: controller.show_frame(New))
        button3 = tk.Button(self, text="Go to the start page", command=lambda: controller.show_frame(StartPage))
        button4 = tk.Button(self, text="Work *-*)//", command=lambda: controller.show_frame(Work))
        button5 = tk.Button(self, text="House _(:3 JL)_", command=lambda: controller.show_frame(House))
        main_button.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        button5.pack()


class New(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent) 
        label = tk.Label(self, text="New Ja!!!")
        label.place(x=130, y=30)
        main_button = tk.Button(self, text="Go to the main page", command=lambda: controller.show_frame(MainPage))
        main_button.place(x=95, y=550)
        self.title = tk.Label(self, text='Title')
        self.title.place(x=10, y=60)
        self.description = tk.Label(self, text='Description')
        self.description.place(x=10, y=110)
        self.text_title = tk.Text(self)
        self.text_title.config(width=35, heigh=1)
        self.text_title.place(x=10, y=80)
        self.text = tk.Text(self)
        self.text.config(width=35, heigh=15)
        self.text.place(x=10, y=130)
        self.button = tk.Button(self, text="Save", command=self.on_button)
        self.button.place(x=260, y=395)
        self.list_m = ['January', 'Fabruary', 'March', 'April', 'May', 'June',
                     'July', 'August', 'September', 'October', 'November', 'December']
        self.dict = {'January':range(1,32), 'Fabruary':range(1,30), 'March':range(1,32),
                     'April':range(1,31), 'May':range(1,32), 'June':range(1,31),
                     'July':range(1,32), 'August':range(1,32), 'September':range(1,31),
                     'October':range(1,32), 'November':range(1,31), 'December':range(1,32)}
        self.year = range(2014, 2031)
        self.variable_a = tk.StringVar(self)
        self.variable_b = tk.StringVar(self)
        self.variable_c = tk.StringVar(self)
        self.variable_a.trace('w', self.update_b)
        self.optionmenu_a = tk.OptionMenu(self, self.variable_a, *self.list_m)
        self.optionmenu_b = tk.OptionMenu(self, self.variable_b, *self.dict['January'])
        self.optionmenu_c = tk.OptionMenu(self, self.variable_c, *self.year)
        self.variable_a.set('January')
        self.variable_b.set(1)
        self.variable_c.set(2014)
        self.optionmenu_a.place(x=10, y=390)
        self.optionmenu_b.place(x=110, y=390)
        self.optionmenu_c.place(x=165, y=390)
        self.pack()
    def on_button(self):
        date = str(datetime.datetime.now().date())
        title = self.text_title.get('1.0', 'end-1c')
        name = date+" _ "+str(title)
        data = self.text.get('1.0', 'end-1c')
        new_file = open("Note-Data/"+name+".txt", "w+")
        alert = str(self.variable_c.get())+'-'+str(self.variable_a.get())+'-'+str(self.variable_b.get())
        new_file.write("%s\n\n%s" %(alert,data))
        self.text.delete('1.0', 'end')
        self.text_title.delete('1.0', 'end')
        self.success = tk.Label(self, text='...File saved...')
        self.success.place(x=117, y=440)
    def update_b(self, *args):
        value_a = self.dict[self.variable_a.get()]
        self.optionmenu_b.pack_forget()
        self.optionmenu_b = tk.OptionMenu(self, self.variable_b, *value_a)
        self.variable_b.set(1)
        self.optionmenu_b.place(x=110, y=390)    



class Work(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Workkkkkk!!!")
        label.pack(side="top", fill="x", pady=10)
        main_button = tk.Button(self, text="Go to the main page", command=lambda: controller.show_frame(MainPage))
        main_button.place(x=95, y=550)



class House(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="House =3=")
        label.pack(side="top", fill="x", pady=10)
        main_button = tk.Button(self, text="Go to the main page", command=lambda: controller.show_frame(MainPage))
        main_button.place(x=95, y=550)



if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
