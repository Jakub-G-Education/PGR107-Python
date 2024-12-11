class Student:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark
        self.passing_mark = 60

    def __str__(self):
        return "Student ---> " + str(self.name) + ", " + "Mark ---> " + str(self.mark)

    def pass_or_fail(self):
        if self.mark >= self.passing_mark:
            return "Status: Pass"
        else:
            return "Status: Fail"


student1 = Student("John", 52)
print(student1)
status1 = student1.pass_or_fail()
print(status1)

print()

student2 = Student("Jenny", 69)
print(student2)
status2 = student2.pass_or_fail()
print(status2)
