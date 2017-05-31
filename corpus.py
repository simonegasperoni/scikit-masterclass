import snowballstemmer
import re

#features extractor, power by snowball-stemmer
lang = 'italian'


#functional stemming
def stemm_functional(word, lang):
    stemmer = snowballstemmer.stemmer(lang)
    return stemmer.stemWord(word)


#side effect stemming
def stemm_side_effect(word, lang):
    stemmer = snowballstemmer.stemmer(lang)
    word = stemmer.stemWord(word)


#regulare exp 4 normalize
def normalize(sentence):
    normal = re.sub(r'[^\w\s]', ' ', sentence).lower()
    return normal.split()


def txt_pipe(text):
    li = normalize(text)
    li2 = []
    for entry in li:
        li2.append(stemm_functional(entry, lang))
    return li2

print(txt_pipe('prova.   Prova?età @##@[P[]@#., dda'))