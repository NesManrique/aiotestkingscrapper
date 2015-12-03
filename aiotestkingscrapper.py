#!/usr/bin/env python

import sys
from bs4 import BeautifulSoup
from argparse import ArgumentParser
import urllib.request

parser = ArgumentParser(description="Generates txt with questions from aiotestking.")
parser.add_argument('exam_code', help='Code of the exam and version (i.e. "1z0-821", "1z0-821 (v.2)")')

args = parser.parse_args()

exam_code=args.exam_code
url_home="http://www.aiotestking.com"

page = urllib.request.urlopen(url_home)
soup = BeautifulSoup(page.read(), 'html.parser')
exam_url = soup.find('a',title=exam_code)['href']

exam_name = exam_url.split("category/",1)[1][:-1].replace('-',' ')
exam_url = exam_url.split("category",1)[0] + "category/single" + exam_url.split("category",1)[1]

soup = BeautifulSoup(urllib.request.urlopen(exam_url).read(), 'html.parser')
total_pages = soup.find('span',class_='pages').string[-1]
print("\nProcessing test: "+exam_name+"\n") 
print("The test has "+total_pages+" pages of questions...\n")

q_number=0

def question_parser(question):
    q_options =  question.find_all('p')
    parsed_q = q_options[0].get_text()+"\n"
    answers = 'Answers: '
    for x in q_options[1:]:
        parsed_q = parsed_q+x.get_text()+"\n"
        if x.find('font', color='#333333'):
            answers=answers+x.contents[0][:-1]+', '
    parsed_q = parsed_q+answers[:-2]+'\n'
    return parsed_q

for i in range(2, int(total_pages)+2):
    questions = soup.find_all('div', class_='archive_post_block')
    for n,q in zip(range(q_number+1,len(questions)+q_number+1),map(question_parser,questions)):
        print(str(n)+'. '+q)

    q_number = q_number+len(questions)

    next_page_url=exam_url+'page/'+str(i)+'/'

    next_page = urllib.request.urlopen(next_page_url)

    soup = BeautifulSoup(next_page.read(), 'html.parser')
