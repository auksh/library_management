#import login
from tkinter import messagebox
import landing

from utils import *

def login(username,password,admin):

    if not auth(username,password,admin):
        messagebox.showerror("Error", "Invalid Credentials")
        layout.destroy()
        
    else:
        if 'selected' in admin:
            layout.destroy()
            print("Admin Windows")
            landing.admin_login()
            
        else:
            print("User window")
            messagebox.showinfo("Info", "Login Successfull")
            layout.destroy() 
            landing.user_login()
           

                   

       
        



def main():

    # Initialize Tables
    global layout

    InitializeTables()

    layout = tk_layout("Library management system")

    # Title Decoration
    _title = Frame(layout,bg="white",bd=5)
    _title.place(relx=0.25, y=100, relwidth=0.5, relheight=0.13)
    _titlelabel = Label(_title,text="LIBRARY MANAGEMENT SYSTEM", bg="black", fg="white", font=('Courier',15)).place(relx=0, rely=0, relwidth=1, relheight=1)

    # Frame for Login
    LoginFrame = Frame(layout, bg="black",bd=5)
    LoginFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.5)

    Label(LoginFrame, text='Email',fg="white",bg="black",font=('Courier',14)).place(relx=0.35, rely=0.5, anchor=CENTER)
    Label(LoginFrame, text='Password',fg="white",bg="black",font=('Courier',14)).place(relx=0.35, rely=0.65, anchor=CENTER)

    username = Entry(LoginFrame)
    username.place(relx=0.6, rely=0.5, anchor=CENTER)
    password = Entry(LoginFrame,show='*')
    password.place(relx=0.6, rely=0.65, anchor=CENTER)



    #check_btn

    _adminchk = ttk.Checkbutton(LoginFrame, text='Librarian')
    _adminchk.place(relx=0.5, rely=0.8, anchor=CENTER)
  
    


    #login_btn
    button = Button(LoginFrame, text='Login', width=25, command=lambda: login(username.get(),password.get(),_adminchk.state()),font=('Courier',14)).place(relx=0.5, rely=0.95, anchor=CENTER)


    layout.mainloop()
    


if __name__ == "__main__":
    main()