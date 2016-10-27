#!/bin/bash
# This script erases one library. Only execute if you are sure about it
read -p "Library name: " library

rm -r ~/corpus/train/$library
rm -r ~/corpus/train/$library"_nlm"
rm -r ~/corpus/testc/$library
rm -r ~/corpus/testc/$library"_nlm"
