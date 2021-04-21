import sqlite3  
  
con = sqlite3.connect("members.db")  
print("Database opened successfully")  
  
con.execute("create table Members (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL, address TEXT NOT NULL, number INTEGER NOT NULL)")
print("Table created successfully")  
  
con.close()  