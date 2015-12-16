aiotestkingScrapper
==================

Scrapper for aiotestking page built in Python3 with [beautifulsoup](http://www.crummy.com/software/BeautifulSoup/).

The idea is to get all the questions, options and answers from a specified test in aiotestking and get the exam formatted in a .txt or .rtf file.

The purpose of this script is to practice web scrapping, python programming and generation of rtf files. aiotestking page has a pretty simple and standard format so it's perfect for practicing scrapping techniques.

## Installation

1. Since the script is built in Python 3 you will need to install this version of python on your system. In my case I used Python 3.4 you can download it from [here](https://www.python.org/downloads/release/python-343/) although the latest version in the time of writing this README is Python 3.5 (I didn't test the script with this version).

2. After installing Python 3 use the requirements.txt file in the repo with pip to install all the packages for the script.

3. Run the script with your Python 3 interpreter, make sure you are using the correct version looking for the default python in your path variable.

## Usage


```
usage: aiotestkingscrapper.py [-h] [-f output_filepath] [-txt] exam_code

Generates rtf with questions from aiotestking.

positional arguments:
  exam_code             Code of the exam and version (i.e. "1z0-821", "1z0-821
                        (v.2)")

optional arguments:
  -h, --help            show this help message and exit
  -f output_filepath, --output-filepath output_filepath
                        especify output file name
  -txt, --txt-output    outputs txt format instead of rtf (warning, txt format
                        does not support images in questions)
```

The only argument for the script is the exam code as it appears in the home page of aiotestking, several versions of the same exam may appear so you can especify the version like in the page as well, e.g. "1z0-821", "1z0-821 (v.2)". Right now is case sensitive so if the exam code appears like "1Z0-100" using minus z won't work.

## Script Output

The output file containing questions is a rtf file (or optionally a .txt file). Irrespective of the format, the file should consist of the following parts:

   1. An exam description located before the first question (optionally).
   2. A numbered list of questions.

Each question should consist of four parts:

   1. Question text.
   2. List of answer choices.
   3. Correct answer.

The example of an output text file for import is given below and its format is described in details.

Source File Sample

```
1. Text of the first question.

A. First choice text.
B. Second choice text.
C. Third choice text.
D. Fourth choice text.

Answer: A

2. Text of the second question.

a) First choice text.
b) Second choice text.
c) Third choice text.
d) Fourth choice text.

Answer: C, D
```

### To do list
- [x] Code an early version of the script.
- [x] Make the script available in github
- [x] Show error messages for exam codes not listed in aiotestking.
- [x] Make output go to file instead of stdout. Also add parameter to specify file path and name.
- [x] Add an option so it can output a .rtf file instead of a .txt so we can include images in questions as well.
- [ ] Support scrapping and parsing images in questions.
- [ ] Change the script so it is not case sensitive in the exam search.
- [ ] Make the script interactive and design a menu to list the exam codes and names of the tests for a specific vendor, e.g. Oracle, Cisco, etc (kind of like is organized in the home page of aiotestking).
- [ ] Make the script python 2 compatible or turn it to binary with pyinstaller or cx_freeze.

=======

Copyright (C) 2016 Nestor Manrique

This software is published under the [X11 License](http://www.gnu.org/licenses/license-list.html#X11License) which is compatible with the GNU GPL.
