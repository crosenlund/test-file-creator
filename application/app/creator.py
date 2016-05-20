from app import app
import os
import re
import shutil
import zipfile


def clear_folders(path):
    # first remove zipped file that is used for downloading
    zipped_path = fix_slashes(app.config['DOWNLOAD_FOLDER'])
    zipped_path = app.config['DOWNLOAD_FOLDER']
    if os.path.isdir(zipped_path) and not os.path.islink(zipped_path):
        try:
            shutil.rmtree(zipped_path)
        except Exception as e:
            print(e)
    elif os.path.exists(zipped_path):
        try:
            os.remove(zipped_path)
        except Exception as e:
            print(e)
    return True


def create_files(zipFile, regex):
    regex_list = regex
    # zipFile = fix_slashes(zipFile)
    with zipfile.ZipFile(zipFile, 'r') as myzip:
        for file in myzip.infolist():
            with myzip.open(file.filename) as myfile:
                with zipfile.ZipFile('testfilecreator.zip', 'a',
                                     compression=zipfile.ZIP_DEFLATED) as zippedfolder:
                    file_string = myfile.read()
                    for regex in regex_list:
                        if regex['value']:
                            s = re.compile(regex['name'].encode(), re.DOTALL)
                            file_string = re.sub(s, regex['value'].encode(), file_string)
                    zippedfolder.writestr(file.filename, file_string, zipfile.ZIP_DEFLATED)
    return True


def fix_slashes(str1):
    if app.config['DEVELOPMENT']:
        s = re.compile('/', re.DOTALL)
        str1 = re.sub(s, '\\\\', str1)
    return str1
