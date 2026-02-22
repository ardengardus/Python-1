name = input("Ваше имя: ")
last_name = input("Фамилия: ")
age = input("Возраст: ")
print("\nРеализация через format:")
output_format = "Ваше имя: {}, Фамилия: {}, Возраст: {} лет".format(name, last_name, age)
print(output_format)
print("\nРеализация через f-string:")
output_fstring = f"Ваше имя: {name}, Фамилия: {last_name}, Возраст: {age} лет"
print(output_fstring)