import sqlite3

connection = sqlite3.connect("data.db")
curser = connection.cursor()

create_table = "CREATE TABLE  IF NOT EXISTS users (id INTEGER PRIMARY KEY , username text, password real)"
curser.execute(create_table)

create_table = "CREATE TABLE  IF NOT EXISTS items (id INTEGER PRIMARY KEY , name text, price real)"
curser.execute(create_table)
#curser.execute("INSERT INTO items VALUES ('test',10.99)")
connection.commit()

connection.close()
