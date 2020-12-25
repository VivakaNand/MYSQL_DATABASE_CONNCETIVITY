import mysql.connector

conn = mysql.connector.connect(host='localhost', user='root', password='password555',
database='new_database') # for existing database

my_cursor = conn.cursor()

# to create database
# query = 'CREATE DATABASE new_database'
# my_cursor.execute(query)

# to show database
query = 'SHOW DATABASES'
my_cursor.execute(query)

# to show all databases
# for database_name in my_cursor:
#    print(database_name)

# to list all databases
print(my_cursor.fetchall())



# to show table data
# for row in my_cursor:
#    print(row)

# to list all table data 
# print(my_cursor.fetchall())


# to create table in database
# query = 'CREATE TABLE student(name VARCHAR(255), age INT)'
# my_cursor.execute(query)

# to insert data in table 
# query = 'INSERT INTO student(name, age) VALUES (%s, %s)' # for SQLite VALUES (?, ?)
# insert single value
# values = ('Vivek', 25)
# my_cursor.execute(query, values) # execute single value

# insert many value
# values = [
#       ('Vivek', 25),
#       ('Mohit', 24),
#       ('Vivek', 35),
#       ('Vivek', 26),
#       ('Aneel', 28),
#       ('Vivek', 55),
# ]

# my_cursor.executemany(query, values) # execute many value

# to select values from table
# query = 'SELECT * FROM student'
# my_cursor.execute(query)

# for row in my_cursor:
#    print(row)
# print(my_cursor.fetchall())



conn.commit()
conn.close()