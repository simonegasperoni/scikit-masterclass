import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.model_selection import cross_val_score

#pandas csv handler
#df: data frame

############## corpus  leggero corte dei conti:ccml_ts4kfoldcsv.csv
df = pd.read_csv('C:/Users/s.gasperoni/Desktop/ccml_ts4kfoldcsv.csv', sep=',')
corpus = list(df.parag)
target = list(df.targ)
#print(lista[0])

#sklearn
vectorizer = CountVectorizer(min_df=1)
m = vectorizer.fit_transform(corpus)

#size of sparse matrix (vectorized corpus)
print("------------------------------------------------------")
print("before CHI-SQUARE selection")
print("------------------------------------------------------")
print("dim(sparse): " + str(m.shape))
print("dim(target): " + str(len(target)))
print("------------------------------------------------------")

ch2 = SelectKBest(chi2, k=2500)
newcorpus = ch2.fit_transform(m, target)

#size of sparse matrix (vectorized corpus)
print("------------------------------------------------------")
print("after CHI-SQUARE selection")
print("------------------------------------------------------")
print("dim(sparse): " + str(newcorpus.shape))
print("dim(target): " + str(len(target)))
print("------------------------------------------------------")

#training on bayes
print("------------------------------------------------------")
print("BAYES")
print("------------------------------------------------------")
from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB()
clf.fit(newcorpus, target)
scores = cross_val_score(clf, newcorpus, target, cv=10)
print(scores)

#training on sgd
print("------------------------------------------------------")
print("SGD")
print("------------------------------------------------------")
from sklearn.linear_model import SGDClassifier
clf2 = SGDClassifier(loss="hinge", penalty="l2")
clf2.fit(newcorpus, target)
scores2 = cross_val_score(clf2, newcorpus, target, cv=10)
print(scores2)

#trainig on SVR (svm regression)
print("------------------------------------------------------")
print("SVM-LinearSVC")
print("------------------------------------------------------")
from sklearn import svm
clf3 = svm.LinearSVC()
clf3.fit(newcorpus, target)
scores3 = cross_val_score(clf3, newcorpus, target, cv=10)
print(scores3)
