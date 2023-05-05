"""
Author: Dr. Reza Dilmaghani
"""

from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

#import platform
import glob
import shutil
import os
import re
from werkzeug.utils import secure_filename

#if platform.system() == "Linux":
#    from utilities.nlp_utils import identify_ner_and_change_case



NEWLINE = "\n"
TOKEN_LIMIT  = 400
def write_to_file(directory, no_of_splits, file_data):
    with open(directory + "file" + str(no_of_splits) + ".txt", 'w', errors='ignore', encoding='utf-8', ) as f:
        f.write(file_data)

def empty_upload_download(filedir1, filedir2):
    ## empty upload folder
    folder = filedir1
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        if os.path.isfile(file_path):
            os.unlink(file_path)

    ## empty download folder
    folder = filedir2
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        if os.path.isfile(file_path):
            os.unlink(file_path)

def save_file(filepath, file):
    filename = secure_filename(file.filename)
    filetype = re.search(r"(?<=\.)[^.]*$", filename).group()
    file.save(os.path.join(filepath, filename))
    return filename, filetype

def allowed_file(filename, exts):
    return '.' in filename and filename.rsplit('.', 1)[1] in exts

def remove_dir(dirPath):
    for root, dirs, files in os.walk(dirPath, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))

def copy_file(src, dest):
    src_files = glob.glob(src + "*.txt")
    for file_name in src_files:
        if (os.path.isfile(file_name)):
            shutil.copy(file_name, dest)

