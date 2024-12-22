import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from tkcalendar import DateEntry
from db_manager import DatabaseManager
from person import Person


class AddPersonWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.db_manager = DatabaseManager()
        self.parent = parent
        self.title("Додати персону вручну")
        self.geometry("350x200")
        self.create_add_form()

    def create_add_form(self):
        tk.Label(self, text="Ім'я").grid(row=0, column=0)
        self.first_name_entry = tk.Entry(self)
        self.first_name_entry.grid(row=0, column=1)
        tk.Label(self, text="Прізвище").grid(row=1, column=0)
        self.last_name_entry = tk.Entry(self)
        self.last_name_entry.grid(row=1, column=1)
        tk.Label(self, text="По-батькові").grid(row=2, column=0)
        self.middle_name_entry = tk.Entry(self)
        self.middle_name_entry.grid(row=2, column=1)
        tk.Label(self, text="Дата нарождення").grid(row=3, column=0)
        self.birth_date_entry = DateEntry(self, date_pattern='yyyy-mm-dd')
        self.birth_date_entry.grid(row=3, column=1)
        tk.Label(self, text="Дата смерті").grid(row=4, column=0)
        self.death_date_entry = DateEntry(self, date_pattern='yyyy-mm-dd')
        self.death_date_entry.grid(row=4, column=1)
        tk.Label(self, text="Стать").grid(row=5, column=0)
        self.gender_var = tk.StringVar(value="Ч")
        self.gender_menu = tk.OptionMenu(self, self.gender_var, "Ч", "Ж")
        self.gender_menu.grid(row=5, column=1)
        tk.Button(self, text="Додати", command=self.add_person).grid(row=6, column=0, columnspan=2)

    def add_person(self):
        person = Person(
            self.first_name_entry.get(),
            self.last_name_entry.get(),
            self.middle_name_entry.get(),
            self.birth_date_entry.get(),
            self.death_date_entry.get(),
            self.gender_var.get()
        )
        self.db_manager.add_person(person)
        messagebox.showinfo("Виконано!", "Персону додано в базу даних.")
        self.parent.refresh_main_view()
        self.destroy()


class SearchPersonWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.db_manager = DatabaseManager()
        self.title("Пошук в базі")
        self.geometry("400x300")
        self.create_search_form()

    def create_search_form(self):
        tk.Label(self, text="Запит для пошуку").grid(row=0, column=0)
        self.query_entry = tk.Entry(self)
        self.query_entry.grid(row=0, column=1)
        tk.Button(self, text="Пошук", command=self.search_persons).grid(row=1, column=0, columnspan=2)
        self.result_text = tk.Text(self, state='disabled', width=50, height=15)
        self.result_text.grid(row=2, column=0, columnspan=2)

    def search_persons(self):
        query = self.query_entry.get()
        results = self.db_manager.search_persons(query)
        self.result_text.config(state='normal')
        self.result_text.delete(1.0, tk.END)
        for person in results:
            age = self.calculate_age(person[4], person[5])
            self.result_text.insert(tk.END,
                                    f"Ім'я: {person[1]}, Прізвище: {person[2]}, По-батькові: {person[3]}, Вік(повних років): {age}, Дата нарождення: {person[4]}, Дата смерті: {person[5]}, Стать: {person[6]}\n")
        self.result_text.config(state='disabled')

    def calculate_age(self, birth_date, death_date):
        birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
        if death_date:
            death_date = datetime.strptime(death_date, "%Y-%m-%d")
            age = death_date.year - birth_date.year - (
                        (death_date.month, death_date.day) < (birth_date.month, birth_date.day))
        else:
            today = datetime.today()
            age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age