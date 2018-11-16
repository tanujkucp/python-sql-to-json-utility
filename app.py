from flask import Flask, render_template, request, jsonify, send_from_directory, current_app
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


# stores the content of the file last uploaded
content = ''
UPLOAD_FOLDER = 'upload/'
DOWNLOAD_FOLDER = 'data/'


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        global UPLOAD_FOLDER
        filename = secure_filename(f.filename)
        f.save(os.path.join(UPLOAD_FOLDER, filename))
        text = readFile(filename)
        data = {'filename': filename}
        global content
        content = text if text is not None else 'Could not read file!'
        data['content'] = content
        data = jsonify(data)
        return data


@app.route('/downloader/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    global DOWNLOAD_FOLDER
    uploads = os.path.join(current_app.root_path, DOWNLOAD_FOLDER)
    print(uploads)
    return send_from_directory(directory=uploads, filename=filename, as_attachment=True)


@app.route('/json/2', methods=['GET', 'POST'])
def json2java():
    return j2java.main(content)


@app.route('/xml/2', methods=['GET', 'POST'])
def xml2json():
    return x2j.main(content)


@app.route('/json/1', methods=['GET', 'POST'])
def json2db():
    return j2db.main(content)


@app.route('/xml/1', methods=['GET', 'POST'])
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
