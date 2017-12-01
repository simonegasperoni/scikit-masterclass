# scikit_notes

This rep contains some notes and scripts about machine learning programming in scikit-learn, the requirements are: 
```
mkl, numpy, pandas, scipy, scikit-learn, snowballstemmer, psycopg2, beautifulsoup
```

#### scikitlearn_hello.py: hello world in sklearn

#### dataframe: pandas and svmlight data representation
* importing_svmlight.py: working on svmlight file (representation of sparse matrices)
* classify_from_csv.py: importing dataset from CSV (pandas) and feature selection by CHI-SQUARE

#### multilabel_text: multilabel text categorization
* multi_label_ex.py: an example of multi-label-text-categorization
* multi_label_cross_val.py: cross validation on multilabel training-set

#### preproc: data preprocessing and middleware 
* Extractor.py: text corpus handling with regular expression and snowball stemmer + stopwords filtering
* myparser.py: parsing with beautifulsoup
* postgres.py: psycopg2 utilities (connector postgres for python)

#### decision_tree: some utilities for decision trees
* decision_tree.py: decision tree and printing tree with graphviz and by 'if/then rules'. With graphviz is possible print the tree in '.png' by
```
dot -Tpng input.dot > output.png
```

