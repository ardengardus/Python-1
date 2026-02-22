print("Программа проверки четности")
while True:
    user_input = input("\nВведите число: ")
    if user_input.isdigit():
        number = int(user_input)
        if number % 2 == 0:
            print(f"Число {number} является чётным")
        else:
            print(f"Число {number} является нечётным")
    else:
        print("Ошибка: введено не число")