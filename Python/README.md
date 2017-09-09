# Python Implementation #

This folder contains the python scripts to evaluate our spanish 
literature works classifier. For the moment, the considered techniques 
are:

- *Naive Bayes Classifier* (`test1.py`and `test2.py`)
- *Support Vector Machine* (`test3.py`and `test4.py`)
- *Multilayer Perceptron* (`test5.py`), *in development*
- *Natural Language Modeling, Ngrams* (`test6.py`)

## Execution and save results
- Folder `results` contains the results for the executions of the aforementioned techniques.
- For new executions, create directory in folder results (`vX`), typically associated with a library version X

Run the following lines to create a new directory called `directory` in results and store the results generated when using test2.py

```
python -u test2.py | tee results/directory
```
