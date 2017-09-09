# Book-Author-classification#

This is the repo for a classifier of book fragments. We have used spanish literature books. We have used different classifiers and different trainig/test data distribution strategies.
For more information, read the report of our work.

## Idea
The idea would be as follows:

- **Goal**: Given a text, find its author. Relevant when the text is 
unclassified due to historical reasons (e.g. Shakespeare <-> Cervantes). 
Also, very useful for knowing the features of this author (epoch, style,
 nationality...).
- **Test**: Find the relation between the person that has written a 
certain text (observing its characteristics).
- **Training**: With a varied and large database, which will be labelled 
(assigned) to their actual authors, train the network.
- **Note**: test and training texts would not be the same. Thereby, we 
need to learn how each author writes.


## Folders/Files:

- **Report.pdf**: Report of the work, including some results and conclusions.
- **Python**: Python files implementing different classifiers. For more
details, read the README file in this folder.
- **corpus**: Folder containing different files used.
	- pdf: The PDF files of the books used.
	- train: the different libraries generated from the pdfs for the training.
	- testc: the different libraries generated from the pdfs for the test.
	- txt: PDFs converted to txt format.
	**Note**: For more information, please read the README files in this folder.

## Training:
To prepare training and test sets we have proceeded as follows:
	1. Download books in pdf from [this library](http://www.edu.mec.gub.uy/biblioteca_digital/libros/) and save them in ~/corpus/pdf.
	2. Convert the PDFs in chunks of plain text files. This can be done using the scripts `move_inc.sh` and `move_ninc.sh` located in ~/corpus/testc
		- Run `bash move_inc.sh` to obtain fragments of all the texts in both test and training. 
		- Run `bash move_ninc.sh` to obtain fragments of some books in test and the rest in training (proportion test:train, 3:10).
		**Note**: This will remove the pdf files (if you don't wish so, please modify the first lines of the scripts).
	
## Critical issues	
	- Do not change the names of the folders, this could provoke problems in the code.
	- However, you should change the paths in the bash scripts according to where the project is located (this includes `move_inc-sh`, `move_ninc.sh` and others).
	- Also change the paths from the python scripts according to the location of the test and training libraries.
	- PDF files should beguin with the name of the author (or last name etc.)
	- If you add new authors to the library, update the python files accordingly.

## Requirements

### [NLTK](http://www.nltk.org/book/)
	- This is a Natural Language toolkit developed Team NLTK.
	- For us, [Chapter 6](http://www.nltk.org/book_1ed/ch06.html) is interesting
	- Cool resource: [Demo Corpora (Text Collections Ready for Use)](http://dhresourcesforprojectbuilding.pbworks.com/w/page/69244469/Data%20Collections%20and%20Datasets)
	- Interesting database [txtLAB450 - A Multilingual Data Set of Novels for Teaching and Research](https://ndownloader.figshare.com/files/3686778)
	- [Associated labeling](https://ndownloader.figshare.com/files/3686805)  
	- [Index of /biblioteca_digital/libros](http://www.edu.mec.gub.uy/biblioteca_digital/libros/)
# book-author-classifier
