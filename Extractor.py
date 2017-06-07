import snowballstemmer
import re


class Extractor():
    #features extractor, power by snowball-stemmer
    #lang = 'italian'

    def __init__(self):
        self.stemmer = snowballstemmer.stemmer('italian')

    #regulare exp 4 normalize
    def normalize(self, sentence):
        normal = re.sub(r'[^\w\s]', ' ', sentence).lower()
        return normal.split()

    def stopword_filtering(self, lst):
        stopwords = set(open('stopword-list.txt', encoding='utf-8'))
        sw = list(map(lambda word: word.replace("\n", ""), stopwords))
        newlst = []
        for entry in lst:
            if entry in sw or entry.isdigit():
                pass
            else:
                newlst.append(entry)
        return newlst

    def pipe(self, text):
        #li1: corpus normalizing
        li1 = self.normalize(text)
        #li2: stopwording
        li2 = self.stopword_filtering(li1)
        #li3: stemming
        li3 = []
        for entry in li2:
            li3.append(self.stemmer.stemWord(entry))
        return li3