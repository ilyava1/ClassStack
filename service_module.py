open_brackets = ['[', '{', '(']
close_brackets = [']', '}', ')']
balanced_brackets = ['[]', '{}', '()']


class Stack():
    my_stack = []

    def __init__(self, my_stack):
        self.my_stack = []

    def isEmpty(self):
        """
        Метод проверки стэка на пустоту

        :return: Метод возвращает True или False.
        """
        if self.my_stack == []:
            return True
        else:
            return False

    def push(self, new_element):
        """
        Методо добавления нового элемента в стэк

        :return: Метод ничего не возвращает.
        """
        self.my_stack.append(new_element)
        return

    def pop(self):
        """
        Метод удаления верхнего элемента стэка.

        :return:  Метод возвращает верхний элемент стэка, стэк изменяется
        """
        deleted_element = self.my_stack.pop(-1)
        return deleted_element

    def peek(self):
        """
        Метод возвращения верхнего верхнего элемента стэка.

        :return:  Метод возвращает верхний элемент стека, стэк не меняется
        """
        top_element = self.my_stack[-1]
        return top_element

    def size(self):
        """
        Метод возвращения количества элементов стэка.

        :return:  Метод возвращает количество элементов стэка
        """
        len_stack = len(self.my_stack)
        return len_stack


def inp_string():
    """
    Функция пользовательского ввода строки

    :return: Строка, введенная пользователем
    """
    bracket_string = input('Введите строку со скобками: ')
    return bracket_string


def check_string(bracket_string):
    """
    Функция проверки строки на содержение скобки

    :param bracket_string: строка для проверки на наличие скобки
    :return: Строка с ответом: содержит или не содержит
    """
    for letter in bracket_string:
        if letter in open_brackets or letter in close_brackets:
            check_result = 'Строка содержит одну или более скобок'
            return check_result
    check_result = 'Строка не содержит скобок'
    return check_result


def check_bracket_balance(bracket_string):
    """
    Функция проверки строки со скобками на сбалансированность скобок

    :param bracket_string: Строка со скобками
    :return: Строка с ответом: сбалансированы скобки либо нет
    """
    my_class = Stack
    for simbol in bracket_string:
        if simbol in open_brackets:
            my_class.push(my_class, simbol)
        elif simbol in close_brackets and not my_class.isEmpty(my_class):
            unknown_brackets = my_class.pop(my_class) + simbol
            if str(unknown_brackets) not in balanced_brackets:
                result = 'Скобки не сбалансированы'
                return result
        elif simbol in close_brackets and my_class.isEmpty(my_class):
            result = 'Скобки не сбалансированы'
            return result
    if not my_class.isEmpty(my_class):
        result = 'Скобки не сбалансированы'
        return result
    result = 'Скобки сбалансированы'
    return result
