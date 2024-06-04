def convert_to_uppercase(text):
    """
    Преобразует строку в верхний регистр.

    Вход:
    text (str): Входная строка.

    Выход:
        str: Строка в верхнем регистре.
    """
    uppercase_text = text.upper()
    return uppercase_text

def capitalize_first_letter(text):
    """
    Делает первую букву в строке заглавной.

    Ввод:
    text (str): Входная строка.

    Выход:
        str: Строка с заглавной первой буквой.
    """
    capitalized_text = text.capitalize()
    return capitalized_text

original_text = input("Введите любое слово маленькими буквами: ")
uppercase_text = convert_to_uppercase(original_text)
capitalized_text = capitalize_first_letter(original_text)

print(uppercase_text)  # Выведет введенное слово большими буквами
print(capitalized_text)  # Выведет введенное слово с заглавной первой буквой
