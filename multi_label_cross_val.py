import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.model_selection import cross_val_score


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

X_test = np.array(['capitol vii sicurezz lavor altre provvident misur sicurezz cas risolu rapport mort od invalid perdur dirigent deriv azion delittu dann azi ragion lavor azi medesim scelt assunzion post inizial carrier appen vacant facolt dar preferent famil convivent dirigent anzidett compatibil requis professional richiest posizion concr attitudin famil dirigent dev esser assicur risc mort invalid permanent infortun seppur deriv rapin verificatis attiv lavor altra attiv arco inter giorn second condizion ordinar general polizz pattu ciascun azi capital assicur previst present contratt spes post integral caric azi beneficiar dev esser dirigent cas mort relat familiar convivent caric mancanz ered estrem conten polizz aziendal vann port conoscent dirigent indennizz corrispost dirigent forz polizz stipul sens present veng detratt azi debb eventual corrispond risarc dann cas respons infortun accert imput azi stess cas indennizz liquid compagn assicur dirigent vien consider anticip risarc dann'])
predicted = classifier.predict(X_test)
print(multilabel.inverse_transform(predicted))

#scores = cross_val_score(classifier, corpus, y, cv=5, scoring='f1_macro')
#print(scores)