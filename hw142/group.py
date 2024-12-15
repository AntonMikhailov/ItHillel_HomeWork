class Group:
    def __init__(self, number, max_number_members: int = 10):
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
