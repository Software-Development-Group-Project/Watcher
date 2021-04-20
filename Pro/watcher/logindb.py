import sqlite3  
  
con = sqlite3.connect("admin.db")  
print("Database opened successfully")  
  
con.execute("create table Admin (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, email TEXT UNIQUE NOT NULL, password TEXT UNIQUE NOT NULL)")  
  
print("Table created successfully")  
  
con.close()  