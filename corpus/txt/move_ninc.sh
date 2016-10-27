#!/bin/bash

# Convert all pdf books into txt
for f in *.pdf; do pdftotext "$f"; done 
# Remove the pdf files from this directory
mv *.pdf test

# Prompt user for library name
read -p "Library name: " library
# Create folder associated with the library both in train and test directories
if [ ! -e ~/corpus/train/$library ]; then mkdir ~/corpus/train/$library; fi;
echo "> Create train library... Done!"
if [ ! -e ~/corpus/testc/$library ]; then mkdir ~/corpus/testc/$library; fi;
echo "> Create test library... Done!"

# Create NLM train and test sets
if [ ! -e ~/corpus/train/$library"_nlm" ]; then mkdir ~/corpus/train/$library"_nlm"; fi;
echo "> Create train NLM library... Done!"
if [ ! -e ~/corpus/testc/$library"_nlm" ]; then mkdir ~/corpus/testc/$library"_nlm"; fi;
echo "> Create test NLM library... Done!"

# Size of the chunks after splitting files
read -p "Chunk size (lines): " chunklines

## declare an array variable
declare -a arr=("Becquer" "Calderon" "Cervantes" "Garcia" "Lope" "Quevedo" "Perez" "Pardo")

for author in "${arr[@]}"; do
	# Prompt user for Author name
	# read -p "Author name: " author
	# Convert name to lower case
	authorlabel=${author,,}
	echo $authorlabel
	
	# Create directories of the specific author in the library directory (train and test)
	if [ ! -e ~/corpus/train/$library/$authorlabel ]; then mkdir ~/corpus/train/$library/$authorlabel; fi;
	echo "> Create author label directory in train library... Done!"
	if [ ! -e ~/corpus/testc/$library/$authorlabel ]; then mkdir ~/corpus/testc/$library/$authorlabel; fi;
	echo "> Create author label directory in test library... Done!"
	
	# Counter variable
	var=0
	# Split all files
	for filename in $author*; do 

		((var=var+1))	
		echo $filename; 
		chunkprefix=$authorlabel$var

		# TEST
		if [[ $var>4 ]]; then
			split -l $chunklines -a 2 "$filename" ~/corpus/testc/$library/$authorlabel/$chunkprefix
			echo "> Split Document in test... Done!"
		fi;
		
		# TRAIN
		if [[ $var<5 ]]; then
			split -l $chunklines -a 2 "$filename" ~/corpus/train/$library/$authorlabel/$chunkprefix
			echo "> Split Document in training... Done!"
			cp "$filename" ~/corpus/train/$library"_nlm"/$chunkprefix
			echo "> Copy Document in training NLM... Done!"
		fi;
	
	done;
	
	# Convert to .txt
	for file in ~/corpus/train/$library/$authorlabel/*
	do
        	mv "$file" "$file.txt"
	done
	echo "> Train samples in txt format... Done!"

	for filee in ~/corpus/testc/$library/$authorlabel/*
	do
        	mv "$filee" "$filee.txt"
	done
	echo "> Test samples in txt format... Done!"

	# Unify documents in NLM library
	cat ~/corpus/train/$library"_nlm"/$authorlabel* > $authorlabel.txt
	rm ~/corpus/train/$library"_nlm"/$authorlabel*
	mv $authorlabel.txt ~/corpus/train/$library"_nlm"/$authorlabel.txt
	echo "> Unify all author books into one long .txt... Done!"
	#rm ~/corpus/testc/$library/$authorlabel/$authorlabel"1"*

done;



cp -r ~/corpus/testc/$library ~/corpus/testc/$library"_nlm"
echo "> Process finished... Done!"

#cd ~/corpora/txt

# Check duplicates
#diff -srq ~/corpus/train/spanishlit_ninc_v3/becquer/ ~/corpus/testc/spanishlit_ninc_v3/becquer/ | grep idèntics
#diff -srq ~/corpus/train/spanishlit_inc_v1/calderon/ ~/corpus/testc/spanishlit_inc_v1/calderon/ | grep idèntics
#diff -srq ~/corpus/train/spanishlit_ninc_v1/cervantes/ ~/corpus/testc/spanishlit_ninc_v1/cervantes/ | grep idèntics
#diff -srq ~/corpus/train/spanishlit_ninc_v1/garcia/ ~/corpus/testc/spanishlit_ninc_v1/garcia/ | grep idèntics
#diff -srq ~/corpus/train/spanishlit_ninc_v1/lorca/ ~/corpus/testc/spanishlit_ninc_v1/lorca/ | grep idèntics
#diff -srq ~/corpus/train/spanishlit_ninc_v1/pardo/ ~/corpus/testc/spanishlit_ninc_v1/pardo/ | grep idèntics
#diff -srq ~/corpus/train/spanishlit_ninc_v1/perez/ ~/corpus/testc/spanishlit_ninc_v1/perez/ | grep idèntics
