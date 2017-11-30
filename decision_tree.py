from sklearn import tree
import pandas as pd
from sklearn.datasets import load_iris
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'


def tree_to_pseudo(tree, feature_names):

    '''
    Outputs a decision tree model as if/then pseudocode
    
    Parameters:
    -----------
    tree: decision tree model
        The decision tree to represent as pseudocode
    feature_names: list
        The feature names of the dataset used for building the decision tree
    '''

    left = tree.tree_.children_left
    right = tree.tree_.children_right
    threshold = tree.tree_.threshold
    features = [feature_names[i] for i in tree.tree_.feature]
    value = tree.tree_.value

    def recurse(left, right, threshold, features, node, depth=0):
        indent = "  " * depth
        if (threshold[node] != -2):
            print (indent,"if ( " + features[node] + " <= " + str(threshold[node]) + " ) {")
            if left[node] != -1:
                recurse (left, right, threshold, features, left[node], depth+1)
                print (indent,"} else {")
                if right[node] != -1:
                    recurse (left, right, threshold, features, right[node], depth+1)
                print (indent,"}")
        else:
            print (indent,"return " + str(value[node]))

    recurse(left, right, threshold, features, 0)

#-----------------------------------------------------

data = pd.read_csv(open('iris.data'))
target = data['target']
del data['target']


#print(data)
#print(target)

#clf = DecisionTreeClassifier(criterion = "entropy", random_state = 100, max_depth=3, min_samples_leaf=5)
#clf.fit(data, target)

#iris = load_iris()
clf = tree.DecisionTreeClassifier(criterion = "entropy")
clf = clf.fit(data, target)

#import graphviz
dotfile = open("dtree3.dot", 'w')
tree.export_graphviz(clf, out_file = dotfile, feature_names = data.columns, class_names = ['Iris-setosa','Iris-versicolor','Iris-virginica'])
dotfile.close()

tree_to_pseudo(clf, data.columns)