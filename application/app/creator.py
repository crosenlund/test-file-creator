from app import app
import os
import re
import zipfile


def clear_folder():
    print(os.listdir(app.config['ZIP_FOLDER']))
    print(app.config['BASE_FOLDER'])
    for file in os.listdir(app.config['ZIP_FOLDER']):
        file_path = os.path.join(app.config['ZIP_FOLDER'], file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)
    return True


def unzip_folder(zipFile):
    with zipfile.ZipFile(zipFile, 'r') as myzip:
        print(myzip.infolist())
        path = app.config['ZIP_FOLDER'] + '\\'
        for file in myzip.infolist():
            with myzip.open(file.filename) as myfile:
                print(file.filename.endswith('/'))
                if file.filename.endswith('/'):
                    print('is dir')
                    print(file.filename)
                    print(file)
                    if not os.path.exists(file.filename):
                        print('new dir')
                        print(path + file.filename)
                        os.mkdir(path + file.filename)
                    path = path + file.filename
                else:
                    write_file(myfile, path + file.filename)
    return True


def dir_exists(f):
    d = os.path.dirname(f)
    print(f)
    print(d)
    if os.path.exists(d):
        return True


def write_file(file, file_name):
    file_string = file.read()
    print(file_string)
    w = open(app.config['ZIP_FOLDER'] + '/' + file_name, 'wb')
    w.write(file_string)
    w.close()
    return True


def regex_files(regex):
    regex_list = regex
    for file in os.listdir(app.config['ZIP_FOLDER']):
        file_path = os.path.join(app.config['ZIP_FOLDER'], file)
        print(file_path)
        r = open(file_path, 'r+')
        file_string = r.read()
        r.close()
        print(regex_list)
        for regex, replacement in regex_list.items():
            s = re.compile(regex, re.DOTALL)
            file_string = re.sub(s, replacement, file_string)
        w = open(file_path, 'w')
        w.write(file_string)
        w.close()
    return True


def zip_files():
    print('zip_files')
    with zipfile.ZipFile('testfilecreator.zip', 'w') as myzip:
        for file in os.listdir(app.config['ZIP_FOLDER']):
            file_path = os.path.join(app.config['ZIP_FOLDER'], file)
            myzip.write(file_path)
    return True
