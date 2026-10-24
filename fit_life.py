# Проект FitLife - MVP версия 1.0
# Задаем переменные для приветствия и декоративного разделителя
GREETINGS = 'Доброго времени суток!'
DECOR_LINE = '-' * 60

# Оформляем вывод приветствия
print(DECOR_LINE, GREETINGS, DECOR_LINE, sep='\n')

# Собираем данные о пользователе (Имя, Возраст)
user_name = input('Введите Ваше имя: ')
name_title = user_name.title()
user_age = int(input('Введите Ваш возраст: '))

# Собираем данные о пользователе (Вес, Рост)
user_weight = float(
    input('Введите Ваш вес в кг (например, 82): ').replace(',', '.')
)
user_height = float(
    input('Введите Ваш рост в метрах (например, 1.81): ').replace(',', '.')
)

# Рассчитываем Индекс Массы Тела (ИМТ)
bmi = user_weight / (user_height ** 2)

# Задаем отдельную переменную ИМТ для вывода, на случай,
# если понадобится промежуточное значение
bmi_rounded = round(bmi, 1)

# Рассчитываем норму воды в миллилитрах
WATER_PER_KG = 30
water_ml = user_weight * WATER_PER_KG
# Переводим в литры
WATER_PER_L = 1000
water_l = water_ml / WATER_PER_L

# Выводим готовый отчет пользователю
print(DECOR_LINE)
print(f'Отчет для пользователя: {name_title} ({user_age} г.)')
print(f'Ваш Индекс Массы Тела (ИМТ): {bmi_rounded}')
print(f'Рекомендуемая норма воды {water_l:.1f} л. в день')
print(DECOR_LINE)
print('Расчет окончен. Будьте здоровы!')
