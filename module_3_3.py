#"Распаковка позиционных параметров".

def print_params(a = 1, b = 'строка', c = True):
    values_list_2 = [54.32, 'Строка', True]
    values_dict = {a: 1, b: 'Ctroka', c: False}



print_params(*values_list_2, 42)
print_params(*values_list_2, 42)
print_params(*values_list_2, 42)
print_params(*values_list_2, 42)
print_params(*values_list_2, 42)
print_params(b = 25)
print_params(c = [1,2,3])
