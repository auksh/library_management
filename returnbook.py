from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import utils


def return_book(bookID):

    # Check if bookID exists
    if utils.bookID_exists(bookID):
        utils.return_bookdb(bookID)
        messagebox.showinfo("Returned","Book Returned")
        layout.destroy
    
    else:
        messagebox.showerror("Error","Book ID doesn't exists")
        layout.destroy 
    return
    

def tk_return():
    
    global layout

    layout = utils.tk_layout("Return Books")

    _frame =  Frame(layout, bg="black",bd=5)
    _frame.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.3,anchor=N)

    Label(_frame, text='Book ID : ',fg="white",bg="black",font=('Courier',14)).place(relx=0.05, rely=0.1)

    _bookID = Entry(_frame)
    _bookID.place(relx=0.25, rely=0.1)



    Button(_frame, text='Return', width=20, command=lambda: return_book(int(_bookID.get())),font=('Courier',14)).place(anchor=CENTER,relx=0.5,rely=0.75)

    Button(_frame, text='Close', width=15, command=layout.destroy,font=('Courier',14)).place(relx=1, rely=0.3, anchor=E)

    layout.mainloop()

