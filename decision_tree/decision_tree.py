from sklearn import tree
import pandas as pd
import os

'''
    this script contains some utils for decision trees on sklearn
        tree_to_dot:
            it obtains .dot script for graphviz
        tree_to_pseudo:
            it prints the tree in if/then rules on terminal     
'''

def tree_to_dot(file, classifier, columns, classes):
    #on win sy:
    os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
    dotfile = open(file, 'w')
    tree.export_graphviz(classifier, out_file = dotfile, feature_names = columns, class_names = classes)
    dotfile.close()

def tree_to_pseudo(tree, feature_names):
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

if __name__ == "__main__":
    
    data = pd.read_csv(open('../files/iris.data'))
    targets = data.target.unique()
    target = data['target']
    del data['target']
    clf = tree.DecisionTreeClassifier(criterion = "entropy")
    clf = clf.fit(data, target)
    
    tree_to_dot('../files/dotfile.dot', clf, data.columns, targets)
    #tree_to_pseudo(clf, data.columns)
    
    