#!/usr/bin/env python

#Copyright (C) 2016 Nestor Manrique
#
#Permission is hereby granted, free of charge, to any person obtaining
#a copy of this software and associated documentation files (the
#"Software"), to deal in the Software without restriction, including
#without limitation the rights to use, copy, modify, merge, publish,
#distribute, sublicense, and/or sell copies of the Software, and to
#permit persons to whom the Software is furnished to do so, subject to
#the following conditions:
#
#The above copyright notice and this permission notice shall be
#included in all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
#NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
#CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
#TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
#SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
#Except as contained in this notice, the name of the author shall
#not be used in advertising or otherwise to promote the sale, use or
#other dealings in this Software without prior written authorization
#from himself.

import sys
from bs4 import BeautifulSoup
from argparse import ArgumentParser,FileType
from PIL import Image
import urllib.request
import io.BytesIO

def question_parser_rtf(question):
    q_options =  question.find_all('p')
    parsed_q = q_options[0].get_text()+"\line\par\n"
    answers = 'Answers: '
    for x in q_options[1:]:
        if x.get_text()[:11] == 'Explanation':
            continue
        parsed_q = parsed_q+x.get_text()+"\line\par\n"
        if x.find('font', color='#333333'):
            answers=answers+x.contents[0][:-1]+', '
    parsed_q = parsed_q+answers[:-2]+'\line\par\n'
    return parsed_q

def question_parser_txt(question):
    q_options =  question.find_all('p')
    parsed_q = q_options[0].get_text()+"\n"
    answers = 'Answers: '
    for x in q_options[1:]:
        if x.get_text()[:11] == 'Explanation':
            continue
        parsed_q = parsed_q+x.get_text()+"\n"
        if x.find('font', color='#333333'):
            answers=answers+x.contents[0][:-1]+', '

def get_image_from_url(image_url):
    url_contents = urllib.request.urlopen(image_url)
    image_file = io.BytesIO(url_contents)
    im = Image.open(image_file)
    return im

def image_to_hex(image):
    hex_string='somehexstringsoon'
    return hex_string

parser = ArgumentParser(description="Generates rtf with questions from aiotestking.")
parser.add_argument('exam_code', help='Code of the exam and version (i.e. "1z0-821", "1z0-821 (v.2)")')
parser.add_argument('-f', '--output-filepath', help='especify output file name', metavar='output_filepath')
parser.add_argument('-txt', '--txt-output', action='store_true', help='outputs txt format instead of rtf (warning, txt format does not support images in questions)')

args = parser.parse_args()

exam_code=args.exam_code
output_filepath=exam_code+'.rtf'

if args.output_filepath and args.output_filepath[-4] == '.' and args.output_filepath[3:] != '.rtf':
    print('dasdasd')
    output_filepath=args.output_filepath[:-4] + '.rtf'

url_home="http://www.aiotestking.com"

page = urllib.request.urlopen(url_home)
soup = BeautifulSoup(page.read(), 'html.parser')
exam_url = soup.find('a',title=exam_code)

if not exam_url:
    print('Test code not found.')
    exit(0)

file = open(output_filepath,'w')

exam_url = exam_url['href']

exam_name = exam_url.split("category/",1)[1][:-1].replace('-',' ')
exam_url = exam_url.split("category",1)[0] + "category/single" + exam_url.split("category",1)[1]

soup = BeautifulSoup(urllib.request.urlopen(exam_url).read(), 'html.parser')
total_pages = soup.find('span',class_='pages').string[-1]
print("\nProcessing test: "+exam_name+"\n") 
print("The test has "+total_pages+" pages of questions...\n")

q_number=0

file.write("{\\rtf1\\ansi\\ansicpg1252\\deff0\\deflang1033{\\fonttbl{\\f0\\fswiss\\fcharset0 Arial;}}\n")

for i in range(2, int(total_pages)+2):
    questions = soup.find_all('div', class_='archive_post_block')
    for n,q in zip(range(q_number+1,len(questions)+q_number+1),map(question_parser_rtf,questions)):
        file.write(str(n)+'. '+q+'\line\par\n')
        #print(str(n)+'. '+q)

    q_number = q_number+len(questions)

    next_page_url=exam_url+'page/'+str(i)+'/'

    next_page = urllib.request.urlopen(next_page_url)

    soup = BeautifulSoup(next_page.read(), 'html.parser')

file.write("}}\n\x00")
file.close()
print("Questions saved in "+output_filepath)
