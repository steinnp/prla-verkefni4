import re
import string_utilities as strUtil


romanReg = "(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})"
fileSReg = "((s|S)\d{1,2}(e|E)\d{1,2}|\d{1,2}x\d{1,2})"
testReg = r"""^(?P<title>[-\w'"]+(?P<separator>[ .])(?:[-\w'"]+\2)*?)(?:(?:(?!\d+\2)(?:s(?:eason\2?)?)?(?P<season>\d\d?)(?: e (?: pisode\2?)?)?(?P<episode>\d\d?)?(?:e\d\d?(?:-e?\d\d?)?|x\d\d?)?|(?P<year>[(\]]?\d{4}[)\]]?)))"""



# TODO
# Support The Following Formats
# Season (Roman or Normal Numerals) Episode (Roman or Normal Numerals)


def isolateSE(s):
	#s = strUtil.clean_file_name(s)
	m = re.search(testReg, s, re.I|re.X|re.M)
	if m is not None:
		print("title: " + str(m.group('title')))
		print("season: " + str(m.group('season')))
		print("episode: " + str(m.group('episode')))
		print("-------")
	else:
		print("No Match")

def getEpisodeName(s):
	return None

f = open("downloads.txt").readlines()

l = []

for s in f:
	print(strUtil.clean_file_name(s))
	#isolateSE(s)
	#l.append((s, tempS, tempE, tempEN))

print(len(f))

for s in l:
	print(s)
