# Проект FitLife - MVP версия 1.0
# Задаем переменные для приветствия и декоративного разделителя
greetings = 'Доброго времени суток!'
decor_line = '-' * 60

# Оформляем вывод приветствия
print(decor_line)
print(greetings)
print(decor_line)

# Собираем данные о пользователе (Имя, Возраст)
user_name = input('Введите Ваше имя: ')
user_age = int(input('Введите Ваш возраст: '))

# Собираем данные о пользователе (Вес, Рост)
user_weight = float(
    input('Введите Ваш вес в кг (например, 82): ').replace(",", ".")
)
user_height = float(
    input('Введите Ваш рост в метрах (например, 1.81): ').replace(",", ".")
)

# Рассчитываем Индекс Массы Тела (ИМТ)
bmi = user_weight / (user_height ** 2)
# Задаем отдельную переменную ИМТ для вывода, на случай,
# если понадобится промежуточное значение
bmi_rounded = round(bmi, 1)

# Подсчет воды: вес * 30 мл

# Рассчитываем норму воды в миллилитрах
WATER_PER_KG = 30
water_ml = user_weight * WATER_PER_KG
# Переводим в литры
WATER_PER_L = 1000
water_l = water_ml / WATER_PER_L

# Выводим готовый отчет пользователю
print(decor_line)
print(f"Отчет для пользователя: {user_name.title()} ({user_age} г.)")
print(f"Ваш Индекс Массы Тела (ИМТ): {bmi_rounded}")
print(f"Рекомендуемая норма воды {water_l:.1f} л. в день")
print(decor_line)
print('Расчет окончен. Будьте здоровы!')
