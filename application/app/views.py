from flask import render_template, request, make_response, Response, json, send_file
from app import app, creator

# This script is the interface between the user interface in the form of webpages, and the classes that perform
# the manipulations of data
ALLOWED_EXTENSIONS = set(['zip'])


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


# accepts an uploaded file and parses it into a new scenario with a name, description, and esps
@app.route('/create_test_files', methods=['POST'])
def create_test_files():
    print('create_test_files')
    if request.method == 'POST':
        print('POST')
        zipfile = request.files['zip']
        print('ZIP')
        print(request.form['data'])
        # data = json.loads(request.form['data'])
        print('DATA')
        regex = request.form['data']
        print('REGEX')
        print(zipfile)
        print(regex)
        # zipfile = 'zipTest.zip'
        # regex = {'Change Me!': "I was Changed!!!"}

        folder_cleared = creator.clear_folder()
        if folder_cleared:
            folder_unzipped = creator.unzip_folder(zipfile)
            if folder_unzipped:
                files_regexed = creator.regex_files(regex)
                if files_regexed:
                    files_zipped = creator.zip_files()
                    if files_zipped:
                        # TODO add logic to download zipped file
                        return send_file(app.config['DOWNLOAD_FOLDER'], as_attachment=True, attachment_filename='testfilecreator.zip')

        return False
