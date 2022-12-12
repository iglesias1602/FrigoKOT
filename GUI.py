from tkinter import *
from tkinter import ttk
from main import *


class EcranPrincipal:
    root = Tk()
    frm = ttk.Frame(root, padding=40)
    frm.grid()
    ttk.Label(frm, text="Product").grid(column=0, row=0)
    ttk.Button(frm, text="Add", command=root.destroy).grid(column=1, row=0)
    ttk.Label(frm, text="Etudiant").grid(column=0, row=1)
    ttk.Button(frm, text="Add", command=root.destroy).grid(column=1, row=1)
    root.mainloop()
