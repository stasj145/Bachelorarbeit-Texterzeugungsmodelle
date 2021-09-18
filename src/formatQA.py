import pandas
import io
colnames = ['csvindex', 'text', 'questions', 'id', "answer_start", "answers"]
data = pandas.read_csv('../data/SQuAD_csv.csv', names=colnames)


text=data.text.tolist()
questions=data.questions.tolist()
answers=data.answers.tolist()
c, q, a, e = "<|startoftext|>\n[CONTEXT]: ", "\n[QUESTION]:", "\n[ANSWER]:", "\n<|endoftext|>\n"

f = io.open("QAdataset.txt", "w+", encoding="utf-8")

index = 1
while(index<len(text)):
    dataset = ""
    dataset+=c+text[index]

    dataset+=q+questions[index]
    dataset+=a+answers[index]+e
    index+=1
    f.write(dataset)
    print(index)


f.close()