if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    sum_of= sum(student_marks[query_name])
    avg_of = sum_of/3
    print(format(avg_of,'.2f'))
    