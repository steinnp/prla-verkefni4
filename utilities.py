from re import sub
def replace_files(movie):
    clean = sub('[^\w]', ' ', movie)
    clean = sub('[_]', ' ', clean)
    return clean[::-1].replace(' ','.',1)[::-1]

def replace_dirs(directory):
    clean = sub('[^\w]', ' ', directory)
    clean = sub('[_]', ' ', clean)
    return clean

def is_movie_file(movie):
    format1 = movie[-3:]
    format2 = movie[-4:]
    endings = open('movie_endings.txt','r').read()
    if (format1 in endings) or (format2 in endings):
        return True
    else:
        return False

print(is_movie_file('test.avi'))
print(is_movie_file('test.divx'))
print(is_movie_file('test.dvx'))
