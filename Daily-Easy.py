import Tkinter as tk
import os
from os import listdir
from os.path import isfile, join
import datetime
import tkMessageBox
import tkFont
import random

class Start(object):
    '''intro window'''
    def __init__(self):
        '''create intro window'''
        self.root = tk.Tk()
        self.root.geometry('300x600-10+50')
        self.root.resizable(width='false', height='false')
        self.root.title('Daily Easy')
        to_main_img = tk.PhotoImage(file = "Image/Intro.gif")
        label = tk.Label
        label.image = to_main_img
        self.button = tk.Button(self.root, image = to_main_img, command=self.removethis)
        self.button.pack()
        self.root.mainloop()

    def check_note(self):
        '''ckeck note file and alert if find set time today'''
        now = os.getcwd()
        onlyfiles = [ f for f in listdir(now+'''/Note-Data''') if isfile(join(now+'''/Note-Data''',f)) ]
        for i in onlyfiles:
            if i[:10] == str(datetime.datetime.now().date()):
                tkMessageBox.showinfo(title='Today?', detail=i[13:-27])

    def removethis(self):
        '''destroy this window and call main window'''
        self.check_note()
        self.root.destroy()
        Main()


class Main(object):
    '''main window'''
    def __init__(self):
        '''creat main window'''
        self.root = tk.Tk()
        self.root.geometry('300x600-10+50')
        self.root.resizable(width='false', height='false')
        self.root.title('Daily Easy')
        self.bgimg = tk.PhotoImage(file="Image/mainbg.gif")
        #button
        self.labelbg = tk.Label(self.root, image = self.bgimg)
        self.workbutton = tk.Button(self.root, text="Main", font=tkFont.Font(size=13), state='disabled',relief='groove')
        self.workbutton.place(x=57, y=439)
        self.workbutton = tk.Button(self.root, text="Work", font=tkFont.Font(size=13), command=self.call_work,relief='groove')
        self.workbutton.place(x=119, y=439)
        self.housebutton = tk.Button(self.root, text="House", font=tkFont.Font(size=13), command=self.call_house,relief='groove')
        self.housebutton.place(x=185, y=439)
        self.newbutton = tk.Button(self.root, text="New", font=tkFont.Font(size=13), bg='#7CFC00', command=self.call_new,relief='groove')
        self.newbutton.place(x=250, y=558)
        self.introbutton = tk.Button(self.root, text="Help  About", command=self.call_about,relief='groove')
        self.introbutton.place(x=10, y=563)
        self.aboutbutton = tk.Button(self.root, text=" Intro ", command=self.call_intro,relief='groove')
        self.aboutbutton.place(x=95, y=563)
        #note view
        frame = tk.Frame(self.root)
        frame.place(x=7,y=63)
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side='right', fill='y')
        listbox = tk.Listbox(frame,width=33, height=20, font=tkFont.Font(size=11))
        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox.yview)
        listbox.bind("<Double-Button-1>", self.OnDouble)
        listbox.pack(side="top", fill="both", expand=True)
        #read file
        now = os.getcwd()
        onlyfiles = [ f for f in listdir(now+'''/Note-Data''') if isfile(join(now+'''/Note-Data''',f)) ]
        onlyfiles.sort()
        date = str(datetime.datetime.now().date())
        sum_date = int(date[:4])*10000+int(date[5:7])*100+int(date[8:10])
        #create list today
        cnt = 0
        for j in onlyfiles:
            if int(j[:4])*10000+int(j[5:7])*100+int(j[8:10]) == sum_date:
                listbox.insert('end',j[:-27])
                listbox.itemconfig(cnt, {'bg':'#99FF00'})
                cnt += 1
        #insert tip
        tip = open(now+'/tip.txt', 'r')
        self.tip_line = random.choice(tip.read().splitlines())
        listbox.insert('end', ['*'+self.tip_line, 'Tip: '+self.tip_line[:33]+'...'][len(self.tip_line)>35])
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
        #pack background
        self.labelbg.pack_propagate(0)
        self.labelbg.pack()

    def call_work(self):
        '''call work window'''
        self.root.destroy()
        Work()
    def call_house(self):
        '''call house window'''
        self.root.destroy()
        House()
    def call_intro(self):
        '''call start(intro) window'''
        self.root.destroy()
        Start()
    def call_new(self):
        '''call 'new' window'''
        self.root.destroy()
        New()
    def call_about(self):
        '''call about window'''
        self.root.destroy()
        About()

    def OnDouble(self, event):
        '''choose effect when double click item in listbox'''
        widget = event.widget
        selection=widget.curselection()
        value = widget.get(selection[0])
        if '=============' in value and '_' not in value:
            return
        if 'Tip: ' in value and '_' not in value:
            tkMessageBox.showinfo(title='Tip', detail=self.tip_line)
            return
        self.root.destroy()
        Edit(value)


class Work(object):
    '''work window'''
    def __init__(self):
        '''ceate work window'''
        self.root = tk.Tk()
        self.root.geometry('300x600-10+50')
        self.root.resizable(width='false', height='false')
        self.root.title('Daily Easy')
        self.bgimg = tk.PhotoImage(file="Image/workbg.gif")
        self.labelbg = tk.Label(self.root, image = self.bgimg)
        #button
        self.workbutton = tk.Button(self.root, text="Main", font=tkFont.Font(size=13), command=self.call_main,relief='groove')
        self.workbutton.place(x=57, y=439)
        self.workbutton = tk.Button(self.root, text="Work", font=tkFont.Font(size=13), state='disabled',relief='groove')
        self.workbutton.place(x=119, y=439)
        self.housebutton = tk.Button(self.root, text="House", font=tkFont.Font(size=13), command=self.call_house,relief='groove')
        self.housebutton.place(x=185, y=439)
        self.newbutton = tk.Button(self.root, text="New", font=tkFont.Font(size=13), bg='#7CFC00', command=self.call_new,relief='groove')
        self.newbutton.place(x=250, y=558)
        self.introbutton = tk.Button(self.root, text="Help  About", command=self.call_about,relief='groove')
        self.introbutton.place(x=10, y=563)
        self.aboutbutton = tk.Button(self.root, text=" Intro ", command=self.call_intro,relief='groove')
        self.aboutbutton.place(x=95, y=563)
        #note view
        frame = tk.Frame(self.root)
        frame.place(x=7,y=63)
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side='right', fill='y')
        listbox = tk.Listbox(frame,width=33, height=20, font=tkFont.Font(size=11))
        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox.yview)
        listbox.bind("<Double-Button-1>", self.OnDouble)
        listbox.pack(side="top", fill="both", expand=True)
        #read file
        now = os.getcwd()
        onlyfiles = [ f for f in listdir(now+'''/Note-Data''') if isfile(join(now+'''/Note-Data''',f)) ]
        onlyfiles.sort()
        date = str(datetime.datetime.now().date())
        sum_date = int(date[:4])*10000+int(date[5:7])*100+int(date[8:10])
        #create list today
        cnt = 0
        for j in onlyfiles:
            if int(j[:4])*10000+int(j[5:7])*100+int(j[8:10]) == sum_date and '#works' in j:
                listbox.insert('end',j[:-27])
                listbox.itemconfig(cnt, {'bg':'#99FF00'})
                cnt += 1
        #create list next time
        for j in onlyfiles:
            if '#works' in j:
                if int(j[:4])*10000+int(j[5:7])*100+int(j[8:10]) > sum_date:
                    listbox.insert('end',j[:-27])
        listbox.insert('end','===============================================')
        #create old list
        for k in onlyfiles:
            if '#works' in k:
                if int(k[:4])*10000+int(k[5:7])*100+int(k[8:10]) < sum_date:
                    listbox.insert('end',k[:-27])
        #pack background
        self.labelbg.pack_propagate(0)
        self.labelbg.pack()

    def call_main(self):
        '''call main window'''
        self.root.destroy()
        Main()
    def call_house(self):
        '''call house window'''
        self.root.destroy()
        House()
    def call_intro(self):
        '''call intro window'''
        self.root.destroy()
        Start()
    def call_new(self):
        '''call 'new' window'''
        self.root.destroy()
        New()
    def call_about(self):
        '''call about window'''
        self.root.destroy()
        About()

    def OnDouble(self, event):
        '''choose effect when double click item in listbox'''
        widget = event.widget
        selection=widget.curselection()
        value = widget.get(selection[0])
        if '=============' in value and '_' not in value:
            return
        self.root.destroy()
        Edit(value)


class House(object):
    '''house window'''
    def __init__(self):
        '''create house window'''
        self.root = tk.Tk()
        self.root.geometry('300x600-10+50')
        self.root.resizable(width='false', height='false')
        self.root.title('Daily Easy')
        self.bgimg = tk.PhotoImage(file="Image/housebg.gif")
        self.labelbg = tk.Label(self.root, image = self.bgimg)
        #button
        self.workbutton = tk.Button(self.root, text="Main", font=tkFont.Font(size=13), command=self.call_main,relief='groove')
        self.workbutton.place(x=57, y=439)
        self.workbutton = tk.Button(self.root, text="Work", font=tkFont.Font(size=13), command=self.call_work,relief='groove')
        self.workbutton.place(x=119, y=439)
        self.housebutton = tk.Button(self.root, text="House", font=tkFont.Font(size=13), state='disabled',relief='groove')
        self.housebutton.place(x=185, y=439)
        self.newbutton = tk.Button(self.root, text="New", font=tkFont.Font(size=13), bg='#7CFC00', command=self.call_new,relief='groove')
        self.newbutton.place(x=250, y=558)
        self.introbutton = tk.Button(self.root, text="Help  About", command=self.call_about,relief='groove')
        self.introbutton.place(x=10, y=563)
        self.aboutbutton = tk.Button(self.root, text=" Intro ", command=self.call_intro,relief='groove')
        self.aboutbutton.place(x=95, y=563)
        #note view
        frame = tk.Frame(self.root)
        frame.place(x=7,y=63)
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side='right', fill='y')
        listbox = tk.Listbox(frame,width=33, height=20, font=tkFont.Font(size=11))
        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox.yview)
        listbox.bind("<Double-Button-1>", self.OnDouble)
        listbox.pack(side="top", fill="both", expand=True)
        #read file
        now = os.getcwd()
        onlyfiles = [ f for f in listdir(now+'''/Note-Data''') if isfile(join(now+'''/Note-Data''',f)) ]
        onlyfiles.sort()
        date = str(datetime.datetime.now().date())
        sum_date = int(date[:4])*10000+int(date[5:7])*100+int(date[8:10])
        #create list today
        cnt = 0
        for j in onlyfiles:
            if int(j[:4])*10000+int(j[5:7])*100+int(j[8:10]) == sum_date and '#house' in j:
                listbox.insert('end',j[:-27])
                listbox.itemconfig(cnt, {'bg':'#99FF00'})
                cnt += 1
        #create list next time
        for j in onlyfiles:
            if '#house' in j:
                if int(j[:4])*10000+int(j[5:7])*100+int(j[8:10]) > sum_date:
                    listbox.insert('end',j[:-27])
        listbox.insert('end','===============================================')
        #create old list
        for k in onlyfiles:
            if '#house' in k:
                if int(k[:4])*10000+int(k[5:7])*100+int(k[8:10]) < sum_date:
                    listbox.insert('end',k[:-27])
        #pack background
        self.labelbg.pack_propagate(0)
        self.labelbg.pack()

    def call_main(self):
        '''call main window'''
        self.root.destroy()
        Main()
    def call_work(self):
        '''call work window'''
        self.root.destroy()
        Work()
    def call_intro(self):
        '''call intro window'''
        self.root.destroy()
        Start()
    def call_new(self):
        '''call 'new' window'''
        self.root.destroy()
        New()
    def call_about(self):
        '''callabout window'''
        self.root.destroy()
        About()

    def OnDouble(self, event):
        '''choose effect when double click item in listbox'''
        widget = event.widget
        selection=widget.curselection()
        value = widget.get(selection[0])
        if '=============' in value and '_' not in value:
            return
        self.root.destroy()
        Edit(value)


class New(object):
    '''new window'''
    def __init__(self):
        '''creat 'new' window'''
        self.root = tk.Tk()
        self.root.geometry('300x600-10+50')
        self.root.resizable(width='false', height='false')
        self.root.title('Daily Easy')
        self.bgimg = tk.PhotoImage(file="Image/newbg.gif")
        self.labelbg = tk.Label(self.root, image = self.bgimg)
        #go to the main page button
        main_button = tk.Button(self.root,command = self.call_main, text="Go to the main page",relief='groove')
        main_button.place(x=98, y=552)
        #textbox
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
        self.tag_var.set('works')
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
        #pack background
        self.labelbg.pack_propagate(0)
        self.labelbg.pack()

    def save_note(self):
        '''save note'''
        self.date = str(datetime.datetime.now().date())
        title = self.text_title.get('1.0', 'end-1c')
        alert = str(self.variable_y.get())+'-'+str(self.variable_m.get()).zfill(2)+'-'+str(self.variable_d.get()).zfill(2)
        tag = [str(self.tag_var.get()),'works'][str(self.tag_var.get())=='']
        name = alert+" _ "+str(title)+' __ '+self.date+'   #'+tag
        data = self.text.get('1.0', 'end-1c')
        if title == '':
            tkMessageBox.showinfo(title='_(:3 JL)_', detail="Please write title's name")
            return
        elif (('\\' in title or '/' in title) or (':' in title or '?' in title)) or (('"' in title or '<' in title) or ('>' in title or '|' in title)) or '*' in title:
            tkMessageBox.showinfo(title='_(:3 JL)_', detail="Please not use \\ / : ? "" < > | * in title")
            return
        new_file = open("Note-Data/"+name+".txt", "w+")
        alert = str(self.variable_y.get())+'-'+str(self.variable_m.get())+'-'+str(self.variable_d.get())
        new_file.write(data)
        self.text.delete('1.0', 'end')
        self.text_title.delete('1.0', 'end')
        self.call_main()

    def update_b(self, *args):
        '''update day optionmenu when change month'''
        self.optionmenu_d.destroy()
        value_a = self.dict[self.variable_m.get()]
        self.optionmenu_d.pack_forget()
        self.optionmenu_d = tk.OptionMenu(self.root, self.variable_d, *value_a)
        self.variable_d.set(1)
        self.optionmenu_d.place(x=160, y=410)

    def call_main(self):
        '''call main window'''
        self.root.destroy()
        Main()


class Edit(object):
    '''edit window'''
    def __init__(self, find_note):
        '''create edit window'''
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
        #go to the main page button
        main_button = tk.Button(self.root, text="Go to the main page", command=self.call_main,relief='groove')
        main_button.place(x=98, y=552)
        #textbox
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
        self.tag_var.set(str(self.file[-9:-4]))
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
        '''save note'''
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


    def delete_note(self):
        '''delete note'''
        root = tk.Tk()
        root.withdraw()
        if tkMessageBox.askyesno(title='Really?', detail='Do you want to delete?'):
            #delete file
            os.remove(self.now+'/Note-Data/'+self.file)
            self.call_main()

    def update_b(self, *args):
        '''update day optionmenu when change month'''
        self.optionmenu_d.destroy()
        value_a = self.dict[self.variable_m.get()]
        self.optionmenu_d.pack_forget()
        self.optionmenu_d = tk.OptionMenu(self.root, self.variable_d, *value_a)
        self.variable_d.set(1)
        self.optionmenu_d.place(x=160, y=410)

    def call_main(self):
        '''call main window'''
        self.root.destroy()
        Main()      


class About(object):
    '''about window'''
    def __init__(self):
        '''create about window'''
        self.root = tk.Tk()
        self.root.geometry('300x600-10+50')
        self.root.resizable(width='false', height='false')
        self.root.title('Daily Easy')
        to_main_img = tk.PhotoImage(file = "Image/Help.gif")
        label = tk.Label
        label.image = to_main_img
        self.button = tk.Button(self.root, image = to_main_img, command=self.removethis)
        self.button.pack()

    def removethis(self):
        '''call main window'''
        self.root.destroy()
        Main()


Start()
