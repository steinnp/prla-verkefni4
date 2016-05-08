
# returns the longest matching substring in both strings if it exists
def substring_match(a, b):
    a = a[:min(len(a),len(b))]
    b = b[:min(len(a),len(b))]
    if a == b:
        return a
    while ' ' in a:
        a = a.rsplit(' ', 1)[0]
        b = b.rsplit(' ', 1)[0]
        if a == b:
            return a
    return 0
#print(substring_match('this is a test', 'this is bad test'))
#print(substring_match('this a test', 'is bad test'))

#returns true if the string full is a substring in part
def partial_string_match(full, part):
    return full in part

#print(partial_string_match('test', 'testing this function'))
#print(partial_string_match('test', 'tesing this function'))
