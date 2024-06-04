def convert_to_uppercase(text):
       """
    Преобразует строку в верхний регистр.

    Args:
        text (str): Входная строка.

    Returns:
        str: Строка в верхнем регистре.
    """
    uppercase_text = text.upper()
    return uppercase_text

original_text = input("Введите любое слово маленькими буквами: ")
uppercase_text = convert_to_uppercase(original_text)
print(uppercase_text)  # Выведет введенное слово большими буквами

