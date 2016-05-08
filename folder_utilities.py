
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
    if not os.path.exists(newpath):
        os.makedirs(newpath)

# returns 0 for linux systems, 1 for unix and -1 for other operating systems
def detect_os():
    if _platform == "linux" or _platform == "linux2" or _platform == "darwin":
        return 0
    elif _platform == "win32":
        return 1
    else:
        return -1

# returns a list of all files in directory (requires full path)
def list_files(directory):
    return list(filter(path.isfile, listdir(directory)))

# returns true if directory is a directory false otherwise
def is_directory(directory):
    return not path.isfile

# returns a list of all files in directory (requires full path)
def list_directories(directory):
    d = '.'
    return [o for o in listdir(directory) if path.isdir(path.join(d,o))]
