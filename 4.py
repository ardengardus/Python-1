while True:
    user_input = input("Введите число: ")
    if user_input.lstrip('-').isdigit():
        digits_only = user_input.lstrip('-')
        count = len(digits_only)
        print(f"В этом числе {count} цифр(ы).")
    else:
        print("Ошибка: вводимые данные не являются числом.")