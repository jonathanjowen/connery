#!/bin/python3


def workbook(n, k, arr):
    # Reassigned for clarity
    n_chapters = n
    questions_per_page = k
    chapter_lengths = arr
    # Optional for visualizing explanation, tracking, & debugging
    book = {}
    special_question_id = None
        # Required for HackerRank solution
    page = 1
    chapter = 1
    chapter_part = 1
    special_questions = 0
    while chapter <= n_chapters:
        last_question_in_chapter = chapter_lengths[chapter - 1]
        first_question_on_page = questions_per_page * (chapter_part - 1) + 1
        last_question_on_page = min(questions_per_page * chapter_part, last_question_in_chapter)
        if first_question_on_page <= page and page <= last_question_on_page:
            special_questions += 1
            special_question_id = page # Optional
        # Optional for visualizing explanation, tracking, & debugging
        book[page] = {'chapter': chapter, 'part': chapter_part, 'questions': range(first_question_on_page, last_question_on_page + 1), 'special question': special_question_id}
        if chapter_part == 1:
            print()
        print(page, book[page])
        special_question_id = None
        # Required for HackerRank solution
        page += 1
        if last_question_on_page < last_question_in_chapter:
            chapter_part += 1
        else:
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