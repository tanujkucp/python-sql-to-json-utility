import modules.json2db as j2db
import modules.json2java as j2java
import modules.xml2db as x2db
import modules.xml2json as x2j

# this is the main program which connects all the modules.
# Upon run of this project , this file is run first


def showMainMenu():
    print('^^^^^^^^^^^^Welcome to the main menu^^^^^^^^^^^^\n')
    print('What type of file do you have?\n1. JSON\t2. XML\n')
    answer=int(input('Answer:'))
    showNextMenu(answer)


def showNextMenu(choice1):
    if choice1==1:
        print('Choose an operation for JSON-\n1. JSON to SQL DB\t2. JSON to Java Class\n')
        answer=int(input('Answer:'))
        performJSON(choice1,answer)
    elif choice1==2:
        print('Choose an operation for XML-\n1. XML to SQL DB\t2. XML to JSON\n')
        answer = int(input('Answer:'))
        performXML(choice1,answer)
    else:
        print('Wrong selection!')
        showMainMenu()


def performJSON(choice1,choice2):
    fileName = input('Enter JSON file name to convert(with .json):')
    if fileName.strip()[-4:] == 'json':
        success=readFile(fileName)
        if success!=None:
            if choice2==1:
                j2db.main(success)
            elif choice2==2:
                j2java.main(success)
            else:
                print('Wrong Selection')
                showNextMenu(choice1)
        else:
            print('Error while opening specified file.Try different file name!\n')
            performJSON(choice1,choice2)
    else:
        print('Filename should end with .json. Try Again!')
        performJSON(choice1,choice2)


def performXML(choice1,choice2):
    fileName = input('Enter XML file name to convert(with .xml):')
    if fileName.strip()[-3:] == 'xml':
        success=readFile(fileName)
        if success!=None:
            if choice2 == 1:
                x2db.main(success)
            elif choice2 == 2:
                x2j.main(success)
            else:
                print('Wrong Selection')
                showNextMenu(choice1)
        else:
            print('Error while opening specified file.Try different file name!\n')
            performXML(choice1,choice2)
    else:
        print('Filename should end with .xml. Try Again!')
        performXML(choice1, choice2)


def readFile(name):
    try:
        file = open('data/'+name, 'r')
        contents = file.read()
        return contents
    except IOError as e:
        print(e)
        return None

# main function call that runs this code
showMainMenu()