import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk
import toplevel
from csv_manager import CSV_Manager
from db_manager import DatabaseManager


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.db_manager = DatabaseManager()
        self.csv_manager = CSV_Manager()
        self.title("Person Manager")
        self.geometry("1200x600")
        self.create_menu()
        self.load_data_into_main_window()

    def create_menu(self):
        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Додати персону вручну", command=self.add_data_manually)
        file_menu.add_command(label="Пошук по базі", command=self.search_data)
        file_menu.add_separator()
        file_menu.add_command(label="Завантажити інформацію в базу із файла", command=self.load_data_from_file)
        file_menu.add_command(label="Вивантаження всіх даних бази в файл", command=self.export_data_to_file)
        file_menu.add_command(label="!!! Видалення всіх даних з бази", command=self.clear_database)
        file_menu.add_separator()
        file_menu.add_command(label="Вихід", command=self.quit)
        menu_bar.add_cascade(label="Меню", menu=file_menu)
        self.tree = ttk.Treeview(self, columns=("Ім'я", "Прізвище", "По-батькові", "Дата нарождення", "Дата смерті", "Стать"),
                                 show="headings")
        self.tree.heading("Ім'я", text="Ім'я")
        self.tree.heading("Прізвище", text="Прізвище")
        self.tree.heading("По-батькові", text="По-батькові")
        self.tree.heading("Дата нарождення", text="Дата нарождення")
        self.tree.heading("Дата смерті", text="Дата смерті")
        self.tree.heading("Стать", text="Стать")
        self.tree.pack(fill=tk.BOTH, expand=True)

    def load_data_into_main_window(self):
        for row in self.db_manager.get_all_persons():
            self.tree.insert("", tk.END, values=row[1:])

    def load_data_from_file(self):
        self.csv_manager.load_data_from_file()
        self.refresh_main_view()

    def add_data_manually(self):
        toplevel.AddPersonWindow(self)

    def search_data(self):
        toplevel.SearchPersonWindow(self)

    def export_data_to_file(self):
        self.csv_manager.export_data_to_file()

    def clear_database(self):
        count = self.db_manager.count_persons()
        if messagebox.askyesno("Підтвердження", f"Впевнені, що бажаєте видалити всі {count} записи?"):
            self.db_manager.delete_all_persons()
            messagebox.showinfo("Виконано!", "База даних очищена.")
            self.refresh_main_view()

    def refresh_main_view(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.load_data_into_main_window()
