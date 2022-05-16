from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector 

def gen_payslip(emp_id,hours,week):
   
    hourly_rate = 15.00

# Checks if below normal hours and calculates 20% tax
    if hours <= 37:
        grossPay = hours * hourly_rate
        tax = grossPay * 0.20
        netPay = grossPay - tax

# If overtime done calculates 20% tax up to €750 
# and 40% tax on anything over this
    else:
        normalPay = 37 * hourly_rate
        overtime = hours - 37
        overpay = overtime * 21.00
        grossPay = normalPay + overpay  
        if grossPay <= 750:
            tax = grossPay * 0.20
            netPay = grossPay - tax
        else:                    
            highGross = grossPay - 750
            tax = (750 * 0.20) + (highGross * 0.40)
            netPay = grossPay - tax
    values = (emp_id, week, hours, grossPay, netPay)  

    sql = """INSERT INTO payroll (emp_id, week_no, hours, gross_pay, net_pay)
                    VALUES (%s, %s, %s, %s, %s)"""
    dbcon = dbconnector()
    cursor = dbcon.cursor()
    cursor.execute(sql,values)
    dbcon.commit()
    messagebox.showinfo("Success","Payroll Processed" )
    return


def dbconnector():
    dbcon = mysql.connector.connect (
    host ="127.0.0.1",
    user ="root",
    password ="root",
    database ="library"
    )
    return dbcon

def listTable():

    db = dbconnector()
    _list = []
    cursor = db.cursor()
    sql_query = "SHOW TABLES"
    cursor.execute(sql_query)
    for tbl in cursor:
        _list.append(tbl[0])      
    db.close()

    return _list

def init_db():

    if 'payroll' not in listTable():
        db = dbconnector()
        cursor =  db.cursor()
        sql_query = "CREATE TABLE payroll ( emp_id int NOT NULL ,week_no INT, hours INT, gross_pay INT, net_pay INT  )"
        cursor.execute(sql_query)
        print("Payroll Table Initialized")
        db.close()
    return True
    


def view_payslip():

    child = Tk()
    child.title("View Payroll")
    child.minsize(width=1200,height=800)

    tableFrame = Frame(child,bg='grey')
    tableFrame.place(relx=0.1,rely=0.25,relwidth=0.8,relheight=0.5)
    e=Label(tableFrame,width=10,text='EMP ID',borderwidth=2, relief='ridge',anchor='w')
    e.grid(row=0,column=0)
    e=Label(tableFrame,width=10,text='WEEK NO',borderwidth=2, relief='ridge',anchor='w')
    e.grid(row=0,column=1)
    e=Label(tableFrame,width=10,text='Hours',borderwidth=2, relief='ridge',anchor='w')
    e.grid(row=0,column=2)
    e=Label(tableFrame,width=10,text='Gross Pay',borderwidth=2, relief='ridge',anchor='w')
    e.grid(row=0,column=3)
    e=Label(tableFrame,width=10,text='Net Pay',borderwidth=2, relief='ridge',anchor='w')
    e.grid(row=0,column=4)

    dbcon = dbconnector()
    cursor = dbcon.cursor()
    search_query = 'SELECT * from payroll'
    cursor.execute(search_query)
    i = 1
    for book in cursor:
        for j in range(len(book)):
            e = Label(tableFrame, width=10, text=book[j])
            e.grid(row=i, column=j)
            
        i = i +1 
    Button(tableFrame, text='Exit', width=5, command=child.destroy,font=('Courier',14)).place(relx=0.9,anchor=NW)
    return

def tk_payroll():
    root = Tk()
    root.title("Payroll Managements")
    root.minsize(width=1200,height=800)


    # Title Decoration
    _title = Frame(root,bg="white",bd=5)
    _title.place(relx=0.25, y=100, relwidth=0.5, relheight=0.13)
    _titlelabel = Label(_title,text="Payroll MANAGEMENT", bg="black", fg="white", font=('Courier',15)).place(relx=0, rely=0, relwidth=1, relheight=1)
    

    # Frame for Login
    _contentFrame = Frame(root, bg="black",bd=5)
    _contentFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.5)

    Label(_contentFrame, text='Employee ID :',fg="white",bg="black",font=('Courier',14)).place(relx=0.2, rely=0.2)
    employee_id = Entry(_contentFrame)
    employee_id.place(relx=0.6, rely=0.2)

    Label(_contentFrame, text='Hours Worked :',fg="white",bg="black",font=('Courier',14)).place(relx=0.2, rely=0.4)
    hours_worked = Entry(_contentFrame)
    hours_worked.place(relx=0.6, rely=0.4)

    Label(_contentFrame, text='Weeks :',fg="white",bg="black",font=('Courier',14)).place(relx=0.2, rely=0.6)
    week = Entry(_contentFrame)
    week.place(relx=0.6, rely=0.6)

    Button(_contentFrame, text='Generate Payslip', width=25, command=lambda: gen_payslip(int(employee_id.get()),int(hours_worked.get()),int(week.get())),font=('Courier',14)).place(relx=0.2, rely=0.9, anchor=CENTER)

    Button(_contentFrame, text='View Payslip', width=25, command=view_payslip,font=('Courier',14)).place(relx=0.8, rely=0.9, anchor=CENTER)


    Button(_contentFrame, text='Exit', width=5, command=root.destroy,font=('Courier',14)).place(relx=0.9,anchor=NW)


    root.mainloop()


init_db()

tk_payroll()