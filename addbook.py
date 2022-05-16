
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from turtle import width
import utils


def addbook(_newbook):
    

    _records = {'title' : _newbook['title'].get(), 
                'author': _newbook['author'].get(), 
                'isbn'  : _newbook['isbn'].get(), 
                'pub'   : _newbook['pub'].get() }

    
    if utils.addbooks_db(_records):
        messagebox.showinfo("Success", "Book added successfully")
        root.destroy
       
        
    else:
        messagebox.showerror("Error", "Can't add to Database")
        
        
   
    return
    



def tk_addbook():
     
    global root
    root = Tk()
    root.title("Add Book")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    addbook_canvas = Canvas(root)
    addbook_canvas.config()
    addbook_canvas.pack(expand=True,fill=BOTH)

    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.4)

    # Book Title
    _title_label = Label(labelFrame,text="Title :", bg='black', fg='white')
    _title_label.place(relx=0.05,rely=0.35, relheight=0.08)

    _title = Entry(labelFrame)
    _title.place(relx=0.2,rely=0.35, relwidth=0.62, relheight=0.1)


    # Book Author
    _author_label = Label(labelFrame,text="Author :", bg='black', fg='white')
    _author_label.place(relx=0.05,rely=0.50, relheight=0.08)

    _author = Entry(labelFrame)
    _author.place(relx=0.2,rely=0.50, relwidth=0.62, relheight=0.1)


    # Book ISBN
    _isbn_label = Label(labelFrame,text="ISBN :", bg='black', fg='white')
    _isbn_label.place(relx=0.05,rely=0.65, relheight=0.08)

    _isbn = Entry(labelFrame)
    _isbn.place(relx=0.2,rely=0.65, relwidth=0.62, relheight=0.1)


        # Book Publication
    _pub_label = Label(labelFrame,text="Publication :", bg='black', fg='white')
    _pub_label.place(relx=0.05,rely=0.80, relheight=0.08)

    _pub = Entry(labelFrame)
    _pub.place(relx=0.2,rely=0.80, relwidth=0.62, relheight=0.1)

    

    _records = {'title' : _title, 'author': _author, 'isbn': _isbn, 'pub': _pub }


    # Add Button

    _add_btn = Button(root, text="ADD", command=lambda: addbook(_records))
    _add_btn.place(relx=0.25, rely=0.65, relwidth=0.18,relheight=0.08)


    # Cancel Button

    _cancel_btn = Button(root, text="Cancel", command=root.destroy)
    _cancel_btn.place(relx=0.60, rely=0.65, relwidth=0.18,relheight=0.08)


    root.mainloop()
