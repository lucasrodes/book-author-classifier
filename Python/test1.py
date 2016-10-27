# -*- coding: utf-8 -*- 

# Naive Bayes Classifier, Ocurrancy of words

# Import all libraries, including the countvectorizer and the naive bayes classifier
from sklearn.datasets import load_files
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import subprocess
import os

# Save output file
#save = raw_input('Save the results in a file? [y/n] ')
#script = os.path.basename(__file__)
#print script
#if save =='y':
#	fileName = raw_input('File Name to save')
#	f = open("test.out", 'w')
#	with open(fileName, "w+") as output:
#		subprocess.call(["python", script], stdout=output);
#	sys.stdout = f

# Print details of this script
print "Naive Bayes Classifier, Occurancy of words"
print "******************************************"
print " "

# Dictionary containing the paths of the training (as key) and test (as value): {train1:test1, train2:test2}
version = raw_input('Which library version do you want to import? ')
files = {'/corpus/train/spanishlit_ninc_v'+version: ['/corpus/testc/spanishlit_ninc_v'+version, 'Not all books in training corpus'],
	'/corpus/train/spanishlit_inc_v'+version: ['/corpus/testc/spanishlit_inc_v'+version, 'All books in training corpus']}

#files2 = {'/veu4/usuaris30/speech00/corpus/testc/spanishlit_ninc_v1' : 'Test Books not included in training','/veu4/usuaris30/speech00/corpus/testc/spanishlit_inc_v1':'Test Books included in ttraining'}

# All possible labels, except for 'becquer'
all_categ = ['calderon', 'cervantes', 'garcia', 'lope', 'perez', 'pardo','quevedo']

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

		
		# Turn the training data into a sparse matrix of word occurencies
		vectorizer = CountVectorizer()
		X_train = vectorizer.fit_transform(text_train_subset.data)
		# Obtain the targets, i.e. the considered categories
		y_train = text_train_subset.target

		# Train the Naive Bayes Classifier
		classifier = MultinomialNB().fit(X_train, y_train)

		# LOAD THE TEST CORPUS
		text_test_subset = load_files(files[file][0], description = 'Test: Some extracts of spanish literature books', 
			categories = categ, load_content = True, encoding = 'utf-8', shuffle = False)

		# Obtain sparse matrix of word occurancies of the data and the detected targets
		X_test = vectorizer.transform(text_test_subset.data)
		y_test = text_test_subset.target

		# Print the considered categories
		print "> Categories:", categ
		# Print the performance of the classifier
		print("> Testing score: {0:.1f}%".format(classifier.score(X_test, y_test) * 100))

#f.close()
