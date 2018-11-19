import mysql.connector
from flask import jsonify


def main():
    db = connectDB()
    data = fetch(db)
    data = {'source': data}
    xml = convertToXml(data)
    data['result'] = xml
    text = jsonify(data)
    return text


def connectDB():
    mydb = mysql.connector.connect(user='root',
                                   password='123',
                                   host='localhost',
                                   database='tanuj'
                                   )
    return mydb


def fetch(db):
    try:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM CONTACTS')
        data = cursor.fetchall()
        print('Table contains-\n')
        print(data)
        return data
    except:
        print('An error occurred while fetching data!\n')


def convertToXml(data):
    return ''