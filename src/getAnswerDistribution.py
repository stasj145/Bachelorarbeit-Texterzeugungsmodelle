fileName="../output/math7_4000steps_774M.txt"
prevLine="[SOLVEFOR]: x\n"

f=open(fileName)
lines = f.readlines()
f.close

nOfLinesFound=0
lineFound=False
distList={}


index=0
while(index < len(lines)):
    line=lines[index]
    if line == prevLine:
        nOfLinesFound+=1
        lineFound=True
        index+=1
        continue
    if lineFound:
        lineFound=False
        if line in distList:
            distList[line] += 1
        else:
            distList[line] = 1
    index+=1

print(nOfLinesFound)


for key, value in distList.items():
    print(key + str(value))
