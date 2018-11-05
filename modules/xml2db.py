import sqlite3 as sql


#file = open('data1.xml', 'r')
#contents = file.read();



def main(contents):
    dbCon = connectDB()
    all = xmltoDB(contents)
    if dict is not None:
       insertToDB(dbCon,all)
    fetch(dbCon)

def connectDB():
    con = sql.connect('Data.db')



    query = 'CREATE TABLE IF NOT EXISTS CONTACTS(id INT PRIMARY KEY, name VARCHAR(30), email VARCHAR(30), phone VARCHAR(15))'
    con.execute(query)
    con.commit()
    return con


def xmltoDB(contents):
    all=[]
    contents = contents.strip()
    content = contents.split('>',1)
    array = content[1].strip()
    new = array[:len(content[1])-len(content[0])-3]
    new1 = new.strip()
    sp = new.split('>', 1)
    spn = sp[0]+'>'
    spn1 = new1.split(spn)

    for row in spn1:
        row = row.strip()
        row1 = row[:-(len(spn)+1)]
        row1 = row1.strip()
        sprow = row1.split('<')
        sprowf = sprow[1::2]
        dict = {}
        for i in sprowf:
            i1 = i.split('>')
            i2 = i1[1]
            j1 = i1[0]
            key = j1.strip()
            value = i2.strip()

            if value.isdigit():
                dict[key] = int(value)
            else:
                dict[key] =value
        if dict:
           t = (dict['id'],dict['name'],dict['email'],dict['mobile'])
           t = tuple(t)
           all.append(t)
    return all

def insertToDB(db, tuples):
    try:
        cursor = db.cursor()
        cursor.executemany('''INSERT INTO CONTACTS(id, name, email, phone) VALUES(?,?,?,?)''', tuples)
        db.commit()
    except:
        print('An error occurred while adding data!\n')

def fetch(db):
    try:
        cursor=db.cursor()
        cursor.execute('SELECT * FROM CONTACTS')
        data=cursor.fetchall()
        print('Table contains-\n')
        for row in data:
            print(row)
    except:
        print('An error occurred while fetching data!\n')
#main(contents)