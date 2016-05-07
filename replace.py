from re import sub
def replace(movie):
    a = sub('[^\w]', ' ', movie)
    a = sub('[_]', ' ', a)
    return a[::-1].replace(' ','.',1)[::-1]

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
