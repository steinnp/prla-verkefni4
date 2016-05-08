import string_utilities
import glob
from os import listdir
from os import rename
from os import path
from os import makedirs
from sys import platform as _platform
# moves old to new (does the same as the mv command)
def move_file(old,new):
    os.rename(old,new)

# makes a new directory at selected path
def make_directory(newpath):
    if not path.exists(newpath):
        makedirs(newpath)

# returns 0 for linux systems, 1 for unix and -1 for other operating systems
def detect_os():
    if _platform == "linux" or _platform == "linux2" or _platform == "darwin":
        return 0
    elif _platform == "win32":
        return 1
    else:
        return -1

# returns a list of all movie files in directory and subdirectories (requires full path)
def list_movies(directory, separator):
    a = []
    for filename in glob.iglob(directory + separator + '**' + separator + '*', recursive=True):
        if is_file(filename) and string_utilities.is_movie_file(filename):
            a.append(filename)
    return a

# returns a list of all subtitle files in directory and subdirectories (requires full path)
def list_movies(directory, separator):
    a = []
    for filename in glob.iglob(directory + separator + '**' + separator + '*', recursive=True):
        if is_file(filename) and string_utilities.is_subtitle_file(filename):
            a.append(filename)
    return a

# returns true if the directory is a file
def is_file(filename):
    return path.isfile(filename)

# returns a list of all files in directory (requires full path)
def list_directories(directory):
    d = '.'
    return [o for o in listdir(directory) if path.isdir(path.join(d,o))]
