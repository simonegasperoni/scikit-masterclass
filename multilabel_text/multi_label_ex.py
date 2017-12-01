import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.multiclass import OneVsRestClassifier

X_train = np.array(["new york is a hell of a town",
                    "new york was originally dutch",
                    "the big apple is great",
                    "new york is also called the big apple",
                    "nyc is nice",
                    "people abbreviate new york city as nyc",
                    "the capital of great britain is london",
                    "london is in the uk",
                    "london is in england",
                    "london is in great britain",
                    "it rains a lot in london",
                    "london hosts the british museum",
                    "new york is great and so is london",
                    "i like london better than new york"])

y_train = [["nyc"], ["nyc"], ["nyc"], ["nyc"], ["nyc"], ["nyc"], ["lon"],
     ["lon"], ["lon"], ["lon"], ["lon"], ["lon"], ["nyc", "lon"],
     ["nyc", "lon"]]

X_test = np.array(['nice day in nyc',
                    'new york city',
                   'welcome to london',
                   'hello welcome to new york. enjoy it here and london too'])

from sklearn.preprocessing import MultiLabelBinarizer

classifier = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', OneVsRestClassifier(LinearSVC()))])

multilabel = MultiLabelBinarizer()
y = multilabel.fit_transform(y_train)

classifier.fit(X_train, y)
predicted = classifier.predict(X_test)

print(multilabel.inverse_transform(predicted))
