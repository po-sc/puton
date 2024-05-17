def main(input_str):
    # Преобразуем входную строку в целое число
    input_number = int(input_str)

    # Извлекаем битовые поля l1, l2 и l3 из входного числа
    l1 = (input_number >> 0) & 0b11  # первые 2 бита
    l2 = (input_number >> 2) & 0b11111111  # следующие 8 бит
    l3 = (input_number >> 10) & 0b1111111  # последние 7 бит

    # Формируем новое число согласно новой схеме
    output_number = (l1 << 16) | (l2 << 3) | l3

    # Преобразуем выходное число в строку и возвращаем
    return str(output_number)


# Тесты
print(main('1426'))  # '1609'
print(main('610'))  # '2440'
print(main('6890'))  # '2990'
print(main('3741'))  # '133747'
