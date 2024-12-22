import sqlite3


class DatabaseManager:
    def __init__(self, db_name="persons.db"):
        self.connect = sqlite3.connect(db_name)

    @staticmethod
    def create_table(db_name):
        connect = sqlite3.connect(db_name)
        with connect:
            connect.execute('''CREATE TABLE IF NOT EXISTS persons (
                                id INTEGER PRIMARY KEY,
                                first_name TEXT NOT NULL,
                                last_name TEXT,
                                middle_name TEXT,
                                birth_date TEXT NOT NULL,
                                death_date TEXT,
                                gender TEXT NOT NULL)''')

    def add_person(self, person):
        with self.connect:
            cursor = self.connect.execute('''SELECT COUNT(*) FROM persons WHERE
                                              first_name = ? AND
                                              last_name = ? AND
                                              middle_name = ? AND
                                              birth_date = ? AND
                                              death_date = ? AND
                                              gender = ?''',
                                          (person.first_name, person.last_name, person.middle_name, person.birth_date,
                                        person.death_date, person.gender))
            if cursor.fetchone()[0] == 0:
                self.connect.execute('''INSERT INTO persons (first_name, last_name, middle_name, birth_date, death_date, gender)
                                         VALUES (?, ?, ?, ?, ?, ?)''',
                                     (person.first_name, person.last_name, person.middle_name, person.birth_date,
                                   person.death_date, person.gender))
            else:
                print(f"Персона {person.first_name} {person.last_name} вже наявна в базі даних.")

    def search_persons(self, query):
        with self.connect:
            cursor = self.connect.execute('''SELECT * FROM persons WHERE 
                                                LOWER(first_name) LIKE LOWER(?) OR 
                                                LOWER(last_name) LIKE LOWER(?) OR 
                                                LOWER(middle_name) LIKE LOWER(?)''',
                (f'%{query}%', f'%{query}%', f'%{query}%'))
            return cursor.fetchall()

    def get_all_persons(self):
        with self.connect:
            cursor = self.connect.execute('SELECT * FROM persons')
            return cursor.fetchall()

    def delete_all_persons(self):
        with self.connect:
            self.connect.execute('DELETE FROM persons')
        self.connect.execute('VACUUM')

    def count_persons(self):
        with self.connect:
            cursor = self.connect.execute('SELECT COUNT(*) FROM persons')
            return cursor.fetchone()[0]

