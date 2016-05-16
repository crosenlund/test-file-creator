from app import app
import os
import re
import shutil
import zipfile


def clear_folder(path):
    path = fix_slashes(path)
    if os.path.isdir(path):
        dir_path = path
        for file in os.listdir(dir_path):
            file_path = os.path.join(dir_path, file)
            if os.path.isdir(file_path) and not os.path.islink(file_path):
                try:
                    shutil.rmtree(file_path)
                except Exception as e:
                    print(e)
            elif os.path.exists(file_path):
                try:
                    os.remove(file_path)
                except Exception as e:
                    print(e)
    return True


def unzip_folder(zipFile):
    with zipfile.ZipFile(zipFile, 'r') as myzip:
        path = app.config['ZIP_FOLDER'] + '/'
        for file in myzip.infolist():
            with myzip.open(file.filename) as myfile:
                if file.filename.endswith('/'):
                    if not os.path.exists(path + file.filename):
                        os.mkdir(fix_slashes(os.path.join(app.config['ZIP_FOLDER'], file.filename)))
                else:
                    write_file(myfile, app.config['ZIP_FOLDER'] + '/' + file.filename)
    return True


def write_file(file, file_name):
    print('write_file: ' + fix_slashes(file_name))
    file_string = file.read()
    w = open(fix_slashes(file_name), 'wb')
    w.write(file_string)
    w.close()
    return True


def regex_files(files, regex, zip_path):
    print('--------- regex')
    regex_list = regex
    files = fix_slashes(files)
    zip_path = fix_slashes(zip_path)
    if os.path.isdir(files):
        for file in os.listdir(files):
            if os.path.isfile(file):
                file_path = os.path.join(zip_path, file)
                r = open(file_path, 'r+')
                file_string = r.read()
                r.close()
                for regex in regex_list:
                    s = re.compile(regex['name'], re.DOTALL)
                    file_string = re.sub(s, regex['value'], file_string)
                w = open(os.path.join(zip_path, file_path), 'w')
                w.write(file_string)
                w.close()
            else:
                file_path = os.path.join(zip_path, file)
                regex_files(file_path, regex, file_path)
    else:
        file_path = os.path.join(zip_path, files)
        r = open(file_path, 'r+')
        file_string = r.read()
        r.close()
        for regex in regex_list:
            s = re.compile(regex['name'], re.DOTALL)
            file_string = re.sub(s, regex['value'], file_string)
        w = open(os.path.join(zip_path, file_path), 'w')
        w.write(file_string)
        w.close()
    return True


def zip_files(files, path):
    print('---------------- zip_files')
    with zipfile.ZipFile(app.config['DOWNLOAD_FOLDER'], 'w') as myzip:
        for file in os.listdir(files):
            if os.path.isdir(os.path.join(path, file)):
                path = os.path.join(path, file)
                zip_files(path, path)
            else:
                file_path = fix_slashes(os.path.join(path, file))
                myzip.write(file_path)
    return True


def fix_slashes(str1):
    if app.config['DEVELOPMENT']:
        s = re.compile('/', re.DOTALL)
        str1 = re.sub(s, '\\\\', str1)
    return str1
