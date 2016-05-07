from re import sub
def replace(s):
    a = sub('[^\w]', ' ', s)
    a = sub('[_]', ' ', a)
    return a[::-1].replace(' ','.',1)[::-1]
