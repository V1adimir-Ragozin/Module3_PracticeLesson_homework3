def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])    # передали первый символ
    if len(str_number) <= 1:   # если в str_number один или менбьше элементов
        return first   #то функция возвращает в место откуда она была вызвана переменную first
    return first * get_multiplied_digits(int(str_number[1:]))


print(get_multiplied_digits(40203))
