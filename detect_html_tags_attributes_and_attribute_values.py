#!/bin/python3

from html.parser import HTMLParser
import re



class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print("->", attr[0], '>', attr[1])
 


def read_integer():
    """Return an integer read from STDIN."""
    return(int(input()))
    


if __name__ == '__main__':
    n_of_html_lines = read_integer()
    in_comment = False
    previous_html_line = ''
    for _ in range(n_of_html_lines):
        parser = MyHTMLParser()
        html_line = previous_html_line + input()
        html_line = re.sub(r'<!--.*-->', '', html_line)
        if bool(re.search(r'<!--', html_line)):
            in_comment = True
        if in_comment is False:
            parser.feed(html_line)
        if bool(re.search(r'-->', html_line)):
            in_comment = False 
        if bool(re.search(r'[^>]$', html_line)):
            previous_html_line = html_line
        else:
            previous_html_line = ''
               
               

# https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem