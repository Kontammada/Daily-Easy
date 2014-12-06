import Tkinter as tk
import os
from os import listdir
from os.path import isfile, join
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
        button1 = tk.Button(self, image = photo,command=lambda: controller.show_frame(MainPage), relief='flat')
        button1.pack()
        work_dir = os.getcwd()
        check = os.listdir(work_dir)
        if 'Note-Data' not in check:
            os.mkdir("Note-Data")



class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="main _/|\_")
        label.pack(side="top", fill="x", pady=10)
        self.edge = tk.Label(self, text="========================================")
        self.edge.place(y = 400)
        self.workbutton = tk.Button(self, text="Work *-*)//", command=lambda: controller.show_frame(Work),relief='groove')
        self.workbutton.place(x=5, y=425)
        self.housebutton = tk.Button(self, text="House _(:3 JL)_", command=lambda: controller.show_frame(House),relief='groove')
        self.housebutton.place(x=80, y=425)
        self.introbutton = tk.Button(self, text="Back to Intro", command=lambda: controller.show_frame(StartPage),relief='groove')
        self.introbutton.place(x=5, y=465)
        self.newbutton = tk.Button(self, text="New", command=lambda: controller.show_frame(New),relief='groove')
        self.newbutton.place(x=5, y=500)
        self.aboutbutton = tk.Button(self, text="About", command=lambda: controller.show_frame(About),relief='groove')
        self.aboutbutton.place(x=5, y=535)
        frame = tk.Frame(self)
        frame.place(x=7,y=40)
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side='right', fill='y')
        listbox = tk.Listbox(frame,width=45, height=22)
        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox.yview)
        listbox.bind("<Double-Button-1>", self.OnDouble)
        listbox.pack(side="top", fill="both", expand=True)
        now = os.getcwd()
        onlyfiles = [ f for f in listdir(now+'''/Note-Data''') if isfile(join(now+'''/Note-Data''',f)) ]
        onlyfiles.sort()
        for j in onlyfiles:
            listbox.insert('end',j[:-27])
    def OnDouble(self, event):
        widget = event.widget
        selection=widget.curselection()
        value = widget.get(selection[0])
        print "selection:", selection, ": '%s'" % value



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
        self.text.insert('1.0', 'my status here.\n')
        self.text.place(x=10, y=130)
        #work or house radiobutton
        self.tag_var = tk.StringVar()
        work = tk.Radiobutton(self, text='Work', variable=self.tag_var, value='works')
        house = tk.Radiobutton(self, text='House', variable=self.tag_var, value='house')
        work.place(x=200,y=420)
        house.place(x=200,y=440)
        #save button
        self.button = tk.Button(self, text="Save", command=self.save_note)
        self.button.place(x=260, y=395)
        self.list_m = ['1','2','3','4','5','6','7','8','9','10','11','12']
        self.dict = {'1':range(1,32), '2':range(1,30), '3':range(1,32),
                     '4':range(1,31), '5':range(1,32), '6':range(1,31),
                     '7':range(1,32), '8':range(1,32), '9':range(1,31),
                     '10':range(1,32), '11':range(1,31), '12':range(1,32)}
        self.year = range(2014, 2031)
        self.variable_a = tk.StringVar(self)
        self.variable_b = tk.StringVar(self)
        self.variable_c = tk.StringVar(self)
        self.variable_a.trace('w', self.update_b)
        self.optionmenu_a = tk.OptionMenu(self, self.variable_a, *self.list_m)
        self.optionmenu_b = tk.OptionMenu(self, self.variable_b, *self.dict['1'])
        self.optionmenu_c = tk.OptionMenu(self, self.variable_c, *self.year)
        self.variable_a.set('1')
        self.variable_b.set(1)
        self.variable_c.set(2014)
        self.optionmenu_a.place(x=10, y=390)
        self.optionmenu_b.place(x=70, y=390)
        self.optionmenu_c.place(x=130, y=390)
        self.pack()
        
    def save_note(self):
        date = str(datetime.datetime.now().date())
        title = self.text_title.get('1.0', 'end-1c')
        alert = str(self.variable_c.get())+'-'+str(self.variable_a.get()).zfill(2)+'-'+str(self.variable_b.get()).zfill(2)
        tag = [str(self.tag_var.get()),'works'][str(self.tag_var.get())=='']
        name = alert+" _ "+str(title)+' __ '+date+'   #'+tag
        data = self.text.get('1.0', 'end-1c')
        new_file = open("Note-Data/"+name+".txt", "w+")
        alert = str(self.variable_c.get())+'-'+str(self.variable_a.get())+'-'+str(self.variable_b.get())
        new_file.write(data)
        self.text.delete('1.0', 'end')
        self.text_title.delete('1.0', 'end')
        self.success = tk.Label(self, text='...File saved...')
        self.success.place(x=117, y=440)
    def update_b(self, *args):
        value_a = self.dict[self.variable_a.get()]
        self.optionmenu_b.pack_forget()
        self.optionmenu_b = tk.OptionMenu(self, self.variable_b, *value_a)
        self.variable_b.set(1)
        self.optionmenu_b.place(x=70, y=390)



class Work(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Workkkkkk!!!")
        label.pack(side="top", fill="x", pady=10)
        self.edge = tk.Label(self, text="========================================")
        self.edge.place(y = 400)
        self.workbutton = tk.Button(self, text="Work *-*)//", command=lambda: controller.show_frame(Work))
        self.workbutton.place(x=5, y=425)
        self.housebutton = tk.Button(self, text="House _(:3 JL)_", command=lambda: controller.show_frame(House))
        self.housebutton.place(x=80, y=425)
        self.introbutton = tk.Button(self, text="Back to Intro", command=lambda: controller.show_frame(StartPage))
        self.introbutton.place(x=5, y=465)
        self.newbutton = tk.Button(self, text="New", command=lambda: controller.show_frame(New))
        self.newbutton.place(x=5, y=500)
        self.aboutbutton = tk.Button(self, text="About", command=lambda: controller.show_frame(About))
        self.aboutbutton.place(x=5, y=535)
        frame = tk.Frame(self)
        frame.place(x=7,y=40)
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side='right', fill='y')
        listbox = tk.Listbox(frame,width=45, height=22)
        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox.yview)
        listbox.bind("<Double-Button-1>", self.OnDouble)
        listbox.pack(side="top", fill="both", expand=True)
        now = os.getcwd()
        onlyfiles = [ f for f in listdir(now+'''/Note-Data''') if isfile(join(now+'''/Note-Data''',f)) ]
        onlyfiles.sort()
        for j in onlyfiles:
            if '#works' in j:
                listbox.insert('end',j[:-27])
    def OnDouble(self, event):
        widget = event.widget
        selection=widget.curselection()
        value = widget.get(selection[0])
        print "selection:", selection, ": '%s'" % value


class House(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="House =3=")
        label.pack(side="top", fill="x", pady=10)
        self.edge = tk.Label(self, text="========================================")
        self.edge.place(y = 400)
        self.workbutton = tk.Button(self, text="Work *-*)//", command=lambda: controller.show_frame(Work))
        self.workbutton.place(x=5, y=425)
        self.housebutton = tk.Button(self, text="House _(:3 JL)_", command=lambda: controller.show_frame(House))
        self.housebutton.place(x=80, y=425)
        self.introbutton = tk.Button(self, text="Back to Intro", command=lambda: controller.show_frame(StartPage))
        self.introbutton.place(x=5, y=465)
        self.newbutton = tk.Button(self, text="New", command=lambda: controller.show_frame(New))
        self.newbutton.place(x=5, y=500)
        self.aboutbutton = tk.Button(self, text="About", command=lambda: controller.show_frame(About))
        self.aboutbutton.place(x=5, y=535)
        frame = tk.Frame(self)
        frame.place(x=7,y=40)
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side='right', fill='y')
        listbox = tk.Listbox(frame,width=45, height=22)
        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox.yview)
        listbox.bind("<Double-Button-1>", self.OnDouble)
        listbox.pack(side="top", fill="both", expand=True)
        now = os.getcwd()
        onlyfiles = [ f for f in listdir(now+'''/Note-Data''') if isfile(join(now+'''/Note-Data''',f)) ]
        onlyfiles.sort()
        for j in onlyfiles:
            if '#house' in j:
                listbox.insert('end',j[:-27])
    def OnDouble(self, event):
        widget = event.widget
        selection=widget.curselection()
        value = widget.get(selection[0])
        print "selection:", selection, ": '%s'" % value


if __name__ == "__main__":
    app = SampleApp()
    app.resizable(width='FALSE', height='FALSE')
    app.mainloop()
