import csv

data = [
    ["Іван", "Іванов", "", "1980-01-01", "", "Ч"],
    ["Марія", "Петрова", "Сергіївна", "1990-02-15", "", "Ж"],
    ["Олексій", "Сидоров", "Олексійович", "1985-03-20", "", "Ч"],
    ["Ольга", "Кузнєцова", "", "1975-04-10", "2019-06-25", "Ж"],
    ["Дмитро", "Смірнов", "Володимирович", "1995-05-05", "", "Ч"],
    ["Анна", "Попова", "Іванівна", "1988-06-30", "", "Ж"],
    ["Сергій", "Ковальчук", "", "1970-07-07", "2020-01-15", "Ч"],
    ["Олена", "Козленко", "Олександрівна", "1992-08-22", "", "Ж"],
    ["Микола", "Новіков", "", "1965-09-09", "2018-12-12", "Ч"],
    ["Тетяна", "Морозова", "Володимирівна", "1983-10-10", "", "Ж"],
    ["Володимир", "Павленко", "", "1987-11-11", "", "Ч"],
    ["Аліна", "Волкова", "Сергіївна", "1991-12-12", "", "Ж"],
    ["Андрій", "Шевчук", "Іванович", "1989-01-13", "", "Ч"],
    ["Юлія", "Соколова", "Олексіївна", "1982-02-14", "", "Ж"],
    ["Максим", "Орлов", "", "1978-03-15", "2021-07-20", "Ч"]
]

with open('import_persons.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)
