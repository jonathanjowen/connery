#!/bin/python3

def read_integers(sep=None):
    """Return an iterator of integers from a STDIN line."""  
    return(map(int, input().split(sep)))
    
def read_floats(sep=None):
    """Return an iterator of floating point numbers from a STDIN line."""  
    return(map(float, input().split(sep)))
    
    
if __name__ == '__main__':
    
    n_of_students, n_of_subjects = list(read_integers())
    
    all_scores = []
    
    for subject in range(n_of_subjects):
        subject_scores = list(read_floats())
        all_scores += [subject_scores]
        
    student_scores = zip(*all_scores)
    student_averages = map(lambda x: sum(x) / n_of_subjects, student_scores)
    
    [print(avg) for avg in student_averages]


# https://www.hackerrank.com/challenges/zipped/problem