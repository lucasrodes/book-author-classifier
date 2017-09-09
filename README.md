# Book-Author-classification

Book-Author-classification is a project based on python and bash to classift book fragments. We have used spanish literature books. We have used different classifiers and different trainig/test data distribution strategies.

The project started in May 2016 by [lucasrodes](https://github.com/lucasrodes) and Sergi Liesegang and is distributed under the GPL-3.0 license.

⭐️ Please star our project if you found it interesting to keep us motivated 😃!

---

For more information, feel free to read the our [report](report.pdf).

## Idea
The idea is as follows:

- **Goal**: Given a text (i.e. long string of characters) we have to find its author. This can be relevant when the text is 
unclassified due to historical reasons (e.g. Shakespeare and Cervantes). Also, it may be useful for detecting the features of an author (e.g. epoch, style, nationality...).
- **Preparing the dataset**: First, we choose some authors. Next, we get their works and split them into small chunks. Each chung is labelled with the author that wrote it. This way, we are able to build a dataset suitable for a supervised learning approach. This dataset is then splitted into training and test sets.
- **Training and testing the model**: We propose different supervised approaches. We train our model using the training set and evaluate its performance on the test set.


## Folders/Files:

- **python**: This folder contains all the python files which implement the different classifiers. Find more information [here](python/README.md).
- **corpus**: Folder containing different files used. Find more information [here](corpus/README.md).
- **report.pdf**: Report of this project. Read it to see our results and conclusions.

## Training:
To prepare the training and test sets follow this procedure:

1. Download books in pdf from [this library](http://www.edu.mec.gub.uy/biblioteca_digital/libros/) and save them in ~/corpus/pdf.
2. Convert the PDFs in chunks of plain text files. This can be done using the scripts `move_inc.sh` or `move_ninc.sh` (depending on the approach) located in ~/corpus/txt. More information [here](corpus/README.md)
	- Run `bash move_inc.sh` to obtain fragments of all the books in both test and training. 
	- Run `bash move_ninc.sh` to obtain fragments of some books in test and some others in the training (proportion test:train, 3:10).
	- **Note**: This will remove the pdf files (if you don't wish so, please modify the first lines of the scripts).
	
## Critical issues	
- Do not change the names of the folders, this could provoke problems in the code.
- However, you should change the paths in the bash scripts according to where the project is located (this includes `move_inc-sh` and `move_ninc.sh`).
- Also change the paths from the python scripts according to the location of the test and training libraries.
- PDF files should begin with the name of the author (or last name etc.)
- If you add new authors to the library, update the python files accordingly.

## Requirements

### [NLTK](http://www.nltk.org/book/)
- This is a Natural Language toolkit developed Team NLTK.
- For us, [Chapter 6](http://www.nltk.org/book_1ed/ch06.html) is interesting
- Cool resource: [Demo Corpora (Text Collections Ready for Use)](http://dhresourcesforprojectbuilding.pbworks.com/w/page/69244469/Data%20Collections%20and%20Datasets)
- Interesting database [txtLAB450 - A Multilingual Data Set of Novels for Teaching and Research](https://ndownloader.figshare.com/files/3686778)
- [Associated labeling](https://ndownloader.figshare.com/files/3686805)  
- [Index of /biblioteca_digital/libros](http://www.edu.mec.gub.uy/biblioteca_digital/libros/)

## Colaborate
Please report to issues if you find any bug. I will be happy to assist you!
