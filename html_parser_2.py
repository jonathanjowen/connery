#!/bin/python3

import re
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
  
    def handle_comment(self, data):
        if bool(re.search(r'\n', data)):
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data)
  
    def handle_data(self, data):
        if bool(re.search(r'^[\n]+$', data)) is not True:
            data = re.sub(r'\n', 'linefeed', data)
            print(">>> Data")
            print(data)
    
if __name__ == '__main__':
    html = ''       
    for i in range(int(input())):
        html += input().rstrip()
        html += '\n'

    parser = MyHTMLParser()
    parser.feed(html)
    parser.close()
               

# https://www.hackerrank.com/challenges/html-parser-part-2/problem