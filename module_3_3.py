#"Распаковка позиционных параметров".

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
values_list = [34, 'Список', [1, 2, 3]]
values_list_2 = [54.32, 'Список2']
values_dict = {'a': 2, 'b': 'Словарь', 'c': False}


print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])
