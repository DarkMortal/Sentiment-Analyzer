import string
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
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

        emotion_list = {}
        with open('./data/emotion.txt') as file:
            for line in file :
                clear_line = line.replace('\n','').replace(',','').replace("'",'').strip()
                word, emotion = clear_line.split(':')

                if word in tokenized_words:
                    if emotion in emotion_list.keys():
                        emotion_list[emotion] += tokenized_words.count(word)
                    else: emotion_list[emotion] = tokenized_words.count(word)

        return emotion_list

    def generatePlot(self, data, graphOptions):
        graph = None

        figure, axis = plt.subplots(
            facecolor = graphOptions.get('faceColor'),
        )
        if graphOptions.get('isHorizontal'):
            graph = axis.barh(
                list(data.keys()),
                list(data.values()),
                color = graphOptions.get('graphColor')
            )
            axis.xaxis.set_ticks(list(range(
                int(min(data.values())),
                int(max(data.values())) + 1, 1
            )))
        else:
            graph = axis.bar(
                list(data.keys()),
                list(data.values()),
                color = graphOptions.get('graphColor')
            )
            axis.yaxis.set_ticks(list(range(
                int(min(data.values())),
                int(max(data.values())) + 1, 1
            )))

        total = sum(data.values())
        
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

        # grid options
        plt.grid(visible = graphOptions.get('isAxis'),
                 axis = ('x' if graphOptions.get('isHorizontal') else 'y'))

        if graphOptions.get('showP'):
            i = 0
            for p in graph:
                width = p.get_width()
                height = p.get_height()
                x, y = p.get_xy()
                val = list(data.values())[i]
                plt.text(x + width / 2,
                        y + height * 1.01,
                        f"{round(val * 100 / total, 2)}%",
                        ha = "center",
                        weight = "bold"
                        )
                i += 1
        return figure