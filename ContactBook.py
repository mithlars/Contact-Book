import sqlite3
datafile = input("Введите адрес файла базы данных")
conn = sqlite3.connect(f'{datafile}')
c = conn.cursor()

tables = c.execute("CREATE TABLE favourite")




























conn.commit()
conn.close()