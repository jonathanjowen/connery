#!/bin/python3

from collections import OrderedDict

n_items = int(input())

items = OrderedDict()

for item in range(n_items):
    item_as_list = input().split()
    item_price = int(item_as_list.pop())
    item_name = ' '.join(item_as_list)
    if item_name in items.keys():
        items[item_name] += int(item_price)
    else:
        items[item_name] = int(item_price)
        
for item_name, item_price in items.items():
    print(item_name, item_price)


# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem