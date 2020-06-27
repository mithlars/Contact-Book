import sqlite3
datafile =
conn = sqlite3.connect('ContactBook.db')
c = conn.cursor()
tables = c.execute()




























conn.commit()
conn.close()