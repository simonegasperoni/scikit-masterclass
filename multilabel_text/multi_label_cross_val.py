import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.feature_selection import SelectKBest, chi2
#from sklearn.model_selection import cross_val_score


#pandas reads on multilabel csv
df = pd.read_csv('C:/Users/s.gasperoni/Desktop/ccd_toplevel_multilabel.csv',
                    sep=';')

corpus = list(df.parag)
target = list(df.target)

lst = []
for item in target:
        lst.append(item.replace("[", "").replace("]", "").split(", "))

from sklearn.preprocessing import MultiLabelBinarizer

classifier = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('chi', SelectKBest(chi2, k=2500)),
    ('tfidf', TfidfTransformer()),
    ('clf', OneVsRestClassifier(LinearSVC()))
    ])

multilabel = MultiLabelBinarizer()
y = multilabel.fit_transform(lst)

classifier.fit(corpus, y)

X_test = np.array(['capitol vii sicurezz'])
predicted = classifier.predict(X_test)
print(multilabel.inverse_transform(predicted))

#scores = cross_val_score(classifier, corpus, y, cv=5, scoring='f1_macro')
#print(scores)