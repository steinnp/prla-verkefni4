from re import sub

def clean_file_name(movie):
    movie = movie.strip()
    clean = sub('[^\w]', ' ', movie)
    clean = sub('[_]', ' ', clean)
    return clean[::-1].replace(' ','.',1)[::-1]

def replace_dirs(directory):
    clean = sub('[^\w]', ' ', directory)
    clean = sub('[_]', ' ', clean)
    return clean

def is_movie_file(movie):
    movie_type = movie[movie.rfind('.')+1:]
    endings = open('movie_endings.txt','r').read()
    if movie_type in endings:
        return True
    else:
        return False

#print(is_movie_file('test.avi'))
#print(is_movie_file('test.divx'))
#print(is_movie_file('test.dvx'))
