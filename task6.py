name = input("Введите ваше имя: ")
age = input("Введите ваш возраст: ")
fav_subj = input("Введите любимые предметы (через запятую): ")

subjects_list = fav_subj.split(',')

student_info = {
    "Имя": name,
    "Возраст": age,
    "Любимые предметы": subjects_list
}

print("===============================")
print("АНКЕТА СТУДЕНТА")
print("===============================")
print(f"Имя: {student_info['Имя']}")
print(f"Возраст: {student_info['Возраст']}")
print(f"Любимые предметы: {student_info['Любимые предметы']}")
print("===============================")