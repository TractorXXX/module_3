def get_multiplied_digits(number):    # Если устраивает нулевой результат при последнем нуле
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first
#------------------------------------------------------------------------
def get_multiplied_digits_0(number):    # Если нужно убрать последний нуль
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits_0(int(str_number[1:]))
    else:
        if first > 0:
            return first
        else:
            return 1
#------------------------------------------------------------------------

result = get_multiplied_digits(40203)    # Вариант без нуля в конце
print(result)
result_0 = get_multiplied_digits_0(40203)
print(result_0)

result = get_multiplied_digits(402030)    # Вариант с нулем в конце
print(result)
result_0 = get_multiplied_digits_0(402030)
print(result_0)