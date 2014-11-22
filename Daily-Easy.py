from Tkinter import *
import tkFont



def create_new_file():
    '''open new window for choose type of new note'''
    new_file = Toplevel()
    new_file.geometry('200x200-65+200')
    new_file.title('Choose your type')
    new_file.focus_set()
    tell_user = Label(new_file, text='Please choose\n your type', font=create_new_file_font_bold).place(x=25, y=5)
    type_1 = Radiobutton(new_file, text='Regular', font=create_new_file_font, variable = 1).place(x=30, y=60)
    type_2 = Radiobutton(new_file, text='Work', font=create_new_file_font, variable = 1).place(x=30, y=90)
    type_3 = Radiobutton(new_file, text='three', font=create_new_file_font, variable = 1).place(x=30, y=120)
    type_4 = Radiobutton(new_file, text='four', font=create_new_file_font, variable = 1).place(x=30, y=150)



#Create Window

gui = Tk()
gui.geometry('300x600-10+50')
gui.title('Daily Ealy')



#Font size

create_new_file_font_bold = tkFont.Font(size="15", weight="bold")
create_new_file_font = tkFont.Font(size="15")



#Creat new note

create_new_button = Button(gui, text='New', font=30, bg='green', fg='black', command = create_new_file).place(x=240,y=555)



gui.mainloop()
