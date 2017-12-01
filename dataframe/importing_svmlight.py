from sklearn.datasets import load_svmlight_file
from sklearn import svm
from sklearn.model_selection import cross_val_score

x, y = load_svmlight_file("../files/svmlight_tr")
print("x:")
print(x)
print("y:")
print(y)


clf = svm.SVC().fit(x, y)
s = clf.score(x, y)
print(str(s))


print("c fold cross validation c=5")
ss = cross_val_score(clf, x, y, cv=5, scoring='accuracy')
print(str(ss))
