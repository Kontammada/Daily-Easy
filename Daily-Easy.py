import Tkinter as tk
import tkMessageBox
import os
from os import listdir
from os.path import isfile, join
import datetime


class Edit(object):
    def __init__(self, find_note):
        self.now = os.getcwd()
        for file in os.listdir(self.now+"/Note-Data"):
            if file.startswith(find_note):
                edit_note = open(self.now+"/Note-Data/"+file, "r+")
                detail = edit_note.read()
                self.file = str(file)
        self.root = tk.Tk()
        self.root.geometry('300x600-10+50')
        label = tk.Label(self.root, text="Edit")
        label.place(x=130, y=30)
        main_button = tk.Button(self.root, text="Go to the main page")
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
        self.root.mainloop()
    def save_note(self):
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
            
    def update_b(self, *args):
        value_a = self.dict[self.variable_m.get()]
        self.optionmenu_d.pack_forget()
        self.optionmenu_d = tk.OptionMenu(self.root, self.variable_d, *value_a)
        self.variable_d.set(1)
        self.optionmenu_d.place(x=70, y=390)


Edit('2022-12-12 _ patopatohoho')
