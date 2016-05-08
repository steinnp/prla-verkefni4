import re


romanReg = "(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})"
fileSReg = "((s|S)\d{1,2}(e|E)\d{1,2}|\d{1,2}x\d{1,2})"
testReg  = """^(?P<title>[-\w'"]+(?P<separator> [ .] )(?: [-\w'"]+\2 )*?)(?:(?:(?! \d+ \2 )(?: s (?: eason \2? )? )?(?P<season>\d\d?)(?: e (?: pisode \2? )? )?(?P<episode> \d\d? )?(?: e\d\d?(?:-e?\d\d?)? | x\d\d? )?|(?P<year> [(\]]?\d{4}[)\]]? )))"""




# TODO
# Support The Following Formats
# Season (Roman or Normal Numerals) Episode (Roman or Normal Numerals)


def isolateSE(s):
	m = re.search(testReg, s)
	if m is not None:
		print(m.group(0))
		return (getSeason(m.group(0)), getEpisode(m.group(0)))

def getSeason(s):
	return 0

def getEpisode(s):
	return 0

def getEpisodeName(s):
	return None


f = open("downloads.txt").readlines()

l = []

for s in f:
	isolateSE(s)
	#tempS = getSeason(s)
	#tempE = getEpisode(s)
	#tempEN = getEpisodeName(s)
	#l.append((s, tempS, tempE, tempEN))


for s in l:
	print(s)
