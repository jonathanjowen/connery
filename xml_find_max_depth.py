#!/bin/python3

import sys
import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level): 
    """Track and update maximum depth while iterating through XML tree"""
    global maxdepth
    print(maxdepth, '  ' * (level+1), elem.tag)
    if (level == maxdepth):
        maxdepth += 1
    for child in elem:
        depth(child, level + 1)

if __name__ == '__main__':
    # n = int(input())
    # xml = ""
    # for i in range(n):
    #     xml =  xml + input() + "\n"
    xml = "".join(
        ["<feed xml:lang='en'>",
         "<title>HackerRank</title>",
         "<subtitle lang='en'>Programming challenges",
         "<subtitle2>",
         "<subtitle3>",
         "<subtitle4></subtitle4>",
         "</subtitle3>",
         "</subtitle2>",
         "</subtitle>",
         "<link rel='alternate' type='text/html' href='http://hackerrank.com/'/>",
         "<updated>2013-12-25T12:00:00",
         "<updated2>",
         "<updated3>",
         "<updated4></updated4>",
         "</updated3>",
         "</updated2>",
         "</updated>",
         "</feed>"])
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)


# https://www.hackerrank.com/challenges/xml2-find-the-maximum-depth/problem