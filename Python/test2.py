# -*- coding: utf-8 -*- 

# Naive Bayes Classifier, Frecuency of words/Word Occurancy, Using Pipeline

# Import all libraries, including the countvectorizer and the naive bayes classifier
from sklearn.datasets import load_files
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
# New libraries: Pipeline to easily define a classifier and TfidTransformer to manipulate frequency of words. Also numpy for some vector calculus.
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
import numpy as np

# Print details of this script
print "Naive Bayes Classifier"
print "**************************************"
print " "

# Dictionary containing the paths of the training (as key) and test (as value): {train1:test1, train2:test2}
version = raw_input('Which library version do you want to import? ')
files = {'/veu4/usuaris30/speech00/corpus/train/spanishlit_ninc_v'+version:
			 ['/veu4/usuaris30/speech00/corpus/testc/spanishlit_ninc_v'+version, 'Not all books in training corpus'],
	'/veu4/usuaris30/speech00/corpus/train/spanishlit_inc_v'+version: ['/veu4/usuaris30/speech00/corpus/testc/spanishlit_inc_v'+version, 'All books in training corpus']}


# Definition of the classifier using Pipeline
inp = int(raw_input('Word occurancy/Word frequency (0/1)? '))
if inp == 0:
	classifier = Pipeline([('vect', CountVectorizer()),('clf', MultinomialNB())])
elif inp == 1:
	classifier = Pipeline([('vect', CountVectorizer()),('tfidf', TfidfTransformer()),('clf', MultinomialNB())])

# All possible labels, except for 'becquer'
all_categ = ['calderon', 'cervantes', 'garcia', 'lope', 'perez', 'pardo', 'quevedo']

# Iterate for all train-test pair
for file in files:
	print "-----------------------------"
	print files[file][1]

	# Initial considered category
	categ = ['becquer'] 
	
	# In each iteration the number of considered categories increase and thus does the complexity of the classifier 
	for newcateg in all_categ:
		# Add new category
		categ.append(newcateg)

		# LOAD THE TRAINING CORPUS
		text_train_subset = load_files(file, description = 'Training: Some extracts of spanish literature books', 
			categories = categ, load_content = True, encoding = 'utf-8', shuffle = False)

		# Train the Naive Bayes classifier with the training set (data and labels)
		classifier = classifier.fit(text_train_subset.data, text_train_subset.target)

		# LOAD THE TEST CORPUS
		text_test_subset = load_files(files[file][0], description = 'Test: Some extracts of spanish literature books', 
			categories = categ, load_content = True, encoding = 'utf-8', shuffle = False)

		# Print the considered categories
		print "> Categories:", categ
		# Print the performance of the classifier using the test set (data and labels)
		print("> Testing score: {0:.1f}%".format(classifier.score(text_test_subset.data, text_test_subset.target) * 100))

# Prediction of the test label according to the classifier
# predicted = classifier.predict(X_test)
# A way to compute the classifier score
# print "Testing score:", np.mean(predicted == y_test)
