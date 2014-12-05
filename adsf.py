from Tkinter import *
import tkFont


class Main_window(object):
    def __init__(self):
        pass
    def main(self):
        #Create Window
        gui = Tk()
        gui.geometry('300x600-10+50')
        gui.title('Daily Ealy')

        #Font size
        create_new_file_font_bold = tkFont.Font(size="15", weight="bold")
        create_new_file_font = tkFont.Font(size="15")

        #Creat new note
        create_new_button = Button(gui, text='New', font=create_new_file_font, bg='green', fg='black').place(x=240,y=555)

        gui.mainloop()



win = Main_window()
win.main()
