#!/bin/python3

from collections import Counter
from collections import defaultdict

# Read single-line inputs
# X = int(input())                                        # total shoes in stock
# shoe_stock = Counter(list(map(int, input().split())))   # stock by shoe size
# N = int(input())                                        # total customers
shoe_stock = Counter([2, 3, 4, 5, 6, 8, 7, 6, 5, 18])
N = 6

# Create customer shoes dictionary by looping over N customer input lines
shoes = {}
for _ in range(N):
    shoe_size, price = map(int, input().split())
    if shoe_size in shoes:
        shoes[shoe_size].append(price)
        # uncomment if sales prioritized by price:
        # shoes[shoe_size].sort(reverse=True)
    else:
        shoes[shoe_size] = [price]

# Initiate sales total then toop through shoes adding price to total sales
sales = 0
for shoe in shoes:
    customers = len(shoes[shoe])                 # potential sales for shoe size
    stock = shoe_stock[shoe]                     # avaiilable in shoe size
    n_sales = min(customers, stock)              # shoes that can be sold
    sales = sales + sum(shoes[shoe][:n_sales])
    
print(sales)
