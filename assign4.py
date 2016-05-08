import argparse
import folder_utilities as folder_utils

parser = argparse.ArgumentParser(description='Sort out messy movie folders')
parser.add_argument('directory_path', metavar = 'o', type = str,
                    help='path of the directory that needs sorting')
parser.add_argument('new_path', metavar = 'n', type = str,
                    help='path of the new sorted directory, defaults to the ' +
                         'path of the directory that needs sorting', nargs='?')

args = parser.parse_args()
#print(args)

files = folder_utils.list_files(args.directory_path)
directories = folder_utils.list_directories(args.directory_path)

def move_file_to_new(file_instance):
    return None
