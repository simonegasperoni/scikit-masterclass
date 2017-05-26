from sklearn import datasets
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier

# load the iris datasets
dataset = datasets.load_iris()

# fit a CART model to the data
model = DecisionTreeClassifier()
model.fit(dataset.data, dataset.target)
print(dataset.data)
print(dataset.target)

print("dataset.data length: " + str(len(dataset.data)))
print("dataset.target length: " + str(len(dataset.target)))

print(model)

# make predictions
expected = dataset.target
predicted = model.predict(dataset.data)

# summarize the fit of the model
print("---")
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))
