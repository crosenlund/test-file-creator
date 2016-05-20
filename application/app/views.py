from flask import render_template, request, json, send_file
from app import app, creator

# This script is the interface between the user interface in the form of webpages, and the classes that perform
# the manipulations of data
ALLOWED_EXTENSIONS = ['zip']


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


#  unzip uploaded folder, regex according to user input, return zipped folder
@app.route('/create_test_files', methods=['POST'])
def create_test_files():
    if request.method == 'POST':
        zip_file = request.files['zip']
        data = json.loads(request.form['data'])
        regex = data['regex']

        creator.clear_folders(zip_file)
        files_zipped = creator.create_files(zip_file, regex)
        if files_zipped:
            # creator.remove_first_file('')
            # is_zip = zipfile.is_zipfile(app.config['DOWNLOAD_FOLDER'])
            # print(is_zip)
            # TODO add logic to download zipped file
            return send_file(app.config['DOWNLOAD_FOLDER'], as_attachment=True, attachment_filename='testfilecreator.zip')
        return False
