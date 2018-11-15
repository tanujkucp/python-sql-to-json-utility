from flask import jsonify


def main(contents):
    str = xml2json(contents)
    writeFile(str)
    text={'content':str}
    text=jsonify(text)
    return text

def xml2json(contents):
    all = []
    contents = contents.strip()
    content = contents.split('>', 1)
    array = content[1].strip()
    mainName = content[0]
    mainName = mainName[1:]
    new = array[1:len(content[1]) - len(content[0]) - 3]
    new1 = new.strip()
    sp = new.split('>', 1)
    spn = sp[0] + '>'
    splitted = new1.split(spn)

    for row in splitted:
        row = row.strip()
        row1 = row[:-(len(spn) + 1)]
        row1 = row1.strip()
        sprow = row1.split('<')
        sprowf = sprow[1::2]
        list = []

        for i in sprowf:
            i1 = i.split('>')
            i2 = i1[1].strip()
            j1 = i1[0]
            j1 = j1.strip()
            if i2.isdigit() and j1 == 'id':
                i3 = i2
            else:
                i3 = '"' + i2 + '"'
            i3 = '"' + j1 + '"' + ' : ' + i3 + ',\n'
            list.append(i3)
        str = ''.join(list)
        str = str[:-2]
        if str:
            str1 = '\n{\n' + str + '},'
            all.append(str1)
    all1 = all[:]
    str2 = ''.join(all1)
    str2 = str2[:-1]
    str3 = '{\n' + '"' + mainName + '"' + ':[' + str2 + '\n]\n}'
    return str3


def writeFile(str):
    try:
        f = open('data/outputJSON.json', 'w+')
        f.write(str)
        print('JSON file created successfully!')
    except:
        print("An error occurred in file creation!")
