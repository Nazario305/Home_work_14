from student import Student
from group import Group, GroupLimitError


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

gr.add_student(st1)
gr.add_student(st2)
print(gr)

students = [st1, st2, st3, st4, st5, st6, st7, st8, st9, st10]
for student in students:
    gr.add_student(student)
print(gr)

try:
    gr.add_student(st11)
except GroupLimitError as e:
    print(e)



assert gr.find_student('Jobs') == st1, "Test1 failed"  # Порівняння об'єктів
assert gr.find_student('Jobs2') is None, "Test2 failed"  # Пошук неіснуючого студента

gr.delete_student('Taylor')
print(gr)
