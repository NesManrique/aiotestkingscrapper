aiotestkingScrapper
==================

Scrapper for aiotestking page built in Python3 with [beautifulsoup](http://www.crummy.com/software/BeautifulSoup/).

The idea is to get all the questions, options and answers from a specified test in aiotestking and get the exam formatted in a .txt or .rtf file and then import it to [Avanset VCE Exam Simulator](http://www.avanset.com/vce-simulator.html) desgining tool and finally run the test with the simulator.

The purpose of this script is to ease the process of studying with a simulator and encourage you to search for the real anwsers since, as we have seen in our own experience, the anwsers and explanations in aiotestking are mostly wrong. ***Consider yourself advice! Do not self-rekt assuming everything in that page is right.***

## Usage

./aiotestkingScrapper <exam_code>

The only argument for the script is the exam code as it appears in the home page of aiotestking, several versions of the same exam may appear so you can especify the version like in the page as well, e.g. "1z0-821", "1z0-821 (v.2)". Right now is case sensitive so if the exam code appears like "1Z0-100" using minus z won't work.

## Script Output

The output file containing questions is an usual text file (and soon well be an option with a formatted text document in RTF (Rich Text Format)). Irrespective of the format, the file should consist of the following parts:

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

The format for the exam simulator allows to add an explanation for the anwser but since answers in aiotestkings are mostly wrong, we strongly recommend you to review the questions by yourself, research the correct anwsers in the documentation of the product you are aiming a certification for, and benefit from te knowledge you will obtain with this plan of study.

### To do list
- [x] Code an early version of the script.
- [x] Make the script available in github
- [ ] Show error messages for exam codes not listed in aiotestking.
- [ ] Make the script python 2 compatible.
- [ ] Add a parameter to specify the name of an output file instead of only getting the questions data in stdout.
- [ ] Change the script so it is not case sensitive in the exam search.
- [ ] Support scrapping and parsing images in questions.
- [ ] Add an option so it can output a .rtf file instead of a .txt so we can include images in questions as well.
- [ ] Make the script interactive and design a menu to list the exam codes and names of the tests for a specific vendor, e.g. Oracle, Cisco, etc (kind of like the front page has it organized).

=======

Copyright (C) 2016 Nestor Manrique

This software is published under the [X11 License](http://www.gnu.org/licenses/license-list.html#X11License) which is compatible with the GNU GPL.
