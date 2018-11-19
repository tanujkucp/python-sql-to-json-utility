import mysql.connector
from flask import jsonify


def main():
    db = connectDB()
    data = fetch(db)
    xml = convertToXml(data)
    data = {'source': data}
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
        print(data)
        return data
    except:
        print('An error occurred while fetching data!\n')


def convertToXml(data):
    xml='<students> '
    for row in data:
        start=''
        start+='\n<student> \n \t<id>'+str(row[0])+'</id>' \
                '\n \t<name>'+row[1]+'</name>' \
                '\n\t<email>'+row[2]+'</email>' \
                '\n\t<mobile>'+row[3]+'</mobile>' \
                '\n</student>'
        xml += start
    xml += '\n</students>'
    return xml
