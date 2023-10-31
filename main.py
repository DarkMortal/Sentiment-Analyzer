import string
from collections import Counter
import matplotlib.pyplot as plt

# text pre-processing
text = open('./data/read.txt',encoding='utf-8').read()
lower_case = text.lower()
cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))
tokenized_words = cleaned_text.split()

# load stop-words
stop_words = []
with open('./data/stop_words.txt') as file:
    for line in file:
        words = line.split(',')
        stop_words.append(words)

# remove stop-words
tokenized_words = list(filter(lambda w: w not in stop_words, tokenized_words))

emotion_list = []
with open('./data/emotion.txt') as file:
    for line in file :
        clear_line = line.replace('\n','').replace(',','').replace("'",'').strip()
        word, emotion = clear_line.split(':')

        if word in tokenized_words:
            emotion_list.append(emotion)

w = Counter(emotion_list)
fig, ax1 = plt.subplots()
ax1.bar(w.keys(),w.values())
fig.autofmt_xdate()
plt.savefig('./results/graph.png')