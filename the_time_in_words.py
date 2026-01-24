#!/bin/python3


def timeInWords(h, m):
  
    words_map = {
        '0': "twelve",
        '1': 'one', 
        '2': 'two', 
        '3': 'three', 
        '4': 'four',
        '5': 'five', 
        '6': 'six', 
        '7': 'seven', 
        '8': 'eight', 
        '9': 'nine',
        '10': 'ten', 
        '11': 'eleven', 
        '12': 'twelve', 
        '13': 'thirteen', 
        '14': 'fourteen',
        '16': 'sixteen', 
        '17': 'seventeen', 
        '18': 'eighteen', 
        '19': 'nineteen',
        '20': 'twenty',
        '21': 'twenty one', 
        '22': 'twenty two', 
        '23': 'twenty three', 
        '24': 'twenty four',
        '25': 'twenty five', 
        '26': 'twenty six', 
        '27': 'twenty seven', 
        '28': 'twenty eight', 
        '29': 'twenty nine'
    }

    time_in_words = 'failed to convert time into words'

    if m == 0:
        time_in_words = ' '.join([words_map[str(h)], "o' clock"])
    elif m == 15:
        time_in_words = ' '.join(['quarter past', words_map[str(h)]])
    elif m < 30:
        time_in_words = ' '.join([words_map[str(m)], 'minutes past', words_map[str(h)]])
    elif m == 30:
        time_in_words = ' '.join(['half past', words_map[str(h)]])
    elif m == 45:
        time_in_words = ' '.join(['quarter to', words_map[str((h + 1) % 12)]])
    elif m > 30:
        time_in_words = ' '.join([words_map[str(60 - m)], 'minutes to', words_map[str((h + 1) % 12)]])
    if (m == 1) or (m == 59):
        time_in_words = time_in_words.replace('minutes', 'minute')

    return time_in_words


if __name__ == '__main__':

    h = int(input().strip())
    m = int(input().strip())

    result = timeInWords(h, m)
    print(result)


# https://www.hackerrank.com/challenges/the-time-in-words/problem