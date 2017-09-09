## Folders

## pdf/
This folder contains some pdfs downloaded from the cited databse. This could be the folder you could save your pdf files.

## train/ and testc/
This folders contain different libraries for both training and testing. Note that each library was created differently using different parameters in `move_inc.sh` or `move_ninc.sh`.

### Notation
All libraries start with the prefix _spanishlit_, which stands for (guess what) Spanish Literature. In addition, the second term refers to the nature of the division between the training and the test sets. In particular:

- *inc*: Chunks of all books in both training and test
- *ninc*: No blocks of the same book included both in training and test.

Moreover, the last term denotes the version of the training/test pair. Particularly:

- *v1*: Chunks of 10 lines, 10 books per author, 7 authors.
- *v2*: Chunks of 10 lines, 15 books per author, 7 authors. 
- *v3*: Chunks of 10 lines, 15 books per author, 8 authors.
- *v4*: Chunks of 25 lines, 15 books per author, 8 authors.
- *v4*: Chunks of 50 lines, 15 books per author, 8 authors.

Besides this, if the file name is followed by *_nlm*, it means that this library is prepared for the scripts implemented with NLTK.

## txt/
This folder contains some samples that were converted from pdf to txt. In particular, this folder should be the directory where the user should place all his pdf files, and execute the provided scripts `move_inc.sh` and `move_ninc.sh` found in this folder (its explanation has been written in the main README).
