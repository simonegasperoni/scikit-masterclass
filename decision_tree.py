from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.datasets import load_iris 

iris = load_iris()
clf = DecisionTreeClassifier(criterion = "entropy", random_state = 100,
 max_depth=2, min_samples_leaf=5)
clf.fit(iris.data, iris.target)
tree.export_graphviz(clf, out_file='tree.dot')    
