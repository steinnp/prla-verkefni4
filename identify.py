import re
import string_utilities as strUtil
import file_class



romanTestReg = re.compile(r"""^(?P<title>[-\w'"]+(?P<separator>[ .])(?:[-\w'"]+\2)*?)(?:(?:(?:(?!\d+\2)(?:s(?:eason\2?)?)(?P<season>(?:XC|XL|L?X{0,3})(?:IX|IV|V?I{0,3}))(?:\s{0,4})(?:(?:e(?: pisode\2?)?))?(?P<episode>\d\d?)?(?:e\d\d?(?:-e?\d\d?)?\d\d?)?)))""",re.I|re.X|re.M)
testReg = re.compile(r"""^(?P<title>[-\w'"]+(?P<separator>[ .])(?:[-\w'"]+\2)*?)(?:(?:(?!\d+\2)(?:s(?:eason\2?)?)?(?P<season>\d\d?)((?: e (?: pisode\2?)?)|x)?(?P<episode>\d\d?)?(?:e\d\d?(?:-e?\d\d?)?|x\d\d?)?|(?P<year>[(\]]?\d{4}[)\]]?)))""",re.I|re.X|re.M)



# TODO
# Support The Following Formats
# Season (Roman or Normal Numerals) Episode (Roman or Normal Numerals)
# match episode in seasonxepisode

# reads episode name, season and episode from filepath, returns a class instance of
# file class on success, None on error
def isolateSE(s, separator):
    name = s.split(separator)[-1]
    name = strUtil.clean_file_name(name)
    name = re.sub(' +',' ',name)
    m = testReg.search(name)
    if m is None:
        new_name = ' '.join(s.split(separator)[-3:])
        match = re.search('season|Season|S[0-9]{1,2}E', new_name)
        if match is not None:
            new_name = strUtil.clean_file_name(new_name)
            new_name = re.sub(' +',' ',name)
            print(new_name)
            m = testReg.search(new_name)
            if m is None:
                m = romanTestReg.search(new_name)
    if m is not None:
        a = file_class.File_info(s)
        if m.group('title') is not None:
            a.set_name(str(m.group('title')))
        if m.group('season') is not None:
            a.set_season(str(m.group('season')))
        if m.group('episode') is not None:
            a.set_episode(str(m.group('episode')))
        a.set_extension(s[s.rfind('.')+1:])
        return a
            #print("title: " + str(m.group('title')))
            #print("season: " + str(m.group('season')))
            #print("episode: " + str(m.group('episode')))
            #print("-------")
    else:
        return None

def getEpisodeName(s):
    return None

f = open("downloads.txt").readlines()

l = []

#for s in f:
#    print(strUtil.clean_file_name(s))
#    isolateSE(s)
    #l.append((s, tempS, tempE, tempEN))

#print(len(f))

#for s in l:
#    print(s)
