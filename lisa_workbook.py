#!/bin/python3

import math

def workbook(n, k, arr):
    
    # Reassigned for clarity
    n_chapters = n
    max_questions_per_page = k
    chapter_lengths = arr
    
    # Required for HackerRank solution
    page = 1
    chapter = 1
    chapter_part = 1
    special_questions = 0

    # Optional for formatted visualizing explanation and debugging
    print()
    # Text labels
    chapter_label = 'CHAPTER'
    page_col_label = 'page'
    question_col_label = 'questions'
    special_question_char = '*'
    # Estimate column widths to apply to all chapters
    page_count = 0
    max_question_chars = 0
    for chapter_length in chapter_lengths:
        full_pages_in_chapter = chapter_length // max_questions_per_page
        partial_last_page = chapter_length % max_questions_per_page > 0        
        page_count += full_pages_in_chapter + partial_last_page
        question_chars_for_chapter = (int(math.log10(chapter_length)) + 2) * max_questions_per_page + len(special_question_char)
        max_question_chars = max(max_question_chars, question_chars_for_chapter)
    max_page_chars = int(math.log10(page_count)) + 1
    col_margin = 1
    page_col_text = (' ' * col_margin) + page_col_label + (' ' * col_margin)
    page_col_width = max(len(page_col_text), max_page_chars)
    page_spacer = (page_col_width - max_page_chars) // 2
    page_extra_left_space = (page_col_width - max_page_chars) % 2
    question_col_text = (' ' * col_margin) + question_col_label + (' ' * col_margin)
    question_col_width = max(len(question_col_text), max_question_chars + 2 * col_margin)
    max_line_chars = page_col_width + question_col_width
    max_chapter_chars = len(chapter_label) + int(math.log10(max(chapter_lengths))) + 2
    chapter_spacer = ((max_line_chars - max_chapter_chars) // 2) - 1
    # Initialize dictionary & special question flag 
    book = {}
   

    # Required for HackerRank solution
    while chapter <= n_chapters:
        last_question_in_chapter = chapter_lengths[chapter - 1]
        first_question_on_page = max_questions_per_page * (chapter_part - 1) + 1
        last_question_on_page = min(max_questions_per_page * chapter_part, last_question_in_chapter)
        if first_question_on_page <= page and page <= last_question_on_page:
            special_questions += 1
            special_question_flag = special_question_char # Optional

        # Optional
        book[page] = {'chapter': chapter, 'part': chapter_part, 'questions': range(first_question_on_page, last_question_on_page + 1)}
        if chapter_part == 1:
            print(' ' * chapter_spacer, chapter_label, chapter)
            print(page_col_text, question_col_text)
            print('-' * max_line_chars)
        question_chars = 0
        for question in book[page]['questions']:
            question_chars += int(math.log10(question)) + 2
        print(' ' * page_extra_left_space, ' ' * page_spacer, '.' * (max_page_chars - int(math.log10(page)) - 1), page, ' ' * page_spacer, sep='', end=' ' * col_margin)
        print(*book[page]['questions'], end=' ' * (max_line_chars - page_col_width - question_chars - 1))
        print(special_question_flag)
        special_question_flag = ''

        # Required for HackerRank solution
        page += 1
        if last_question_on_page < last_question_in_chapter:
            chapter_part += 1
        else:
            print() # Optional 
            chapter += 1
            chapter_part = 1

    return special_questions
    

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)
    print()
    print('OUTPUT')
    print(result)


# https://www.hackerrank.com/challenges/lisa-workbook/problem