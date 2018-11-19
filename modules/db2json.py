import mysql.connector
from flask import jsonify

def main():
    db = connectDB()
    data = fetch(db)
    json=convertToJson(data)
    data = {'source': data}
    data['result'] = json
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
        return data
    except:
        print('An error occurred while fetching data!\n')

def convertToJson(data):
   json='{\n  "data" : [\n'
   for row in data:
       start=''
       if row != data[0]: start+=',\n'
       start+='\t{\n'
       start+='\t  "id" : '+str(row[0])+',' \
                '\n\t  "name" : "' + row[1]+'",' \
                '\n\t  "email" : "'+row[2]+'",' \
                '\n\t  "mobile" : "'+row[3]+'"\n\t}'
       json+=start
   json+='\n  ]\n}'
   return json
