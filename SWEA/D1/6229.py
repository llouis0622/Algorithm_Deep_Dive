class Person:
    def getGender(self):
        return "Unknown"


class Male(Person):
    def getGender(self):
        return "Male"


class Female(Person):
    def getGender(self):
        return "Female"


m = Male()
f = Female()
print(m.getGender())
print(f.getGender())