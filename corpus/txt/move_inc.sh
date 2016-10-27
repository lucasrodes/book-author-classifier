#!/bin/bash

for f in *.pdf; do pdftotext "$f"; done 
mv *.pdf test

# Define the name of the library
read -p "Library name: " library
if [ ! -e ~/corpus/train/$library ]; then mkdir ~/corpus/train/$library; fi;
echo "> Create train library... Done!"
if [ ! -e ~/corpus/testc/$library ]; then mkdir ~/corpus/testc/$library; fi;
echo "> Create test library... Done!"
# Define size of the chunks (in number of lines)
read -p "Chunk size (lines): " chunklines
#read -p "Number of authors: " numberauthor
numberauthor=6
#read -p "Folder name to save chunks: " folder

for run in {1..8}; do
	read -p "Author name: " author
	authorlabel=${author,,}
	#authorlabel=("$author" | awk '{print tolower($0)}')
	echo $authorlabel
	#read -p "Author label: " authorlabel
	if [ ! -e ~/corpus/train/$library/$authorlabel ]; then mkdir ~/corpus/train/$library/$authorlabel; fi;
	echo "> Create author label directory in train library... Done!"
	if [ ! -e ~/corpus/testc/$library/$authorlabel ]; then mkdir ~/corpus/testc/$library/$authorlabel; fi;
	echo "> Create author label directory in test library... Done!"
	var=0
	# Split all files
	for filename in $author*; do 
		# Show file name
	#	ls -lG
		((var=var+1))	
		echo $filename; 
		chunkprefix=$authorlabel$var
		#read -p "Prefix name of chunks:  " chunkprefix
		split -l $chunklines -a 3 "$filename" $chunkprefix #~/corpus/train/$library/$authorlabel/$chunkprefix
		echo "> Split Document... Done!"
		# Count number of fiels
		a=$(ls $authorlabel* -l | egrep -c '^-')
		#a=$(ls -l ~/corpus/train/$library/$authorlabel/. | egrep -c '^-')
		b=$(($a*1/4))
		#read -p "Press Enter " enter
		ls $authorlabel* |sort -R |tail -$b |while read f; do
		#ls ~/corpus/train/$library/$authorlabel/* |sort -R |tail -b |while read f; do
			#echo $f
			mv "$f" ~/corpus/testc/$library/$authorlabel/
			#mv $filee ~/corpus/txt/test/trying
		done
		mv $authorlabel* ~/corpus/train/$library/$authorlabel/

		echo "> Store test and train samples... Done!"
		# Show number of files
		#cd $folder
		#if [ ! -e training ]; then mkdir training; fi;
	
		#ls -l . | egrep -c '^-'
		#read -p "Number of files: " N
		#ls |sort -R |tail -1000 |while read file; do
    	
		# Something involving $file, or you can leave
    		# off the while to just get the filenames
    		#if [[ "$file" != "training" ]]; then
        	#echo "different from training"
        	#	if [[ "$file" != "move.sh" ]]; then
        	        	#echo "different from move"
	        #                mv $file training/
	        #	fi
	    	#fi
		#done

		#if [ ! -e test ]; then mkdir test; fi;
		#mv $chunkprefix* test/
		#cd ..

	
	done;
	
	for file in ~/corpus/train/$library/$authorlabel/*
	do
	#        echo "hola" 
        	mv "$file" "$file.txt"
	done
	echo "> Train samples in txt format... Done!"

	for file in ~/corpus/testc/$library/$authorlabel/*
	do
	#        echo "hola" 
        	mv "$file" "$file.txt"
	done
	echo "> Test samples in txt format... Done!"

done;


#for file in ~/corpus/$library/$authorlabel/*; do
#    mv "$file" "`basename $file`.txt"
#done
echo "> Process finished... Done!"

#cd ~/corpora/txt
