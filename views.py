from sqlite3 import Cursor
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from turtle import width
import utils


def view_table(_choice):
    
    if _choice == 'All':
        search_query = "SELECT * FROM books limit 0,10"
    elif _choice == 'Available':
        search_query = "SELECT * FROM books WHERE status = 'Available'"
    elif _choice == 'Issued':
        search_query = "SELECT * FROM books WHERE issued_to IS NOT NULL"

    tableFrame = Frame(layout,bg='white')
    tableFrame.place(relx=0.1,rely=0.25,relwidth=0.8,relheight=0.5)
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
    e=Label(tableFrame,width=10,text='Issued_to Email',borderwidth=2, relief='ridge',anchor='w',bg='black')
    e.grid(row=0,column=6)

    db = utils.dbconnector()
    cursor = db.cursor()
    
    cursor.execute(search_query)
    i = 1
    for book in cursor:
        for j in range(len(book)):
            e = Label(tableFrame, width=10, text=book[j],bg="black")
            e.grid(row=i, column=j)
            
        i = i +1 


    
    

    return

def tk_view():
    
    global layout

    layout = utils.tk_layout()

    _frame =  Frame(layout, bg="black",bd=5)
    _frame.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.1,anchor=N)

    Label(_frame, text='Filter By : ',fg="white",bg="black",font=('Courier',14)).place(relx=0.05, rely=0.1)


    _choiceVar = StringVar(_frame)
   # _choiceVar.set("All")

    _choice = OptionMenu(_frame, _choiceVar,"All","Available","Issued",command=view_table)
    _choice.place(relx=0.25,rely=0.1)
    Button(_frame, text='Close', width=15, command=layout.destroy,font=('Courier',14)).place(relx=1, rely=0.3, anchor=E)

    layout.mainloop()

