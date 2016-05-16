from flask import render_template, request, make_response, Response, json, send_file
from app import app, creator

# This script is the interface between the user interface in the form of webpages, and the classes that perform
# the manipulations of data
ALLOWED_EXTENSIONS = set(['zip'])


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


#  unzip uploaded folder, regex according to user input, return zipped folder
@app.route('/create_test_files', methods=['POST'])
def create_test_files():
    if request.method == 'POST':
        zipfile = request.files['zip']
        data = json.loads(request.form['data'])
        regex = data['regex']
        zip_folder = app.config['ZIP_FOLDER']

        folder_cleared = creator.clear_folder(zip_folder)
        if folder_cleared:
            folder_unzipped = creator.unzip_folder(zipfile)
            if folder_unzipped:
                files_regexed = creator.regex_files(zip_folder, regex, zip_folder)
                if files_regexed:
                    files_zipped = creator.zip_files(zip_folder, zip_folder)
                    if files_zipped:
                        # TODO add logic to download zipped file
                        return send_file(app.config['DOWNLOAD_FOLDER'], as_attachment=True, attachment_filename='testfilecreator.zip')
        return False
