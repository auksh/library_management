from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import utils


def search_book(title,author):

    print(title,author)
    search_query = "SELECT * FROM books WHERE title = '" + title + "' OR author = '" + author + "'"


    tableFrame = Frame(layout,bg='white')
    tableFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.5)
    e=Label(tableFrame,width=10,text='Id',borderwidth=2, relief='ridge',anchor='w',bg='black')
    e.grid(row=0,column=0)
    e=Label(tableFrame,width=10,text='Title',borderwidth=2, relief='ridge',anchor='w',bg='black')
    e.grid(row=0,column=1)
    e=Label(tableFrame,width=10,text='Author',borderwidth=2, relief='ridge',anchor='w',bg='black')
    e.grid(row=0,column=2)
    e=Label(tableFrame,width=10,text='ISBN',borderwidth=2, relief='ridge',anchor='w',bg='black')
    e.grid(row=0,column=3)
    e=Label(tableFrame,width=10,text='Publication',borderwidth=2, relief='ridge',anchor='w',bg='black')
    e.grid(row=0,column=4)
    e=Label(tableFrame,width=10,text='Status',borderwidth=2, relief='ridge',anchor='w',bg='black')
    e.grid(row=0,column=5)

    db = utils.dbconnector()
    cursor = db.cursor()
    
    cursor.execute(search_query)
    i = 1
    for book in cursor:
        for j in range(len(book)):
            e = Label(tableFrame, width=10, text=book[j],bg="black")
            e.grid(row=i, column=j)
            print(book[j])
        i = i +1 


    
    

    return

def tk_search():
    
    global layout

    layout = utils.tk_layout()

    _frame =  Frame(layout, bg="black",bd=5)
    _frame.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.3,anchor=N)

    Label(_frame, text='Title : ',fg="white",bg="black",font=('Courier',14)).place(relx=0.05, rely=0.1)

    search_title = Entry(_frame)
    search_title.place(relx=0.25, rely=0.1)

    Label(_frame, text='Author : ',fg="white",bg="black",font=('Courier',14)).place(relx=0.05, rely=0.4)

    search_author = Entry(_frame)
    search_author.place(relx=0.25, rely=0.4)

    Button(_frame, text='Search', width=20, command=lambda: search_book(search_title.get(),search_author.get()),font=('Courier',14)).place(anchor=CENTER,relx=0.5,rely=0.75)

    Button(_frame, text='Close', width=15, command=layout.destroy,font=('Courier',14)).place(relx=1, rely=0.3, anchor=E)

    layout.mainloop()

