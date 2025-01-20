
# Word list utils 

## Requirements
Install python 3

## Utils


### Alphabetically ordered wordle word splitter (`split`)
#### Requirements 

Have a word list of 5 letter words that is alphabetically ordered.
#### Usage
open a terminal in the project directory
run `python3 -m bin.main split <path to word list> --output-dir <path to output directory>` on mac
(or windows / linux distro equivalent)


#### Output

You can find your word list split into a .txt files for each letter of the alphabet in the output directory.


### Verify one txt to many (`verify`)
#### Requirements
already have txt files in another directory that you want to compare there words to a single file word list (usually used to confirm correct output by the split command above) 

#### Usage
open a terminal in the project directory
run `python3 -m bin.main verify <path to word list> --output-dir <path to other files dir>` on mac
(or windows / linux distro equivalent)

#### Output 

Will print to terminal 
## Contribution Guide

Feel free to add on to this... in fact any time travelers that find out cool ways to speed up reading form files feel free to put up a pr. 




