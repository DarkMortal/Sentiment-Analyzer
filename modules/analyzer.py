import string
from collections import Counter
import matplotlib.pyplot as plt
from re import compile, UNICODE as ARGS

graphColor = (31.0/255.0, 117.0/255.0, 254.0/255.0, 1)

class Analyzer:

    def __init__(self):
        
        # load stop-words
        self.stop_words = []

        with open('./data/stop_words.txt') as file:
            for line in file:
                words = line.split(',')
                self.stop_words.append(words)

        self.emoji_filter = compile("["
            u"\U0001F600-\U0001F64F"  # emoticons
            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
            u"\U0001F680-\U0001F6FF"  # transport & map symbols
            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        "]+", flags = ARGS)

    def analyze(self, text):

        # text pre-processing
        lower_case = text.lower()
        lower_case = self.emoji_filter.sub(r'', lower_case)
        cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))
        tokenized_words = cleaned_text.split()

        # remove stop-words
        tokenized_words = list(filter(lambda w: w not in self.stop_words, tokenized_words))

        emotion_list = []
        with open('./data/emotion.txt') as file:
            for line in file :
                clear_line = line.replace('\n','').replace(',','').replace("'",'').strip()
                word, emotion = clear_line.split(':')

                if word in tokenized_words:
                    for i in range(tokenized_words.count(word)):
                        emotion_list.append(emotion)

        emotion_list = Counter(emotion_list)
        figure, axis = plt.subplots()
        axis.bar(
            emotion_list.keys(),
            emotion_list.values(),
            color = graphColor
        )
        figure.autofmt_xdate()
        return figure