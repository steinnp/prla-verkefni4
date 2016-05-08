import argparse
import identify
import folder_utilities as folder_utils
import file_class

parser = argparse.ArgumentParser(description='Sort out messy movie folders')
parser.add_argument('directory_path', metavar = 'o', type = str,
                    help='path of the directory that needs sorting')
parser.add_argument('new_path', metavar = 'n', type = str,
                    help='path of the new sorted directory, defaults to the ' +
                         'path of the directory that needs sorting', nargs='?')

args = parser.parse_args()

FOLDER_SEPARATOR = ''
if folder_utils.detect_os() == 0:
    FOLDER_SEPARATOR = '/'
elif folder_utils.detect_os() == 1:
    FOLDER_SEPARATOR = r'\\'
else:
    raise EnvironmentError('This script only works on Unix and Linux')

if args.new_path is None:
    args.new_path = args.directory_path + FOLDER_SEPARATOR + 'temp'
    folder_utils.make_directory(args.new_path)

movie_files = folder_utils.list_movies(args.directory_path, FOLDER_SEPARATOR)
subtitle_files = folder_utils.list_subtitles(args.directory_path, FOLDER_SEPARATOR)
known_movies = []
unknown_movies = []

def fill_known_movies(files, separator):
    for i in files:
        known = identify.isolateSE(i,separator)
        if known is None:
            unknown_movies.append(i)
        else:
            known_movies.append(known)

fill_known_movies(movie_files, FOLDER_SEPARATOR)
#for i in known_movies:
#    print(i.get_name())
print(len(unknown_movies))
print(len(known_movies))
def move_file_to_new(file_instance):
    return None
