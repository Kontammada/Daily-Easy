import Tkinter as tk
import os
from os import listdir
from os.path import isfile, join
import datetime
import tkMessageBox

class Start(object):
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('300x600-10+50')
        to_main_img = tk.PhotoImage(file = "frame.gif")
        label = tk.Label
        label.image = to_main_img
        self.button = tk.Button(self.root, image = to_main_img, command=self.removethis)
        self.button.pack()
        self.root.mainloop()
    def removethis(self):
        self.root.destroy()
        Main()
        
class Main(object):
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('300x600-10+50')
        label = tk.Label(self.root, text="main _/|\_")
        label.pack(side="top", fill="x", pady=10)
        self.edge = tk.Label(self.root, text="========================================")
        self.edge.place(y = 400)
        self.workbutton = tk.Button(self.root, text="Work *-*)//", command=self.call_work,relief='groove')
        self.workbutton.place(x=5, y=425)
        self.housebutton = tk.Button(self.root, text="House _(:3 JL)_", command=self.call_house,relief='groove')
        self.housebutton.place(x=80, y=425)
        self.introbutton = tk.Button(self.root, text="Back to Intro", command=self.call_intro,relief='groove')
        self.introbutton.place(x=5, y=465)
        self.newbutton = tk.Button(self.root, text="New", command=self.call_new,relief='groove')
        self.newbutton.place(x=5, y=500)
        self.aboutbutton = tk.Button(self.root, text="About", command=self.call_about,relief='groove')
        self.aboutbutton.place(x=5, y=535)
        frame = tk.Frame(self.root)
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
        date = str(datetime.datetime.now().date())
        sum_date = int(date[:4])*10000+int(date[5:7])*100+int(date[8:10])
        for j in onlyfiles:
            if int(j[:4])*10000+int(j[5:7])*100+int(j[8:10]) >= sum_date:
                listbox.insert('end',j[:-27])
        listbox.insert('end','===============================================')
        for k in onlyfiles:
            if int(k[:4])*10000+int(k[5:7])*100+int(k[8:10]) < sum_date:
                listbox.insert('end',k[:-27])
    def call_work(self):
        self.root.destroy()
        Work()
    def call_house(self):
        self.root.destroy()
        House()
    def call_intro(self):
        self.root.destroy()
        Start()
    def call_new(self):
        self.root.destroy()
        New()
    def call_about(self):
        self.root.destroy()
        About()
    def OnDouble(self, event):
        widget = event.widget
        selection=widget.curselection()
        value = widget.get(selection[0])
        print "selection:", selection, ": '%s'" % value
        Edit(value)
        self.root.destroy()
class New(object):
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('300x600-10+50')
        label = tk.Label(self.root, text="New =w=")
        label.place(x=130, y=30)
        main_button = tk.Button(self.root,command = self.call_main, text="Go to the main page",relief='groove')
        main_button.place(x=95, y=550)
        self.title = tk.Label(self.root, text='Title')
        self.title.place(x=10, y=60)
        self.description = tk.Label(self.root, text='Description')
        self.description.place(x=10, y=110)
        self.text_title = tk.Text(self.root)
        self.text_title.config(width=35, heigh=1)
        self.text_title.place(x=10, y=80)
        self.text = tk.Text(self.root)
        self.text.config(width=35, heigh=15)
        self.text.place(x=10, y=130)
        #work or house radiobutton
        self.tag_var = tk.StringVar()
        work = tk.Radiobutton(self.root, text='Work', variable=self.tag_var, value='works')
        house = tk.Radiobutton(self.root, text='House', variable=self.tag_var, value='house')
        work.place(x=200,y=420)
        house.place(x=200,y=440)
        #save button
        self.button = tk.Button(self.root, text="Save", command=self.save_note)
        self.button.place(x=260, y=395)
        #date optionmenu
        self.list_m = ['1','2','3','4','5','6','7','8','9','10','11','12']
        self.dict = {'1':range(1,32), '2':range(1,30), '3':range(1,32),
                     '4':range(1,31), '5':range(1,32), '6':range(1,31),
                     '7':range(1,32), '8':range(1,32), '9':range(1,31),
                     '10':range(1,32), '11':range(1,31), '12':range(1,32)}
        self.year = range(2014, 2031)
        self.variable_a = tk.StringVar(self.root)
        self.variable_b = tk.StringVar(self.root)
        self.variable_c = tk.StringVar(self.root)
        self.variable_a.trace('w', self.update_b)
        self.optionmenu_a = tk.OptionMenu(self.root, self.variable_a, *self.list_m)
        self.optionmenu_b = tk.OptionMenu(self.root, self.variable_b, *self.dict['1'])
        self.optionmenu_c = tk.OptionMenu(self.root, self.variable_c, *self.year)
        self.variable_a.set('1')
        self.variable_b.set(1)
        self.variable_c.set(2014)
        self.optionmenu_a.place(x=10, y=390)
        self.optionmenu_b.place(x=70, y=390)
        self.optionmenu_c.place(x=130, y=390)
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
        self.success = tk.Label(self.root, text='...File saved...')
        self.success.place(x=117, y=440)
    def update_b(self, *args):
        value_a = self.dict[self.variable_a.get()]
        self.optionmenu_b.pack_forget()
        self.optionmenu_b = tk.OptionMenu(self.root, self.variable_b, *value_a)
        self.variable_b.set(1)
        self.optionmenu_b.place(x=70, y=390)
    def call_main(self):
        self.root.destroy()
        Main()
class Edit(object):
    def __init__(self, find_note):
        self.root = tk.Tk()
        self.root.geometry('300x600-10+50')
        self.now = os.getcwd()
        for file in os.listdir(self.now+"/Note-Data"):
            if file.startswith(find_note):
                edit_note = open(self.now+"/Note-Data/"+file, "r+")
                detail = edit_note.read()
                self.file = str(file)

        label = tk.Label(self.root, text="Edit")
        label.place(x=130, y=30)
        main_button = tk.Button(self.root, text="Go to the main page", command=self.call_main)
        main_button.place(x=95, y=550)
        self.title = tk.Label(self.root, text='Title')
        self.title.place(x=10, y=60)
        self.description = tk.Label(self.root, text='Description')
        self.description.place(x=10, y=110)
        self.text_title = tk.Text(self.root)
        self.text_title.config(width=35, heigh=1)
        self.text_title.place(x=10, y=80)
        self.text_title.insert('1.0', self.file[13:-27])
        self.text = tk.Text(self.root)
        self.text.config(width=35, heigh=15)
        self.text.place(x=10, y=130)
        self.text.insert('1.0', detail)
        #work or house radiobutton
        self.tag_var = tk.StringVar(self.root)
        work = tk.Radiobutton(self.root, text='Work', variable=self.tag_var, value='works')
        house = tk.Radiobutton(self.root, text='House', variable=self.tag_var, value='house')
        work.place(x=200,y=420)
        house.place(x=200,y=440)
        #save button
        self.button = tk.Button(self.root, text="Save", command=self.save_note)
        self.button.place(x=260, y=395)
        #delete button
        self.delete_button = tk.Button(self.root, text='delete',command=self.delete_note)
        self.delete_button.place(x=260, y=410)
        #date optionmenu
        self.list_m = ['1','2','3','4','5','6','7','8','9','10','11','12']
        self.dict = {'1':range(1,32), '2':range(1,30), '3':range(1,32),
                     '4':range(1,31), '5':range(1,32), '6':range(1,31),
                     '7':range(1,32), '8':range(1,32), '9':range(1,31),
                     '10':range(1,32), '11':range(1,31), '12':range(1,32)}
        self.year = range(2014, 2031)
        self.variable_m = tk.StringVar(self.root)
        self.variable_d = tk.StringVar(self.root)
        self.variable_y = tk.StringVar(self.root)
        self.variable_m.trace('w', self.update_b)
        self.optionmenu_m = tk.OptionMenu(self.root, self.variable_m, *self.list_m)
        self.optionmenu_d = tk.OptionMenu(self.root, self.variable_d, *self.dict['1'])
        self.optionmenu_y = tk.OptionMenu(self.root, self.variable_y, *self.year)
        self.variable_m.set(int(self.file[5:7]))
        self.variable_d.set(int(self.file[8:10]))
        self.variable_y.set(int(self.file[:4]))
        self.optionmenu_m.place(x=10, y=390)
        self.optionmenu_d.place(x=70, y=390)
        self.optionmenu_y.place(x=130, y=390)
    def save_note(self):
        root = tk.Tk()
        root.withdraw()
        if tkMessageBox.askyesno(title='Really?', detail='Do you want to save?'):
            #delete old file
            os.remove(self.now+'/Note-Data/'+self.file)
            #create new file
            date = str(datetime.datetime.now().date())
            title = self.text_title.get('1.0', 'end-1c')
            alert = str(self.variable_y.get())+'-'+str(self.variable_m.get()).zfill(2)+'-'+str(self.variable_d.get()).zfill(2)
            tag = [str(self.tag_var.get()), self.file[-9:-4]][self.tag_var.get() == '']
            name = alert+" _ "+str(title)+' __ '+date+'   #'+tag
            data = self.text.get('1.0', 'end-1c')
            new_file = open("Note-Data/"+name+".txt", "w+")
            alert = str(self.variable_y.get())+'-'+str(self.variable_m.get())+'-'+str(self.variable_d.get())
            new_file.write(data)
            self.text.delete('1.0', 'end')
            self.text_title.delete('1.0', 'end')
            self.success = tk.Label(self.root, text='...File saved...')
            self.success.place(x=117, y=440)
<<<<<<< HEAD
            self.root.destroy()
            Main()
    def call_main(self):
        self.root.destroy()
        Main()
=======
    def delete_note(self):
        root = tk.Tk()
        root.withdraw()
        if tkMessageBox.askyesno(title='Really?', detail='Do you want to remove?'):
            #delete file
            os.remove(self.now+'/Note-Data/'+self.file)
            call_nain()
>>>>>>> origin/master
            
    def update_b(self, *args):
        value_a = self.dict[self.variable_m.get()]
        self.optionmenu_d.pack_forget()
        self.optionmenu_d = tk.OptionMenu(self.root, self.variable_d, *value_a)
        self.variable_d.set(1)
        self.optionmenu_d.place(x=70, y=390)
    def call_main(self):
        self.root.destroy()
        Main()

        
class Work(object):
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('300x600-10+50')
        label = tk.Label(self.root, text="Workkkkkk!!!")
        label.pack(side="top", fill="x", pady=10)
        self.edge = tk.Label(self.root, text="========================================")
        self.edge.place(y = 400)
        self.workbutton = tk.Button(self.root, text="Main", command=self.call_main,relief='groove')
        self.workbutton.place(x=5, y=425)
        self.housebutton = tk.Button(self.root, text="House _(:3 JL)_", command=self.call_house,relief='groove')
        self.housebutton.place(x=80, y=425)
        self.introbutton = tk.Button(self.root, text="Back to Intro", command=self.call_intro,relief='groove')
        self.introbutton.place(x=5, y=465)
        self.newbutton = tk.Button(self.root, text="New", command=self.call_new,relief='groove')
        self.newbutton.place(x=5, y=500)
        self.aboutbutton = tk.Button(self.root, text="About", command=self.call_about,relief='groove')
        self.aboutbutton.place(x=5, y=535)
        frame = tk.Frame(self.root)
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

    def call_main(self):
        self.root.destroy()
        Main()
    def call_house(self):
        self.root.destroy()
        House()
    def call_intro(self):
        self.root.destroy()
        Start()
    def call_new(self):
        self.root.destroy()
        New()
    def call_about(self):
        self.root.destroy()
        About()
    def OnDouble(self, event):
        widget = event.widget
        selection=widget.curselection()
        value = widget.get(selection[0])
        print "selection:", selection, ": '%s'" % value
        Edit(value)
        self.root.destroy()

class House(object):
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('300x600-10+50')
        label = tk.Label(self.root, text="House =3=")
        label.pack(side="top", fill="x", pady=10)
        self.edge = tk.Label(self.root, text="========================================")
        self.edge.place(y = 400)
        self.workbutton = tk.Button(self.root, text="Main", command=self.call_main,relief='groove')
        self.workbutton.place(x=5, y=425)
        self.housebutton = tk.Button(self.root, text="Work *-*)//", command=self.call_work,relief='groove')
        self.housebutton.place(x=80, y=425)
        self.introbutton = tk.Button(self.root, text="Back to Intro", command=self.call_intro,relief='groove')
        self.introbutton.place(x=5, y=465)
        self.newbutton = tk.Button(self.root, text="New", command=self.call_new,relief='groove')
        self.newbutton.place(x=5, y=500)
        self.aboutbutton = tk.Button(self.root, text="About", command=self.call_about,relief='groove')
        self.aboutbutton.place(x=5, y=535)
        frame = tk.Frame(self.root)
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

    def call_main(self):
        self.root.destroy()
        Main()
    def call_work(self):
        self.root.destroy()
        Work()
    def call_intro(self):
        self.root.destroy()
        Start()
    def call_new(self):
        self.root.destroy()
        New()
    def call_about(self):
        self.root.destroy()
        About()
    def OnDouble(self, event):
        widget = event.widget
        selection=widget.curselection()
        value = widget.get(selection[0])
        print "selection:", selection, ": '%s'" % value
        Edit(value)
        self.root.destroy()
class About(object):
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('300x600-10+50')

Start()
