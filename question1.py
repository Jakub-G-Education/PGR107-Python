class Person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def get_info(self):
        print("Full Name:", self.fname, self.lname)
        print("Age:", self.age)


class Student(Person):
    def __init__(self, fname, lname, age, student_id):
        super().__init__(fname, lname, age)
        self.studentid = student_id

    def get_stuinfo(self):
        super().get_info()
        print("Student ID:", self.studentid)


class Employee(Person):
    def __init__(self, fname, lname, age, employee_number, salaray):
        super().__init__(fname, lname, age)
        self.employee_number = employee_number
        self.salary = salaray

    def get_empinfo(self):
        super().get_info()
        print(f"Employee No: {self.employee_number} \nSalary: {self.salary} USD")


new_student = Student("Anthony", "Smith", 35, "s346571")
new_student.get_stuinfo()
print("============================")
new_employee = Employee("Sarah", "Taylor", 34, 2919736, 5000)
new_employee.get_empinfo()

