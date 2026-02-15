class Student:
    def __init__(self, korean, english, math):
        self.korean = korean
        self.english = english
        self.math = math

    def total(self):
        return self.korean + self.english + self.math


A, B, C = map(int, input().split(', '))
S = Student(A, B, C)
print(f"국어, 영어, 수학의 총점: {S.total()}")