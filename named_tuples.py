if __name__ == '__main__':
    from collections import namedtuple
    n_students = int(input())
    field_names = input()
    Student = namedtuple('Student', field_names)
    total_marks = 0
    for _ in range(n_students):
        student = Student._make(input().split())
        total_marks += int(student.MARKS)
    print(f'{total_marks/n_students:.2f}')