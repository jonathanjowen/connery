#!/bin/python3


import re

def fun(s):
    email_pattern = r'^[a-zA-Z0-9_\-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
    is_email = re.match(email_pattern, s) is not None
    return is_email

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)


# https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem