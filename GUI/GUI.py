import tkinter.messagebox
from tkinter import *

# Tk(screenName=None,  baseName=None,  className=’Tk’,  useTk=1)

win = tkinter.Tk()  # creating the main window and storing the window object in 'win'
# We create the widgetsL here
win.geometry('720x480')
win.configure(background='#F0F8FF')
win.title('Hello, I\'m the main window')
win.update()
win.minsize(win.winfo_width(), win.winfo_height())


# Top menu options
mn = Menu(win)
win.config(menu=mn)
file_menu = Menu(mn)
mn.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New')
file_menu.add_command(label='Open...')
file_menu.add_command(label='Save')
file_menu.add_separator()
file_menu.add_command(label='About')
file_menu.add_separator()
file_menu.add_command(label='Exit', command=win.quit)
help_menu = Menu(mn)
mn.add_cascade(label='Help', menu=help_menu)
help_menu.add_command(label='Feedback')
help_menu.add_command(label='Contact')

# Scrollbar options and list creation
# This is the section of code which creates the a label
Label(win, text='Products', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=20, y=10)

sb = Scrollbar(win)

list_1 = Listbox(win, yscrollcommand = sb.set ) # Listbox creation
sb.pack( side = RIGHT, fill = Y ) # Scrollbar position
for i in range(30): # Item insertion
    list_1.insert(END, 'Item ' + str(i))
list_1.pack( side = LEFT, fill = BOTH )
sb.config( command = list_1.yview )
list_1.place(y= 40, x=20)

win.mainloop()  # running the loop that works as a trigger
