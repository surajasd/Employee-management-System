from tkinter import *
#import tkinter as tk
import psycopg2

root = Tk()
root.title("Employee management system")

def get_data(name,age,address):
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="7872",host="localhost", port="5432")
    curr = conn.cursor()
    query = '''INSERT INTO studentp (name,age,address) values (%s,%s,%s);'''
    curr.execute(query,(name,age,address))
    print("inserted")
    conn.commit()
    conn.close()
    display_all()

def search(id):
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="7872",host="localhost", port="5432")
    curr = conn.cursor()
    curr.execute( '''SELECT * FROM studentp WHERE id=%s;''', [id])
    row = curr.fetchone()
    
    display_search(row)
    conn.commit()
    conn.close()

def display_search(row):
    listbox = Listbox(frame,width=20,height=1)
    listbox.grid(row=11,column=1)
    listbox.insert(END, row)

def Delete_data(id):
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="7872",host="localhost", port="5432")
    curr = conn.cursor()
    curr.execute( '''DELETE FROM studentp WHERE id=%s;''', [id])
    conn.commit()
    conn.close()
    display_all()
    
def display_all():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="7872",host="localhost", port="5432")
    curr = conn.cursor()
    query = '''SELECT * FROM studentp;'''
    curr.execute(query)
    row = curr.fetchall()
    
    listbox = Listbox(frame,width=20,height=5)
    listbox.grid(row=8,column=1)
    for x in row:
        listbox.insert(END, x)
    
    

canvas = Canvas(root,height=1920,width=1080)
canvas.pack()

frame = Frame()
frame.place(relx=0.3,rely=0.1,relwidth=0.8,relheight=0.8)

label = Label(frame,text="Add Employee")
label.grid(row=0,column=1)

label = Label(frame,text="Name")
label.grid(row=1,column=0)

entry_name = Entry(frame)
entry_name.grid(row=1,column=1)

label = Label(frame,text="Age")
label.grid(row=2,column=0)

entry_age = Entry(frame)
entry_age.grid(row=2,column=1)

label = Label(frame,text="Address")
label.grid(row=3,column=0)

entry_address = Entry(frame)
entry_address.grid(row=3,column=1)

buttom = Button(frame,text="add data", command=lambda: get_data(entry_name.get(), entry_age.get(), entry_address.get()))
buttom.grid(row=4,column=1)

label = Label(frame,text="Search employee")
label.grid(row=6,column=1)

label = Label(frame,text="Search by employee id")
label.grid(row=7,column=0)

id_search = Entry(frame)
id_search.grid(row=7,column=1)

buttom = Button(frame,text="Search", command= lambda: search(id_search.get()))
buttom.grid(row=7,column=2)

label = Label(frame,text="Delete employee")
label.grid(row=9,column=1)

label = Label(frame,text="Delete employee by employee id")
label.grid(row=10,column=0)

id_delete = Entry(frame)
id_delete.grid(row=10,column=1)

buttom = Button(frame,text="Search", command= lambda: Delete_data(id_delete.get()))
buttom.grid(row=10,column=2)


display_all()

root.mainloop()