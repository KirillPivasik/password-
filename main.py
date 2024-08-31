import random

# Переменная с символами для пароля
lowercase = "abcdefghijklnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "1234567890"
symbols = lowercase + uppercase + digits

while True:
    # Запрос у пользователя нужной длины пароля
    length = int(input("Введите длину пароля (минимум 3): "))
    
    if length < 3:
        print("Длина пароля должна быть минимум 3 символа.")
        continue

    # Переменные для хранения частей пароля
    generated_password = []

    # Обеспечиваем наличие хотя бы одной заглавной буквы и одной цифры
    generated_password.append(random.choice(uppercase))
    generated_password.append(random.choice(digits))

    # Генерация оставшихся символов пароля
    for _ in range(length - 2):
        generated_password.append(random.choice(symbols))
    
    # Перемешиваем символы пароля
    random.shuffle(generated_password)

    # Преобразуем список в строку
    final_password = ''.join(generated_password)

    # Вывод сгенерированного пароля на консоль
    print("Сгенерированный пароль:", final_password)
    
    # Выход из цикла после успешного генерации пароля
    # break