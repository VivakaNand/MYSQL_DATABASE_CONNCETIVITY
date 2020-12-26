# stater code
import tkinter as tk
from tkinter import ttk
import mysql.connector
win = tk.Tk()
win.title('Database Conncetivity GUI')

# create labels
db_label = ttk.Label(win, text='Select database : ')
db_label.grid(row=1, column=0, sticky=tk.W)

name_label = ttk.Label(win, text='Enter your name : ')
name_label.grid(row=2, column=0, sticky=tk.W)

age_label = ttk.Label(win, text='Enter your age : ')
age_label.grid(row=3, column=0, sticky=tk.W)

conn = mysql.connector.connect(host='localhost', user='root', password='pasword555') 
my_cursor = conn.cursor()
query1= 'SHOW DATABASES;'
my_cursor.execute(query1)
db = my_cursor.fetchall()

# create combobox
db_var = tk.StringVar()
db_combobox = ttk.Combobox(win, width=14, textvariable=db_var, state='readonly')
db_combobox['values'] = db
db_combobox.current(0)
db_combobox.grid(row=1,column=1)

# create entry box
name_var = tk.StringVar()
name_entrybox = ttk.Entry(win,width=16, textvariable=name_var)
name_entrybox.grid(row=2, column=1)
name_entrybox.focus()

age_var = tk.StringVar()
age_entrybox = ttk.Entry(win,width=16, textvariable=age_var)
age_entrybox.grid(row=3, column=1)

# create button


def show_db():
    global conn, my_cursor
    query = 'SHOW DATABASES;'
    my_cursor.execute(query)
    print(my_cursor.fetchall())
    
    conn.commit()
    conn.close()

def update_db():
      
    username = name_var.get()
    userage = age_var.get()
    userdb = db_var.get()
    
    conn = mysql.connector.connect(host='localhost', user='root', password='menghwar555', database = userdb)
    my_cursor = conn.cursor()
    # to insert data in table 
    query = 'INSERT INTO student(name, age) VALUES (%s, %s)' # for SQLite VALUES (?, ?)
    # insert single value
    values = (username, userage)
    my_cursor.execute(query, values) # execute single value
    
    conn.commit()
    conn.close()

    print(f'Database updated with name : {username} and age : {userage}')
    name_entrybox.delete(0, tk.END)
    age_entrybox.delete(0, tk.END)
        
    name_label.configure(foreground='blue')
    submit_button.configure(foreground='blue')


show_db_button = tk.Button(win, text='Show Database',command = show_db)
show_db_button.grid(row=0, column=0)

submit_button = tk.Button(win, text='Submit',command = update_db)
submit_button.grid(row=4, column=0)

win.mainloop()