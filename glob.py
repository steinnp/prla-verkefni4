import glob

f = glob.glob("downloads/**/*.*",recursive=True)
for x in f:
    print(x)
