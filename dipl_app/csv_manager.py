from tkinter import messagebox, filedialog
import csv
from db_manager import DatabaseManager
from person import Person


class CSV_Manager:
    def __init__(self):
        self.db_manager = DatabaseManager()


    def export_data_to_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if file_path:
            persons = self.db_manager.get_all_persons()
            with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["Ім'я", "Прізвище", "По-батькові", "Дата нарождення", "Дата смерті", "Стать"])
                for person in persons:
                    writer.writerow(person[1:])
            messagebox.showinfo("Виконано!", "Інформацію вивантажено в файл.")

    def load_data_from_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            with open(file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                header = next(reader)
                if header != ["Ім'я", "Прізвище", "По-батькові", "Дата нарождення", "Дата смерті", "Стать"]:
                    csvfile.seek(0)
                    reader = csv.reader(csvfile)
                for row in reader:
                    person = Person(*row)
                    self.db_manager.add_person(person)
            messagebox.showinfo("Виконано!", "Інформацію додано в базу.")
