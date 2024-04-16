# lib/models/__init__.py
    #Established a connection to the SQLlite database data.db
    #Ereates a cursor object for executing SQL statements on that database 

import sqlite3

db_connection = sqlite3.connect('data.db')
db_cursor = db_connection.cursor() 

