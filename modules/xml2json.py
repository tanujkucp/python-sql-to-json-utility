
file = open('data1.xml', 'r')
contents = file.read();

def main(contents):
    str = xml2json(contents)
    writeFile(str)

def xml2json(contents):
    all = []
    str2 =''
    str3 = ''
    contents = contents.strip()
    content = contents.split('>', 1)
    array = content[1].strip()
    mainName = content[0]
    mainName = mainName[1:]
    new = array[:len(content[1]) - len(content[0]) - 3]
    new1 = new.strip()
    sp = new.split('>', 1)
    tbname = sp[0]
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
            i2 = i1[1]
            j1 = i1[0]
            j1=j1.strip()
            if i2.isdigit():
                i3 = i2
            else:
                i3 = '"' + i2 + '"'
            i3 = '"'+j1+'"'+' : '+i3+',\n'
            list.append(i3)
        str = ''.join(list)
        str = str[:-2]
        str1 = '\n{\n' + str + '},'
        all.append(str1)
    all1 = all[1:]
    str2 = ''.join(all1)
    str2 = str2[:-1]
    str3 = '{\n'+'"'+mainName+'"'+':['+str2+'\n]\n}'

    return str3

def writeFile(str):
    try:
        filename = input('Enter filename you want to save as json:')
        f = open(filename + '.json', 'w+')
        f.write(str)
    except:
        print("File name already exists, try another name")



main(contents)