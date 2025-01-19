n = int(input())
students = []
for _ in range(n):
    name, k, e, m = input().split()
    students.append((name, int(k), int(e), int(m)))
students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
for student in students:
    print(student[0])