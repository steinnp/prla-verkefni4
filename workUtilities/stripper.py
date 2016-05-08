


f = open("../unknown.txt").readlines()
f = [x.split('/')[-1] for x in f]

for x in f:
    print(x)




