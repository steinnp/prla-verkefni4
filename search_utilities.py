import string_utilities

# returns true if a substring of 2 words or more is in both strings
def substring_match(a, b):
    c = string_utilities.clean_file_name(a).split(' ')
    d = string_utilities.clean_file_name(b).lower()
    if a == b:
        return a
    substrings = []
    for x in range(0,len(c)):
        for y in range(x+2, len(c) + 1):
            substrings.append(' '.join(c[x:y]))
    for x in substrings:
        if x.lower() in d:
            return True

    return False
#print(substring_match('this is a test', 'this is bad test'))
#print(substring_match('this a test', 'is bad test'))

#returns true if the string full is a substring in part
def partial_string_match(full, part):
    return full in part

#print(partial_string_match('test', 'testing this function'))
#print(partial_string_match('test', 'tesing this function'))
