import jieba
import json
import string

data = json.load(open('output.json'))
print('start split')


def split(question):
    print(question["answer"].translate([None, b'，。？']))
    split_question = {
        'answer': list(jieba.cut(question["answer"].translate(string.punctuation), cut_all=False)),
        'title': list(jieba.cut(question["title"].strip(), cut_all=False))
    }
    print(split_question)

    return split_question

# split_data = list(map(split, data))
split_data = split(data[0])
print(split_data)
