def count_calls():
    global calls
    calls += 1

def string_info(string):
    kortej = len(string), string.upper(), string.lower()
    count_calls()
    return kortej

def is_contains(string, list_to_search):
    s = string.lower()    # Переводим строку в нижний регистр
    k = 0
    for i in list_to_search:    # Переводим все элементы списка к нижниму регистру
        list_to_search[k] = i.lower()
        k += 1
    count = list_to_search.count(s)    # Проверка наличия строки в списке
    if count > 0:
        in_list = True
    else:
        in_list = False
    count_calls()
    return in_list
#--------------------------------------------------------------

calls = 0

kortej = string_info('Елизавета')
print(kortej)
kortej = string_info('носТРадАмус')
print(kortej)

in_list = is_contains('СлиВА', ['Яблоко', 'сЛИва', 'дынЯ'])
print(in_list)
in_list = is_contains('груша', ['Яблоко', 'сЛИва', 'дынЯ'])
print(in_list)

print(calls)