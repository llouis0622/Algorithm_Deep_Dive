class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"이름: {self.name}"


class GraduateStudent(Student):
    def __init__(self, name, major):
        super().__init__(name)
        self.major = major

    def __str__(self):
        return f"이름: {self.name}, 전공: {self.major}"


A = Student("홍길동")
B = GraduateStudent("이순신", "컴퓨터")
print(A)
print(B)