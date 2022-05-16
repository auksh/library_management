from audioop import add
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from library_management.returnbook import tk_return
from utils import *
import views
import search
import addbook
import delbook
import issuebooks
import returnbook


def aaa():
    return

def admin_login():

    layout = tk_layout()

    _frame =  Frame(layout, bg="black",bd=5)
    _frame.place(relx=0.5, rely=0.5, relwidth=0.8, relheight=0.8,anchor=CENTER)


    Button(_frame, text='View Books', width=25, command=views.tk_view,font=('Courier',14)).place(relx=0.5, rely=0.1, anchor=CENTER)
    Button(_frame, text='Search Books', width=25, command=search.tk_search,font=('Courier',14)).place(relx=0.5, rely=0.2, anchor=CENTER)

    Button(_frame, text='Add Books', width=25, command=addbook.tk_addbook,font=('Courier',14)).place(relx=0.5, rely=0.4, anchor=CENTER)
    Button(_frame, text='Delete Books', width=25, command=delbook.tk_delete,font=('Courier',14)).place(relx=0.5, rely=0.5, anchor=CENTER)

    Button(_frame, text='Issue Books', width=25, command=issuebooks.tk_issue,font=('Courier',14)).place(relx=0.5, rely=0.7, anchor=CENTER)

    Button(_frame, text='Return Books', width=25, command=returnbook.tk_return,font=('Courier',14)).place(relx=0.5, rely=0.8, anchor=CENTER)



    layout.mainloop()



def user_login():

    layout = tk_layout()

    _frame =  Frame(layout, bg="black",bd=5)
    _frame.place(relx=0.5, rely=0.5, relwidth=0.8, relheight=0.8,anchor=CENTER)


    Button(_frame, text='View Books', width=25, command=views.tk_view,font=('Courier',14)).place(relx=0.5, rely=0.1, anchor=CENTER)
    Button(_frame, text='Search Books', width=25, command=search.tk_search,font=('Courier',14)).place(relx=0.5, rely=0.2, anchor=CENTER)

    Button(_frame, text='Return Books', width=25, command=returnbook.tk_return,font=('Courier',14)).place(relx=0.5, rely=0.8, anchor=CENTER)



    layout.mainloop()

