# -*- coding: utf-8 -*- 

# Natural Language Model to classify texts. 
# In this example we just consider the language model (LM) of Becquer and a set of given test samples

# Import nltk libraries
import nltk
from nltk.probability import LidstoneProbDist, WittenBellProbDist
from nltk.model import NgramModel
# Import io and os for managing files
import io
import os
# Import pandas to display disctionaries in dataframe format
import pandas as pd

version = str(raw_input('Which library version do you want to import? '))
        
N = int(raw_input('Choose N value for the Ngram: '))

all_categ = ['calderon', 'cervantes', 'garcia', 'lope', 'perez', 'pardo','quevedo']
print "> Define categories... Done!"


# Initialize dictionary containing the language models
lm = dict()
# Obtain the Language Models for each category    
for categ in all_categ:

    # Read file
    f = io.open('corpus/train/spanishlit_ninc_v'+version+'_nlm/'+categ+'.txt',encoding='utf8')
    g = f.read().lower()
    # Obtain tokenized words
    train = nltk.word_tokenize(g)
    
    # Remove rare words from the corpus
    # fdist = nltk.FreqDist(w for w in train)
    # vocabulary = set(map(lambda x: x[0], filter(lambda x: x[1] >= 5, fdist.iteritems())))
    # train1 = map(lambda x: x if x in vocabulary else "*unknown*", train)
    
    # Obtain the Language Model using LidstoneProbDist to smooth unseen events
    estimator = lambda fdist, bins: LidstoneProbDist(fdist, 0.2) 
    lm[categ] = NgramModel(N, train, estimator=estimator)
    
    print "> Obtain language model of",categ,"... Done!"
print "> Obtain all language models... Done!"

# Load dictionary with: {category:tests}
n_categ = dict()
test_corpus = dict()
for categ in all_categ:
    files = os.listdir('/veu4/usuaris30/speech00/corpus/testc/spanishlit_ninc_v'+version+'_nlm/'+categ)
    n_categ[categ] = len(files)
    tests = []
    for fi in files:
        f = io.open('/veu4/usuaris30/speech00/corpus/testc/spanishlit_ninc_v'+version+'_nlm/'+categ+'/'+fi, encoding='utf8')
        g = f.read().lower()
        tests.append(nltk.word_tokenize(g))
    test_corpus[categ] = tests
print "> Load test files... Done!"

# Define classification matrix of TP, FP, FN etc.
cmatrix = dict()
for categ1 in all_categ:
    cmatrix[categ1] = dict()
    for categ2 in all_categ:
        cmatrix[categ1][categ2] = 0
print "> Initialize classification matrix with value zero... Done!"
    
# Fullfil the classification matrix
ppl = dict()
for categ, tests in test_corpus.iteritems():
    # Iterate over all tests from a certain category
    for test in tests:
        # Obtain perplexity of the test according to all category's LMs
        for cat in all_categ:
            try:
                ppl[cat] = lm[cat].perplexity(test)
            except:
                print "Error in: true: ",categ+", Evaluated as:",cat," (ignored)"
        # Obtain the category of the test according to perplexity measure
        assigned_categ = min(ppl, key=ppl.get)
        # Increment corresponding value in the matrix
        cmatrix[categ][assigned_categ]+=1
    print "> Classification of tests from category",categ,"... Done!"
print "> Fulfill the classification matrix... Done!"
print "Classification matrix (row: real, column: estimated):"
print pd.DataFrame(cmatrix).transpose() 

# Fullfil the metric matrix (recall, precission, f1)
mmatrix = dict()
mmatrix['Recall'] = dict()
mmatrix['Precission'] = dict()
mmatrix['F1 score'] = dict()
mmatrix['Support']= n_categ
for categ in all_categ:
    mmatrix['Recall'][categ] = cmatrix[categ][categ]/float(sum(cmatrix[categ].values()))
    mmatrix['Precission'][categ] = cmatrix[categ][categ]/float(sum(v[categ] for k,v in cmatrix.iteritems()))
    mmatrix['F1 score'][categ] = 2*(mmatrix['Recall'][categ]*mmatrix['Precission'][categ])/float((mmatrix['Recall'][categ]+mmatrix['Precission'][categ]))
print "> Initialize metric matrix for recall/precission/f1 score with value zero... Done!"
print "Metric matrix:"
mmatrix['Recall']['global'] = str(sum([k*float(l) for (k,l) in zip(mmatrix['Support'].values(),mmatrix['Recall'].values())])/float(sum(mmatrix['Support'].values())))
mmatrix['Precission']['global'] = str(sum([k*float(l) for (k,l) in zip(mmatrix['Support'].values(),mmatrix['Precission'].values())])/float(sum(mmatrix['Support'].values())))
mmatrix['F1 score']['global'] =str(sum([k*float(l) for (k,l) in zip(mmatrix['Support'].values(),mmatrix['F1 score'].values())])/float(sum(mmatrix['Support'].values())))
mmatrix['Support']['global'] = sum(mmatrix['Support'].values())
m = pd.DataFrame(mmatrix).reindex_axis(['Recall', 'Precission', 'F1 score', 'Support'], axis=1)
all_categ.append('global')
m = pd.DataFrame(mmatrix).reindex_axis(all_categ, axis=0)
print m

