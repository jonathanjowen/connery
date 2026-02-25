#!/bin/python3

import re



def alternate(s):
    
    """
    Docstring for alternate
    
    :param s: STRING of n lowercase letters
              1 <= n <= 1000              
    """

    unique = list(set(s))
    n_unique = len(unique)

    alt_length = 0

    for i in range(n_unique):
        for j in range(i + 1, n_unique):
            temp = s
            print('keeping', unique[i], unique[j])
            for x in [u for u in unique if u != unique[i] and u != unique[j]]:
                temp = re.sub(x, '', temp)
                print('    removing', x, temp)
            alt_pattern = '(' + unique[i] + unique[j] + ')+' + unique[i] + '?'
            print('alternating pattern =', alt_pattern)
            alt_match = re.fullmatch(re.compile(alt_pattern), temp)
            if alt_match is not None:
                print('alternating match =', alt_match.group(0))
                print('alternating string length =', len(alt_match.group(0)))
                alt_length = max(alt_length, len(alt_match.group(0)))
            else:
                alt_pattern = '(' + unique[j] + unique[i] + ')+' + unique[j] + '?'
                alt_match = re.fullmatch(re.compile(alt_pattern), temp)
                if alt_match is not None:
                    print('alternating match = ', alt_match.group(0))
                    print('alternating string length =', len(alt_match.group(0)))
                    alt_length = max(alt_length, len(alt_match.group(0)))
            print()

    return alt_length


if __name__ == '__main__':

    l = int(input().strip())

    s = input()

    print()
    result = alternate(s)
    print('OUTPUT')
    print(result)



# https://www.hackerrank.com/challenges/two-characters/problem