
from sqlite3 import Cursor
from tkinter import *
from tkinter import ttk
import mysql.connector 
import random


def dbconnector():
    dbcon = mysql.connector.connect (
    host ="127.0.0.1",
    user ="root",
    password ="root",
    database ="library"
    )
    return dbcon


def checkTableExists(dbcon, tablename):
    
    dbcur = dbcon.cursor()
    dbcur.execute("""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = '{0}'
        """.format(tablename.replace('\'', '\'\'')))
    if dbcur.fetchone()[0] == 1:
        dbcur.close()
        return True

    dbcur.close()
    return False

def InitializeTables():
    dbcon = dbconnector()
    if not checkTableExists(dbcon,'Users'):
        InitUserTable()
    
    if not checkTableExists(dbcon,'books'):
        InitBookTable()
    
    print("Tables are already Initialized")    
        

def load_users():

    db = dbconnector()
    cursor = db.cursor()
    users = ['John','michel','mike','Tom','Goku','Gohan']
    for user in users:
        sql_query = "INSERT into Users (LastName, Email, Password, Admin ) VALUES ( '" + user + "','" + user + "@example.com' , 'password', " + str(random.randint(0,1)) + ")" 
        print(sql_query)
        cursor.execute(sql_query)
    db.commit()


def InitUserTable():

    db = dbconnector()
    cursor =  db.cursor()
    users_tbl = "CREATE TABLE Users ( uid int NOT NULL AUTO_INCREMENT, LastName varchar(255) NOT NULL, FirstName varchar(255), Email varchar(255), Password varchar(255), Admin BIT, PRIMARY KEY (uid))"
    cursor.execute(users_tbl)
    print("User Table Initialized")
    db.close()
    # Optional to load predefined users
    load_users()
    return

def InitBookTable():

    db = dbconnector()
    cursor =  db.cursor()
    book_tbl = "CREATE TABLE books (bid int NOT NULL AUTO_INCREMENT, title varchar(255) NOT NULL, author varchar(255), ISBN varchar(255), publication varchar(255), status varchar(255), issued_to int, FOREIGN KEY (issued_to) REFERENCES Users (uid),  PRIMARY KEY (bid))"
    cursor.execute(book_tbl)
    print("Book Table Initialized")
    db.close()
    return


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



def auth(email,password,admin_state):
    db = dbconnector()
    cursor = db.cursor()
    if 'selected' in admin_state:
        sql_query = "SELECT Password from Users WHERE Email = '" + email + "' AND Admin = 1"
    else:
        sql_query = "SELECT Password from Users WHERE Email = '" + email + "'"
    cursor.execute(sql_query)
    for x in cursor:
        if password == x[0]:
            print("Successfully Authenticated")
            db.close()
            return True
    db.close()
    print('Invalid Authenication')
    return False

#auth('navin@gmail.com','password')


def addbooks_db(_records):

    insertBooks = "INSERT into books  (title, author, ISBN, publication, status) VALUES ('" + _records['title'] +"', '" + _records['author']+"', '"+ _records['isbn']+"', '"+ _records['pub']+"','available')"  

    print(insertBooks)
    db = dbconnector()
    cursor = db.cursor()
    cursor.execute(insertBooks)
    db.commit()
    print('Book added Successfully')
    return  True
 



def bookID_exists(bookID):
    db = dbconnector()
    search_query = "SELECT bid from books WHERE bid =  '" + str(bookID) + "'"
    
    cursor = db.cursor()
    cursor.execute(search_query)
    
    for i in cursor:
        if bookID == i[0]:
            print("Book Exists")
            db.close()
            return True
        else:
            print("Book not found ")
            db.close()
            return False


def studentEmail_exists(emailID):
    db = dbconnector()
    search_query = "SELECT email from Users WHERE Email =  '" + emailID + "'"
    
    cursor = db.cursor()
    cursor.execute(search_query)
    
    for i in cursor:
        if emailID == i[0]:
            print("User Exists")
            db.close()
            return True
        else:
            print("User not exists")
            db.close()
            return False

def get_userID(emailID):
    db = dbconnector()
    search_query = "SELECT uid from Users WHERE Email =  '" + emailID + "'"
    
    cursor = db.cursor()
    cursor.execute(search_query)
    
    for i in cursor:
        return i[0]
      


def issueBook_to_user(bookID,emailID):
    user_id = get_userID(emailID)
    update_query = "UPDATE books SET status = 'not_available', issued_to = '" + str(user_id) + "' WHERE bid = '" + str(bookID) + "'" 
    db = dbconnector()
    cursor = db.cursor()
    cursor.execute(update_query)
    db.commit()
    db.close()


def return_bookdb(bookID):
    update_query = "UPDATE books SET status = 'available', issued_to = NULL WHERE bid = '" + str(bookID) + "'"
    db = dbconnector()
    cursor = db.cursor()
    cursor.execute(update_query)
    db.commit()
    db.close()
    

def delete_book_db(bookID):
    delete_query = "DELETE FROM books WHERE bid = '" + str(bookID) + "'"
    db = dbconnector()
    cursor = db.cursor()
    cursor.execute(delete_query)
    print("Book Deleted Successfully")
    db.commit()
    db.close()
    return True

def tk_layout():
    master = Tk()

    master.title("LMS")
    master.geometry("800x600")
    
    return master


