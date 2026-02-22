print("Программа проверки совершеннолетия")
while True:
    user_input = input("\nВведите ваш возраст: ")
    is_numeric = user_input.lstrip('-').isdigit()
    if not is_numeric:
        print("Ошибка: введено не число!")
    else:
        age = int(user_input)
        if age < 0:
            print("Ошибка: возраст не может быть отрицательным!")
        elif age >= 18:
            print("Вы совершеннолетний.")
        else:
            print("Вы несовершеннолетний.")