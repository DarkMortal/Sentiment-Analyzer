import string
from collections import Counter
import matplotlib.pyplot as plt
from re import compile, UNICODE as ARGS

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

        return Counter(emotion_list)

    def generatePlot(self, data, graphOptions):
        figure, axis = plt.subplots(
            facecolor = graphOptions.get('faceColor'),
        )
        if graphOptions.get('isHorizontal'): axis.barh(
            list(data.keys()),
            list(data.values()),
            color = graphOptions.get('graphColor')
        )
        else: axis.bar(
            list(data.keys()),
            list(data.values()),
            color = graphOptions.get('graphColor')
        )

        # update graph colors
        axis.set_facecolor(graphOptions.get('background'))
        axis.tick_params(axis = 'x', colors = graphOptions.get('labelColor'))
        axis.tick_params(axis = 'y', colors = graphOptions.get('labelColor'))

        # update graph borders
        axis.spines['bottom'].set_color(graphOptions.get('borderColor'))
        axis.spines['top'].set_color(graphOptions.get('borderColor'))
        axis.spines['right'].set_color(graphOptions.get('borderColor'))
        axis.spines['left'].set_color(graphOptions.get('borderColor'))

        # axis options
        if graphOptions.get('showAxes'):
            if graphOptions.get('isHorizontal'):
                plt.ylabel("Emotions")
                plt.xlabel("Occurences")
            else:
                plt.xlabel("Emotions")
                plt.ylabel("Occurences")
        figure.autofmt_xdate()
        return figure