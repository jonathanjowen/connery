#!/bin/python3

import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    attribute_count = len(node.attrib)
    for child in node:
        attribute_count += get_attr_number(child)
    return attribute_count


if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))


# https://www.hackerrank.com/challenges/xml-1-find-the-score/problem