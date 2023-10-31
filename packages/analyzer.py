import string
from collections import Counter
import matplotlib.pyplot as plt

class Analyzer:

    def __init__(self):
        
        # load stop-words
        self.stop_words = []

        with open('./data/stop_words.txt') as file:
            for line in file:
                words = line.split(',')
                self.stop_words.append(words)

    def analyze(self, text):

        # text pre-processing
        lower_case = text.lower()
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
                    emotion_list.append(emotion)

        w = Counter(emotion_list)
        fig, ax1 = plt.subplots()
        ax1.bar(w.keys(),w.values())
        fig.autofmt_xdate()
        return fig