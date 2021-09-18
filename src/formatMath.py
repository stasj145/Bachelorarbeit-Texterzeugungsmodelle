import io
import re

fileName="../data/algebra_linear_1d.txt"
stopAfterNExamples=200000
rePattern='^Solve\s([\S\s]+)\sfor\s(\w)\.$'

f=open(fileName)
lines = f.readlines()
f.close()
print(len(lines))

se, f, s, e = "<|startoftext|>\n[EQUATION]: ", "\n[SOLVEFOR]: ", "\n[SOLUTION]: ", "<|endoftext|>\n"

newF = io.open("mathDataset.txt", "w+", encoding="utf-8")
cont=True

index=0
while(index+2 < len(lines) and cont):
    data = se
    line=lines[index]
    match = re.match(rePattern, line)
    data += str(match.group(1))
    data += f
    data += str(match.group(2))
    index+=1
    line=lines[index]
    data += s
    data += str(line)
    data += e
    newF.write(data)
    index+=1
    print(index)
    if index/2 > stopAfterNExamples:
        cont=False
newF.close()



