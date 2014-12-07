import Tkinter as tk
import os
from os import listdir
from os.path import isfile, join
import datetime
import tkMessageBox
import tkFont
import random

class Start(object):
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('300x600-10+50')
        self.root.resizable(width='false', height='false')
        self.root.title('Daily Easy')
        to_main_img = tk.PhotoImage(file = "Image/frame.gif")
        label = tk.Label
        label.image = to_main_img
        self.button = tk.Button(self.root, image = to_main_img, command=self.removethis)
        self.button.pack()
        self.root.mainloop()
    def check_note(self):
        now = os.getcwd()
        onlyfiles = [ f for f in listdir(now+'''/Note-Data''') if isfile(join(now+'''/Note-Data''',f)) ]
        for i in onlyfiles:
            if i[:10] == str(datetime.datetime.now().date()):
                tkMessageBox.showinfo(title='Today?', detail=i[13:-27])
    def removethis(self):
        self.check_note()
        self.root.destroy()
        Main()
class Main(object):
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('300x600-10+50')
        self.root.resizable(width='false', height='false')
        self.root.title('Daily Easy')
        self.bgimg = tk.PhotoImage(file="Image/mainbg.gif")
        self.labelbg = tk.Label(self.root, image = self.bgimg)
        self.workbutton = tk.Button(self.root, text="Main", font=tkFont.Font(size=13), state='disabled',relief='groove')
        self.workbutton.place(x=57, y=439)
        self.workbutton = tk.Button(self.root, text="Work", font=tkFont.Font(size=13), command=self.call_work,relief='groove')
        self.workbutton.place(x=119, y=439)
        self.housebutton = tk.Button(self.root, text="House", font=tkFont.Font(size=13), command=self.call_house,relief='groove')
        self.housebutton.place(x=185, y=439)
        self.newbutton = tk.Button(self.root, text="New", font=tkFont.Font(size=13), bg='#7CFC00', command=self.call_new,relief='groove')
        self.newbutton.place(x=250, y=558)
        self.introbutton = tk.Button(self.root, text="Back to Intro", command=self.call_intro,relief='groove')
        self.introbutton.place(x=10, y=563)
        self.aboutbutton = tk.Button(self.root, text="About", command=self.call_about,relief='groove')
        self.aboutbutton.place(x=95, y=563)
        frame = tk.Frame(self.root)
        frame.place(x=7,y=63)
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side='right', fill='y')
        listbox = tk.Listbox(frame,width=33, height=20, font=tkFont.Font(size=11))
        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox.yview)
        listbox.bind("<Double-Button-1>", self.OnDouble)
        listbox.pack(side="top", fill="both", expand=True)
        now = os.getcwd()
        onlyfiles = [ f for f in listdir(now+'''/Note-Data''') if isfile(join(now+'''/Note-Data''',f)) ]
        onlyfiles.sort()
        date = str(datetime.datetime.now().date())
        sum_date = int(date[:4])*10000+int(date[5:7])*100+int(date[8:10])
        cnt = 0
        #create list today
        for j in onlyfiles:
            if int(j[:4])*10000+int(j[5:7])*100+int(j[8:10]) == sum_date:
                listbox.insert('end',j[:-27])
                listbox.itemconfig(cnt, {'bg':'#99FF00'})
                cnt += 1
        #insert tip
        tip = open(now+'/tip.txt', 'r')
        self.tip_line = random.choice(tip.read().splitlines())
        listbox.insert('end', ['*'+self.tip_line, '**'+self.tip_line[:35]+'...'][len(self.tip_line)>35])
        listbox.itemconfig(cnt, {'bg':'#FFFF99'})
        #create list next time
        for j in onlyfiles:
            if int(j[:4])*10000+int(j[5:7])*100+int(j[8:10]) > sum_date:
                listbox.insert('end',j[:-27])
        listbox.insert('end','===============================================')
        #create old list
        for k in onlyfiles:
            if int(k[:4])*10000+int(k[5:7])*100+int(k[8:10]) < sum_date:
                listbox.insert('end',k[:-27])
        self.labelbg.pack_propagate(0)
        self.labelbg.pack()
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
        About()
    def OnDouble(self, event):
        widget = event.widget
        selection=widget.curselection()
        value = widget.get(selection[0])
        if '=============' in value:
            return
        if '**' in value:
            tkMessageBox.showinfo(title='Tip', detail=self.tip_line)
            return
        self.root.destroy()
        Edit(value)
class New(object):
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('300x600-10+50')
        self.root.resizable(width='false', height='false')
        self.root.title('Daily Easy')
        self.bgimg = tk.PhotoImage(file="Image/newbg.gif")
        self.labelbg = tk.Label(self.root, image = self.bgimg)
        main_button = tk.Button(self.root,command = self.call_main, text="Go to the main page",relief='groove')
        main_button.place(x=98, y=552)
        self.text_title = tk.Text(self.root)
        self.text_title.config(width=34, heigh=1)
        self.text_title.place(x=10, y=73)
        self.text = tk.Text(self.root)
        self.text.config(width=34, heigh=17)
        self.text.place(x=10, y=122)
        #work or house radiobutton
        self.tag_var = tk.StringVar()
        work = tk.Radiobutton(self.root, text='Works', variable=self.tag_var, value='works')
        house = tk.Radiobutton(self.root, text='House', variable=self.tag_var, value='house')
        work.place(x=165,y=455)
        house.place(x=165,y=473)
        #save button
        self.button = tk.Button(self.root, text="Save", font=tkFont.Font(size=13), bg='#7CFC00', command=self.save_note,relief='groove')
        self.button.place(x=240, y=460)
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
        self.date = str(datetime.datetime.now().date())
        self.variable_m.set(self.date[5:7])
        self.variable_d.set(self.date[8:10])
        self.variable_y.set(self.date[:4])
        self.optionmenu_m.place(x=103, y=409)
        self.optionmenu_d.place(x=163, y=409)
        self.optionmenu_y.place(x=223, y=409)
        self.labelbg.pack_propagate(0)
        self.labelbg.pack()
    def save_note(self):
        self.date = str(datetime.datetime.now().date())
        title = self.text_title.get('1.0', 'end-1c')
        alert = str(self.variable_y.get())+'-'+str(self.variable_m.get()).zfill(2)+'-'+str(self.variable_d.get()).zfill(2)
        tag = [str(self.tag_var.get()),'works'][str(self.tag_var.get())=='']
        name = alert+" _ "+str(title)+' __ '+self.date+'   #'+tag
        data = self.text.get('1.0', 'end-1c')
        if title == '':
            return
        new_file = open("Note-Data/"+name+".txt", "w+")
        alert = str(self.variable_y.get())+'-'+str(self.variable_m.get())+'-'+str(self.variable_d.get())
        new_file.write(data)
        self.text.delete('1.0', 'end')
        self.text_title.delete('1.0', 'end')
        self.call_main()
    def update_b(self, *args):
        value_a = self.dict[self.variable_m.get()]
        self.optionmenu_d.pack_forget()
        self.optionmenu_d = tk.OptionMenu(self.root, self.variable_d, *value_a)
        self.variable_d.set(1)
        self.optionmenu_d.place(x=160, y=410)
    def call_main(self):
        self.root.destroy()
        Main()
class Edit(object):
    def __init__(self, find_note):
        self.root = tk.Tk()
        self.root.geometry('300x600-10+50')
        self.bgimg = tk.PhotoImage(file="Image/Editbg.gif")
        self.root.title('Daily Easy')
        self.labelbg = tk.Label(self.root, image = self.bgimg)
        self.root.resizable(width='false', height='false')
        self.now = os.getcwd()
        for file in os.listdir(self.now+"/Note-Data"):
            if file.startswith(find_note):
                edit_note = open(self.now+"/Note-Data/"+file, "r+")
                detail = edit_note.read()
                self.file = str(file)
        main_button = tk.Button(self.root, text="Go to the main page", command=self.call_main,relief='groove')
        main_button.place(x=98, y=552)
        self.text_title = tk.Text(self.root)
        self.text_title.config(width=34, heigh=1)
        self.text_title.place(x=10, y=73)
        self.text_title.insert('1.0', self.file[13:-27])
        self.text = tk.Text(self.root)
        self.text.config(width=34, heigh=17)
        self.text.place(x=10, y=122)
        self.text.insert('1.0', detail)
        #work or house radiobutton
        self.tag_var = tk.StringVar()
        work = tk.Radiobutton(self.root, text='Works', variable=self.tag_var, value='works')
        house = tk.Radiobutton(self.root, text='House', variable=self.tag_var, value='house')
        work.place(x=165,y=455)
        house.place(x=165,y=473)
        #save button
        self.button = tk.Button(self.root, text="Save", font=tkFont.Font(size=13), bg='#7CFC00', command=self.save_note,relief='groove')
        self.button.place(x=240, y=460)
        #delete button
        self.delete_button = tk.Button(self.root, text='delete', bg='#FF0000',command=self.delete_note,relief='groove')
        self.delete_button.place(x=10, y=412)
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
        self.optionmenu_m.place(x=103, y=409)
        self.optionmenu_d.place(x=163, y=409)
        self.optionmenu_y.place(x=223, y=409)
        self.labelbg.pack_propagate(0)
        self.labelbg.pack()
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
            self.call_main()
    def call_main(self):
        self.root.destroy()
        Main()
    def delete_note(self):
        root = tk.Tk()
        root.withdraw()
        if tkMessageBox.askyesno(title='Really?', detail='Do you want to delete?'):
            #delete file
            os.remove(self.now+'/Note-Data/'+self.file)
            self.call_main()
    def update_b(self, *args):
        value_a = self.dict[self.variable_m.get()]
        self.optionmenu_d.pack_forget()
        self.optionmenu_d = tk.OptionMenu(self.root, self.variable_d, *value_a)
        self.variable_d.set(1)
        self.optionmenu_d.place(x=160, y=410)
    def call_main(self):
        self.root.destroy()
        Main()        

        
class Work(object):
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('300x600-10+50')
        self.root.resizable(width='false', height='false')
        self.root.title('Daily Easy')
        self.bgimg = tk.PhotoImage(file="Image/workbg.gif")
        self.labelbg = tk.Label(self.root, image = self.bgimg)
        self.workbutton = tk.Button(self.root, text="Main", font=tkFont.Font(size=13), command=self.call_main,relief='groove')
        self.workbutton.place(x=57, y=439)
        self.workbutton = tk.Button(self.root, text="Work", font=tkFont.Font(size=13), state='disabled',relief='groove')
        self.workbutton.place(x=119, y=439)
        self.housebutton = tk.Button(self.root, text="House", font=tkFont.Font(size=13), command=self.call_house,relief='groove')
        self.housebutton.place(x=185, y=439)
        self.newbutton = tk.Button(self.root, text="New", font=tkFont.Font(size=13), bg='#7CFC00', command=self.call_new,relief='groove')
        self.newbutton.place(x=250, y=558)
        self.introbutton = tk.Button(self.root, text="Back to Intro", command=self.call_intro,relief='groove')
        self.introbutton.place(x=10, y=563)
        self.aboutbutton = tk.Button(self.root, text="About", command=self.call_about,relief='groove')
        self.aboutbutton.place(x=95, y=563)
        frame = tk.Frame(self.root)
        frame.place(x=7,y=63)
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side='right', fill='y')
        listbox = tk.Listbox(frame,width=33, height=20, font=tkFont.Font(size=11))
        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox.yview)
        listbox.bind("<Double-Button-1>", self.OnDouble)
        listbox.pack(side="top", fill="both", expand=True)
        now = os.getcwd()
        onlyfiles = [ f for f in listdir(now+'''/Note-Data''') if isfile(join(now+'''/Note-Data''',f)) ]
        onlyfiles.sort()
        date = str(datetime.datetime.now().date())
        sum_date = int(date[:4])*10000+int(date[5:7])*100+int(date[8:10])
        cnt = 0
        #create list today
        for j in onlyfiles:
            if int(j[:4])*10000+int(j[5:7])*100+int(j[8:10]) == sum_date and '#works' in j:
                listbox.insert('end',j[:-27])
                listbox.itemconfig(cnt, {'bg':'#99FF00'})
                cnt += 1
        for j in onlyfiles:
            if '#works' in j:
                if int(j[:4])*10000+int(j[5:7])*100+int(j[8:10]) > sum_date:
                    listbox.insert('end',j[:-27])
        listbox.insert('end','===============================================')
        for k in onlyfiles:
            if '#works' in k:
                if int(k[:4])*10000+int(k[5:7])*100+int(k[8:10]) < sum_date:
                    listbox.insert('end',k[:-27])
        self.labelbg.pack_propagate(0)
        self.labelbg.pack()
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
        About()
    def OnDouble(self, event):
        widget = event.widget
        selection=widget.curselection()
        value = widget.get(selection[0])
        if '=============' in value:
            return
        self.root.destroy()
        Edit(value)


class House(object):
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('300x600-10+50')
        self.root.resizable(width='false', height='false')
        self.root.title('Daily Easy')
        self.bgimg = tk.PhotoImage(file="Image/housebg.gif")
        self.labelbg = tk.Label(self.root, image = self.bgimg)
        self.workbutton = tk.Button(self.root, text="Main", font=tkFont.Font(size=13), command=self.call_main,relief='groove')
        self.workbutton.place(x=57, y=439)
        self.workbutton = tk.Button(self.root, text="Work", font=tkFont.Font(size=13), command=self.call_work,relief='groove')
        self.workbutton.place(x=119, y=439)
        self.housebutton = tk.Button(self.root, text="House", font=tkFont.Font(size=13), state='disabled',relief='groove')
        self.housebutton.place(x=185, y=439)
        self.newbutton = tk.Button(self.root, text="New", font=tkFont.Font(size=13), bg='#7CFC00', command=self.call_new,relief='groove')
        self.newbutton.place(x=250, y=558)
        self.introbutton = tk.Button(self.root, text="Back to Intro", command=self.call_intro,relief='groove')
        self.introbutton.place(x=10, y=563)
        self.aboutbutton = tk.Button(self.root, text="About", command=self.call_about,relief='groove')
        self.aboutbutton.place(x=95, y=563)
        frame = tk.Frame(self.root)
        frame.place(x=7,y=63)
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side='right', fill='y')
        listbox = tk.Listbox(frame,width=33, height=20, font=tkFont.Font(size=11))
        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox.yview)
        listbox.bind("<Double-Button-1>", self.OnDouble)
        listbox.pack(side="top", fill="both", expand=True)
        now = os.getcwd()
        onlyfiles = [ f for f in listdir(now+'''/Note-Data''') if isfile(join(now+'''/Note-Data''',f)) ]
        onlyfiles.sort()
        date = str(datetime.datetime.now().date())
        sum_date = int(date[:4])*10000+int(date[5:7])*100+int(date[8:10])
        cnt = 0
        #create list today
        for j in onlyfiles:
            if int(j[:4])*10000+int(j[5:7])*100+int(j[8:10]) == sum_date and '#house' in j:
                listbox.insert('end',j[:-27])
                listbox.itemconfig(cnt, {'bg':'#99FF00'})
                cnt += 1
        for j in onlyfiles:
            if '#house' in j:
                if int(j[:4])*10000+int(j[5:7])*100+int(j[8:10]) > sum_date:
                    listbox.insert('end',j[:-27])
        listbox.insert('end','===============================================')
        for k in onlyfiles:
            if '#house' in k:
                if int(k[:4])*10000+int(k[5:7])*100+int(k[8:10]) < sum_date:
                    listbox.insert('end',k[:-27])
        self.labelbg.pack_propagate(0)
        self.labelbg.pack()
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
        About()
    def OnDouble(self, event):
        widget = event.widget
        selection=widget.curselection()
        value = widget.get(selection[0])
        if '=============' in value:
            return
        self.root.destroy()
        Edit(value)

class About(object):
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('300x150-10+300')
        self.root.resizable(width='false', height='false')
        self.root.title('About: Daily Easy')
        label = tk.Label(self.root, text="Pachara Chaicharoen 57070075")
        label.pack(side="top", fill="x", pady=10)
        label = tk.Label(self.root, text="Suttinai Bunyingyonchai 57070134")
        label.pack(side="top", fill="x", pady=10)
        label = tk.Label(self.root, text="Language: Python")
        label.pack(side="top", fill="x", pady=10)



Start()
