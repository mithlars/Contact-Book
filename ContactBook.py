import sqlite3
# Необходимо создать модуль с классом работы с базой данных
# Необходио заключить все это в блок try и предусмотреть ошибки
# Необходим графический интерфейс для ввода адреса и имени файла базы данных
# Необходимо определять в какой операционной системе осуществляется запуск программы и,
# исходя из этого, формировать адреса файлов конфигурации и базы данных

datafile = 'ContactBook.db'
conn = sqlite3.connect(f'{datafile}')
c = conn.cursor()

c.execute("SELECT name FROM sqlite_master WHERE type = 'table';")
tables1 = c.fetchall()
tables = []
for i in range(0,len(tables1)):
    tables.append(tables1[i][0])
    i += 1

if "favourites" not in tables:
    print("Create the table 'favourites'")
    c.execute("CREATE TABLE favourites (ContactID int);")
else:
    print("The table 'favourites' already made")

if "contacts" not in tables:
    print("Create the table 'contacts'")
    c.execute("CREATE TABLE contacts ("
              "ContactID int, "
              "nickname varchar(50), "
              "surname varchar(20), "
              "name varchar(20), "
              "otchestvo varchar(20), "
              "comment varchar(300), "
              "listNumberIDs varchar, "
              "listAdresIDs varchar"
              ");")
else:
    print("The table 'contacts' already made")
























conn.commit()
conn.close()