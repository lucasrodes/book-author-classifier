# Python Implementation #

This folder contains the python scripts to evaluate our spanish 
literature works classifier. For the moment, the considered techniques 
are:

## Notation
- *Naive Bayes Classifier* (`test1.py`and `test2.py`)
- *Support Vector Machine* (`test3.py`and `test4.py`)
- *Multilayer Perceptron* (`test5.py`), in development
- *Natural Language Modeling, Ngrams* (`test6.py`), it promts for N value in Ngram.

## Execution and save results
- Folder results contains the results for prior executions.
- For new executions, create directory in folder results (vX), typically associated with a library version X


```
cd /veu4/usuaris30/speech00/finalproject/Python/scikit/
mkdir vX
cd ..
version=v3
python -u test2.py | tee results/vX/test2_results
python -u test2.py | tee results/vX/test2_results_nobecquer
python -u test3.py | tee results/vX/test3_results
python -u test3.py | tee results/vX/test3_results_nobecquer
python -u test4.py | tee results/vX/test4_results
python -u test4.py | tee results/vX/test4_results_nobecquer
python -u test6.py | tee results/$version/test6_results_n1
python -u test6.py | tee results/$version/test6_results_n1_nobecquer
python -u test6.py | tee results/$version/test6_results_n2
python -u test6.py | tee results/$version/test6_results_n2_nobecquer
python -u test6.py | tee results/$version/test6_results_n3
python -u test6.py | tee results/$version/test6_results_n3_nobecquer
```
