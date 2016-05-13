import os
basedir = os.path.abspath(os.path.dirname(__file__))

#configuration file for the app. This is where the upload folder and database are set globally.

BASE_FOLDER = basedir
APP_FOLDER = BASE_FOLDER + '/app'
ZIP_FOLDER = BASE_FOLDER + '\\testfilecreator'  # folder to zip
DOWNLOAD_FOLDER = BASE_FOLDER + '/testfilecreator.zip'  # zipped foulder

SECRET_KEY = '0Zr98j/3yX R~XHH!jmN]LWX/,?RTA'
