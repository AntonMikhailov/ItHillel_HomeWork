import random


class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.gender}, age: {self.age}'


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'Student: {super().__str__()}, rec_book: {self.record_book}'

class Group:
    def __init__(self, number, max_number_members=10):
        self.number = number
        self.max_number_members = max_number_members
        self.group = set()

    def add_student(self, student):
        if len(self.group) < self.max_number_members:
            self.group.add(student)
        else:
            raise FullGroupError('The group is completely filled')

    def delete_student(self, last_name):
        try:
            self.group.remove(self.find_student(last_name))
        except KeyError as err:
            print(f'There is no student with the last name: {last_name} in {self.number} group.')

    def find_student(self, last_name):
        find_students = [student for student in self.group if student.last_name == last_name]
        return find_students[0] if find_students else None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Number:{self.number}\n{all_students} '


class FullGroupError(Exception):
    pass


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 22, 'John', 'Doe', 'AN146')
st4 = Student('Female', 24, 'Jane', 'Smith', 'AN147')
st5 = Student('Male', 28, 'Mike', 'Brown', 'AN148')
st6 = Student('Female', 27, 'Emily', 'Davis', 'AN149')
st7 = Student('Male', 26, 'Chris', 'Wilson', 'AN150')
st8 = Student('Female', 23, 'Anna', 'Moore', 'AN151')
st9 = Student('Male', 29, 'James', 'Clark', 'AN152')
st10 = Student('Female', 21, 'Olivia', 'Johnson', 'AN153')
st11 = Student('Male', 24, 'Robert', 'Miller', 'AN154')
st12 = Student('Female', 22, 'Sophia', 'Anderson', 'AN155')
all_students = [st1, st2, st3, st4, st5, st6, st7, st8, st9, st10, st11, st12]
random.shuffle(all_students)
gr = Group('PD1')
try:
    for student in all_students:
        gr.add_student(student)
except FullGroupError as e:
    print(e)
print(gr)
