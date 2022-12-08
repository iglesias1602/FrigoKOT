import tkinter as tk
from tkinter import Menu
import tkinter.font as tkFont
import tkinter.messagebox
from tkcalendar import Calendar
from datetime import datetime
import main_test as mt

root = tk.Tk()

my_frigo = mt.Fridge('Frigo1')


class App(tk.Tk):

    def __init__(self, root):
        # setting title
        root.title("Frigo KOT")
        # setting window size
        width = 100
        height = 25
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 4, (screenheight - height) / 4)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        # Menu bar creation
        MenuBar = tk.Menu(root)
        ft = tkFont.Font(family='Arial', size=11)
        MenuBar['font'] = ft
        MenuBar['background'] = '#ff8000'
        MenuBar['foreground'] = 'black'
        MenuBar['activebackground'] = 'white'
        MenuBar['activeforeground'] = 'black'

        FileMenu = Menu(MenuBar)
        FileMenu['tearoff'] = '1'
        FileMenu['background'] = '#FFFFFF'
        FileMenu['foreground'] = 'black'
        FileMenu.add_command(label="New")
        FileMenu.add_command(label="Open")
        FileMenu.add_command(label="Save")
        FileMenu.add_command(label="Save as")
        FileMenu.add_separator()
        FileMenu.add_command(label="Exit", command=root.quit)
        MenuBar.add_cascade(label="File", menu=FileMenu)

        # View Menu bar
        ViewMenuBar = Menu(MenuBar, tearoff=0)
        ViewMenuBar.add_cascade(label='View', menu=ViewMenuBar)
        root.config(menu=MenuBar)

        # Help Menu bar option
        Help = Menu(MenuBar, tearoff=0)
        Help.add_command(label="About")
        MenuBar.add_cascade(label="Help", menu=help)

        # Product listbox, bg = 'white', listvariable = var, selectmode = tk.SINGLE
        GListBox_214 = tk.Listbox(root)
        GListBox_214["borderwidth"] = "1px"
        ft = tkFont.Font(family='Arial', size=11)
        GListBox_214["font"] = ft
        GListBox_214["fg"] = "#333333"
        GListBox_214["justify"] = "left"
        GListBox_214.place(x=30, y=60, width=172, height=310)
        GListBox_214["exportselection"] = "1"
        GListBox_214["selectmode"] = "SINGLE"
        GListBox_214["setgrid"] = "True"
        # GListBox_214["listvariable"] = var

        # Products shown
        GLabel_62 = tk.Label(root)
        GLabel_62["anchor"] = "center"
        GLabel_62["bg"] = "#dceddc"
        GLabel_62["cursor"] = "arrow"
        ft = tkFont.Font(family='Arial', size=11)
        GLabel_62["font"] = ft
        GLabel_62["fg"] = "#333333"
        GLabel_62["justify"] = "center"
        GLabel_62["text"] = "Products"
        # GLabel_62["relief"] = "raised"
        GLabel_62.place(x=30, y=30, width=171, height=30)

        # Students listbox
        GLineEdit_197 = tk.Entry(root)
        GLineEdit_197["borderwidth"] = "1px"
        ft = tkFont.Font(family='Arial', size=11)
        GLineEdit_197["font"] = ft
        GLineEdit_197["fg"] = "#333333"
        GLineEdit_197["justify"] = "center"
        GLineEdit_197["text"] = "Entry"
        GLineEdit_197.place(x=240, y=60, width=172, height=312)

        GLabel_158 = tk.Label(root)
        GLabel_158["bg"] = "#dceddc"
        ft = tkFont.Font(family='Arial', size=11)
        GLabel_158["font"] = ft
        GLabel_158["fg"] = "#393d49"
        GLabel_158["justify"] = "center"
        GLabel_158["text"] = "Students"
        GLabel_158.place(x=240, y=30, width=171, height=30)

        # Add Product
        GButton_181 = tk.Button(root)
        GButton_181["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Arial', size=11)
        GButton_181["font"] = ft
        GButton_181["fg"] = "#000000"
        GButton_181["justify"] = "center"
        GButton_181["text"] = "Add"
        GButton_181.place(x=40, y=390, width=70, height=25)
        GButton_181["command"] = self.GButton_181_command

        GButton_772 = tk.Button(root)
        GButton_772["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Arial', size=11)
        GButton_772["font"] = ft
        GButton_772["fg"] = "#000000"
        GButton_772["justify"] = "center"
        GButton_772["text"] = "Remove"
        GButton_772.place(x=120, y=390, width=70, height=25)
        GButton_772["command"] = self.GButton_772_command

        GButton_704 = tk.Button(root)
        GButton_704["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Arial', size=11)
        GButton_704["font"] = ft
        GButton_704["fg"] = "#000000"
        GButton_704["justify"] = "center"
        GButton_704["text"] = "View"
        GButton_704.place(x=80, y=430, width=70, height=25)
        GButton_704["command"] = self.GButton_704_command

        GButton_246 = tk.Button(root)
        GButton_246["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Arial', size=11)
        GButton_246["font"] = ft
        GButton_246["fg"] = "#000000"
        GButton_246["justify"] = "center"
        GButton_246["text"] = "Add"
        GButton_246.place(x=250, y=390, width=70, height=25)
        GButton_246["command"] = self.GButton_246_command

        # Add student button
        GButton_934 = tk.Button(root)
        GButton_934["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Arial', size=11)
        GButton_934["font"] = ft
        GButton_934["fg"] = "#000000"
        GButton_934["justify"] = "center"
        GButton_934["text"] = "Remove"
        GButton_934.place(x=330, y=390, width=70, height=25)
        GButton_934["command"] = self.GButton_934_command

        # Refresh Button
        GButton_161 = tk.Button(root)
        GButton_161["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Arial', size=11)
        GButton_161["font"] = ft
        GButton_161["fg"] = "#000000"
        GButton_161["justify"] = "center"
        GButton_161["text"] = "View"
        GButton_161.place(x=290, y=430, width=70, height=25)
        GButton_161["command"] = self.GButton_161_command

        # Recipes Output
        GLabel_158 = tk.Label(root)
        GLabel_158["bg"] = "#FFFFFF"
        ft = tkFont.Font(family='Arial', size=11)
        GLabel_158["font"] = ft
        GLabel_158["fg"] = "#393d49"
        GLabel_158["justify"] = "left"
        GLabel_158["anchor"] = "ne"
        GLabel_158[
            "text"] = "Ipsam repudiandae officia et non molestiae vero fugit.\n Sunt vitae in maiores. Eos magni odio quidem quia aliquid dolor.\n Sit provident minus fuga recusandae magnam sint. Qui hic debitis voluptatem ullam suscipit in et ab.\n Est eum praesentium animi quas voluptatem. " \
                      "Omnis fugit neque exercitationem soluta ipsum. Nulla et soluta est. Omnis reiciendis ipsum voluptates sunt rerum aliquam.\n" \
                      "Laboriosam consequatur tempora distinctio officia praesentium qui non. Aliquam nemo iste quod. Officia quis quo et fugit quo voluptas. Quisquam sint ut provident distinctio non.\n" \
                      "Rerum esse voluptas recusandae veniam et et. Nihil quis itaque delectus reiciendis laborum. \nQui tempore nostrum occaecati tempora beatae modi laudantium et. Omnis id quia consequatur non expedita qui pariatur.\n Ad et quas sunt sed dolor dolores autem commodi." \
                      "Amet sit voluptates vitae debitis laboriosam sunt. Deserunt quibusdam et aut. Neque labore omnis consequatur aspernatur natus esse."
        GLabel_158.place(x=450, y=60, width=360, height=311)

        GLabel_164 = tk.Label(root)
        GLabel_164["bg"] = "#dceddc"
        ft = tkFont.Font(family='Arial', size=11)
        GLabel_164["font"] = ft
        GLabel_164["fg"] = "#333333"
        GLabel_164["justify"] = "center"
        GLabel_164["text"] = "Recipes"
        GLabel_164.place(x=450, y=30, width=361, height=30)

        # Search Button
        GButton_949 = tk.Button(root)
        GButton_949["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Arial', size=11)
        GButton_949["font"] = ft
        GButton_949["fg"] = "#000000"
        GButton_949["justify"] = "center"
        GButton_949["text"] = "Search Recipe"
        GButton_949.place(x=680, y=380, width=121, height=30)
        GButton_949["command"] = self.GButton_949_command

    def newStudent(self):
        newStudent = tk.Toplevel(root)
        newStudent.geometry('200x100')
        newStudent.resizable(width=False, height=False)
        labelNewStudent = tk.Label(newStudent, text="New Window")
        buttonNewStudent = tk.Button(newStudent, text="New Window button")

        labelNewStudent.pack()
        buttonNewStudent.pack()

    def newProduct(self):
        list_type = ('Fruits', 'Vegetables', 'Seafood', 'Dairy', 'Mushrooms', 'Grains', 'Meat', 'Spices', 'Nuts',
                     'Sweets', 'Beverages', 'Baked Products', 'Fast Foods', 'Sauces')

        var = tk.Variable(value=list_type)

        today = datetime.now()

        # New window size definition
        newProduct = tk.Toplevel(root)
        newProduct.title('Add Product')
        newProduct.focus_force()
        newProduct.grab_set()
        # newProduct.geometry('520x330')

        # Position in screen
        width = 520
        height = 330
        screenwidth = newProduct.winfo_screenwidth()
        screenheight = newProduct.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        newProduct.geometry(alignstr)

        newProduct.resizable(width=False, height=False)
        # Labels
        productName = tk.Label(newProduct, text="Product name:")
        productType = tk.Label(newProduct, text="Type of product:")
        dateLabel = tk.Label(newProduct, text='Expiration date:')
        # Inputs and Options
        v = tk.StringVar()
        inputtext = tk.Entry(newProduct, bg='white', textvariable=v)
        listbox = tk.Listbox(newProduct, bg='white', listvariable=var, selectmode=tk.SINGLE)
        cal = Calendar(newProduct, selectmode='day', year=today.year, month=today.month, day=today.day)

        def listbox_command():
            table = []
            outputName = inputtext.get()
            outputType = ''
            outputCal = cal.selection_get()

            for i in listbox.curselection():
                outputType = listbox.get(i)

            # print(outputName, outputType, outputCal)
            if len(outputName) != 0 and len(outputType) != 0:
                my_frigo.add_item(outputName, outputType, outputCal)
            else:
                tk.messagebox.showinfo('Error', 'All the fields are required to add a product')

            # onClick(outputName)

            info = my_frigo.product_in_fridge
            print(info)

            for value in info:
                table.append(value['Product'])
                print(value['Product'])
                # var = tk.Variable(value=info)
                print(table)
                # var = tk.Variable(value)
            return table

        def onClick(output):
            """
                On click triggers a message
                :param output: Product name (outputName)
                :return: String text with product name
                 """
            tk.messagebox.showinfo('Added', f'{output} has been added.')

        # Buttons
        buttonNewProduct = tk.Button(newProduct, text="Add product", command=listbox_command, state='disabled')
        if not v.get():
            buttonNewProduct["state"] = "normal"
        # Pack elements

        productName.pack()  # Write product
        inputtext.pack()
        productType.pack()  # Choose type
        buttonNewProduct.pack()
        listbox.pack(expand=True, fill=tk.BOTH)
        cal.pack(pady=20)

        productName.place(x=20, y=15)
        inputtext.place(x=20, y=35, width=200, height=20)
        productType.place(x=20, y=60)
        listbox.place(x=20, y=85, height=227, width=200)
        dateLabel.place(x=250, y=15)
        cal.place(x=250, y=35)
        buttonNewProduct.place(x=275, y=250, width=200)

    def GCheckBox_160_command(self):
        print("command")

    def GButton_181_command(self):
        self.newProduct()
        #print("command")

    def GButton_772_command(self):
        print("command")

    def GButton_704_command(self):
        print("command")

    def GButton_246_command(self):
        print("command")

    def GButton_934_command(self):
        print("added")

    def GButton_161_command(self):
        print("command")

    def GButton_949_command(self):
        print("command")

    def GListBox_214_command(self):
        print('added')


def main():
    """
    Initialises the App class
    """
    App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
