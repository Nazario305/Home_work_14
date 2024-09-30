class GroupLimitError(Exception):
    def __init__(self, message="Досягнуто ліміт студентів у групі!"):
        self.message = message
        super().__init__(self.message)

class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.age} years old, {self.gender}'

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{self.first_name} {self.last_name},record book:{self.record_book}, {self.age} years old, {self.gender}'

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupLimitError()
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = "\n".join([str(student) for student in self.group])
        return f'Group Number: {self.number}\nStudents:\n{all_students}'

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Female', 23, 'Anna', 'Smith', 'AN146')
st4 = Student('Male', 20, 'John', 'Doe', 'AN147')
st5 = Student('Male', 22, 'Jake', 'White', 'AN148')
st6 = Student('Female', 24, 'Emily', 'Clark', 'AN149')
st7 = Student('Male', 21, 'Chris', 'Evans', 'AN150')
st8 = Student('Male', 23, 'Paul', 'Walker', 'AN151')
st9 = Student('Female', 25, 'Megan', 'Fox', 'AN152')
st10 = Student('Male', 26, 'Tom', 'Hardy', 'AN153')
st11 = Student('Female', 27, 'Natalie', 'Portman', 'AN154')

gr = Group('PD1')

students = [st1, st2, st3, st4, st5, st6, st7, st8, st9, st10]
for student in students:
    gr.add_student(student)
print(gr)

try:
    gr.add_student(st11)
except GroupLimitError as e:
    print(e)



assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

