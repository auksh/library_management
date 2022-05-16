from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import utils


def issue_book(bookID,emailID):

    # Check if bookID exists
    if utils.bookID_exists(bookID) and utils.studentEmail_exists(emailID):
        utils.issueBook_to_user(bookID,emailID)
        messagebox.showinfo("Issued","Book Issued to USER")
        layout.destroy
    
    else:
        messagebox.showerror("Error","Book ID or User Email not exists")
        layout.destroy 
    return
    

def tk_issue():
    
    global layout

    layout = utils.tk_layout()

    _frame =  Frame(layout, bg="black",bd=5)
    _frame.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.3,anchor=N)

    Label(_frame, text='Book ID : ',fg="white",bg="black",font=('Courier',14)).place(relx=0.05, rely=0.1)

    _bookID = Entry(_frame)
    _bookID.place(relx=0.25, rely=0.1)


    Label(_frame, text='Student Email : ',fg="white",bg="black",font=('Courier',14)).place(relx=0.05, rely=0.3)

    _studentEmail = Entry(_frame)
    _studentEmail.place(relx=0.25, rely=0.3)
   

    Button(_frame, text='ISSUE', width=20, command=lambda: issue_book(int(_bookID.get()),_studentEmail.get()),font=('Courier',14)).place(anchor=CENTER,relx=0.5,rely=0.75)

    Button(_frame, text='Close', width=15, command=layout.destroy,font=('Courier',14)).place(relx=1, rely=0.3, anchor=E)

    layout.mainloop()



