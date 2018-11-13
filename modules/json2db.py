# all the source code for the first module (part) of the project goes here
# other modules will also be made as other python files under this folder 'modules'
# import sqlite3 as sql
import mysql.connector


def main(contents):
    db = connectDB()
    tuples = parseJSON(contents)
    if tuples is not None:
        insertToDB(db, tuples)
    fetch(db)


def connectDB():
    mydb = mysql.connector.connect(user='root',
                                   password='123',
                                   host='localhost',
                                   database='tanuj'
                                   )
    query = 'CREATE TABLE IF NOT EXISTS CONTACTS(id INT PRIMARY KEY, name VARCHAR(30), email VARCHAR(30), phone VARCHAR(15))'
    cursor = mydb.cursor()
    cursor.execute(query)
    mydb.commit()
    return mydb


def parseJSON(contents):
    tuples = []
    contents = contents.strip()
    contents = contents[1:len(contents) - 1]
    contents = contents.strip()
    data = contents.split(':', 1)
    if data[0].strip() != '"data"':
        return None
    else:
        arr = data[1].strip()
        arr = arr[1: len(arr) - 1]
        arr = arr.strip()
        arr = arr[1:len(arr)]
        rows = arr.split('{')
        for row in rows:
            row = row.strip()
            keys = row.split(',')
            if len(keys) > 4:
                del keys[len(keys) - 1]
            allValues = {}
            for key in keys:
                key = key.strip()
                pair = key.split(':', 2)
                tag = pair[0].strip()
                tag = tag.split('"', 2)
                tag = tag[1]
                value = pair[1].strip()
                value = value.split('"', 2)
                if value[0] != '':
                    allValues[tag] = int(value[0])
                else:
                    allValues[tag] = value[1]
            tup = (allValues['id'], allValues['name'], allValues['email'], allValues['mobile'])
            tuples.append(tup)
        return tuples


def insertToDB(db, tuples):
    try:
        cursor = db.cursor()
        cursor.executemany('''INSERT INTO CONTACTS(id, name, email, phone) VALUES(%s,%s,%s,%s)''', tuples)
        db.commit()
        print('Data imported successfully!')
    except:
        print('An error occurred while adding data!\n')


def fetch(db):
    try:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM CONTACTS')
        data = cursor.fetchall()
        print('Table contains-\n')
        for row in data:
            print(row)
    except:
        print('An error occurred while fetching data!\n')
