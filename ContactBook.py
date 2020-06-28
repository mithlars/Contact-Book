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

if "Favourites" not in tables:
    print("Create the table 'Favourites'")
    c.execute("CREATE TABLE Favourites (ContactID int);")
else:
    print("The table 'Favourites' already made")

if "Contacts" not in tables:
    print("Create the table 'Contacts'")
    c.execute("CREATE TABLE Contacts ("
              "ContactID int, "
              "NickName varchar(50), "
              "SurName varchar(20), "
              "Name varchar(20), "
              "Patronymic varchar(20), "
              "Comment varchar(300), "
              "ListPhoneNumberIDs varchar, "
              "ListAddressIDs varchar"
              ");")
else:
    print("The table 'contacts' already made")


if "PhoneNumbers" not in tables:
    print("Create the table 'PhoneNumbers'")
    c.execute("CREATE TABLE PhoneNumbers ("
              "PhoneNumID int, "
              "PhoneTagID int, "
              "Country int, "
              "Operator int, "
              "Number int, "
              "ContactID int"
              ");")
else:
    print("The table 'PhoneNumbers' already made")

if "phonetags" not in tables:
    print("Create the table 'phonetags'")
    c.execute("CREATE TABLE phonetags ("
              "PhoneTagID int, "
              "PhoneTag varchar(20) "
              ");")
else:
    print("The table 'phonetags' already made")

if "strtypes" not in tables:
    print("Create the table 'strtypes'")
    c.execute("CREATE TABLE strtypes ("
              "strtypeID int, "
              "strtype varchar(20) "
              ");")
else:
    print("The table 'strtypes' already made")

if "countries" not in tables:
    print("Create the table 'countries'")
    c.execute("CREATE TABLE countries ("
              "countryID int, "
              "country varchar(20) "
              ");")
else:
    print("The table 'countries' already made")

if "cities" not in tables:
    print("Create the table 'cities'")
    c.execute("CREATE TABLE cities ("
              "cityID int, "
              "city varchar(20) "
              ");")
else:
    print("The table 'cities' already made")

if "housetypes" not in tables:
    print("Create the table 'housetypes'")
    c.execute("CREATE TABLE housetypes ("
              "housetypeID int, "
              "housetype varchar(20) "
              ");")
else:
    print("The table 'housetypes' already made")

if "street" not in tables:
    print("Create the table 'street'")
    c.execute("CREATE TABLE street ("
              "streetID int, "
              "street varchar(20) "
              ");")
else:
    print("The table 'street' already made")

if "addresses" not in tables:
    print("Create the table 'addresses'")
    c.execute("CREATE TABLE addresses ("
              "addressID int, "
              "index int, "
              "countryID int, "
              "cityID int, "
              "strtypeID int, "
              "streetID int,"
              "housenum int,"
              "housetypeID int,"
              "doorsnum int,"
              "doorcode varchar(10),"
              "floor int,"
              "flat int"
              ");")
else:
    print("The table 'addresses' already made")

















conn.commit()
conn.close()