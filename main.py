from service_module import inp_string, check_string, check_bracket_balance

if __name__ == '__main__':

    # Запрашиваем ввод строки со скобками
    bracket_string = inp_string()

    # Проверяем строку на содержание скобок
    check_result = check_string(bracket_string)
    if check_result == 'Строка не содержит скобки':
        print(check_result)
        print('Работа программы завершена')
        exit()

    # Проверяем строку на сбалансированность
    result = check_bracket_balance(bracket_string)
    print(result)
