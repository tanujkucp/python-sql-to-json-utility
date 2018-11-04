

def main(contents):
    allVariables = parseJSON(contents)
    file = openOutputFile()
    if file is not None:
        writeToFile(file,allVariables)


def parseJSON(contents):
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
        row=rows[0]
        row = row.strip()
        keys = row.split(',')
        if len(keys) > 4:
            del keys[len(keys) - 1]
        allVariables = {}
        for key in keys:
            key = key.strip()
            pair = key.split(':', 2)
            tag = pair[0].strip()
            tag = tag.split('"', 2)
            tag = tag[1]
            value = pair[1].strip()
            if value[0] == '"':
                allVariables[tag] = 'String'
            else:
                allVariables[tag] = 'int'
            #elif value[0] == '[': then it is an array - then find datatype of values inside array
        return allVariables


def writeToFile(file, allVariables):
    file.write('public class JSONmodel {\n\n')
    for variable in allVariables:
        file.write('\tprivate '+allVariables[variable]+' '+variable+';\n')
    file.write('\npublic JSONmodel() { }\n\n}')
    file.close()
    print('Java model made successfully from JSON.\n')
    input=readFile()
    if input is not None:
        text = input.read()
        print(text)


def openOutputFile():
    try:
        file = open('data/JSONmodel.java', 'w')
        return file
    except IOError as e:
        print(e)
        return None

def readFile():
    try:
        file = open('data/JSONmodel.java', 'r')
        return file
    except IOError as e:
        print(e)
        return None