from human import Human


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'Student: {super().__str__()}, rec_book: {self.record_book}'

    def __eq__(self, other):
        return self.first_name == other.first_name and self.last_name == other.last_name and self.age == other.age

    def __hash__(self):
        return hash(str(self))
