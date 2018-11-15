from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os

import modules.json2db as j2db
import modules.json2java as j2java
import modules.xml2db as x2db
import modules.xml2json as x2j


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/check', methods=['POST', 'GET'])
def square():
    data = {'data': 4}
    data = jsonify(data)
    return data

content=''

@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        UPLOAD_FOLDER = 'upload/'
        filename = secure_filename(f.filename)
        f.save(os.path.join(UPLOAD_FOLDER, filename))
        text = readFile(filename)
        data = {'filename': filename}
        global content
        content = text if text is not None else 'Could not read file!'
        data['content']=content
        data = jsonify(data)
        return data

@app.route('/json/2',methods=['GET','POST'])
def json2java():
    return j2java.main(content)

@app.route('/xml/2',methods=['GET','POST'])
def xml2json():
    return x2j.main(content)

@app.route('/json/1',methods=['GET','POST'])
def json2db():
    return j2db.main(content)

@app.route('/xml/1',methods=['GET','POST'])
def xml2db():
    return x2db.main(content)

def readFile(name):
    try:
        file = open('upload/' + name, 'r')
        contents = file.read()
        return contents
    except IOError as e:
        print(e)
        return None


if __name__ == '__main__':
    app.run(debug=True)
