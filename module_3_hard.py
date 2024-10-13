def calculate_structure_sum(data):
    dlina = int()
    if not data:
        return 0


    if isinstance(data, (list, tuple)):
        return dlina + calculate_structure_sum(data[0]) + calculate_structure_sum(data[1:])
    elif isinstance(data, set):
        return calculate_structure_sum(list(data))

    elif isinstance(data, dict):
        return calculate_structure_sum(list(data.items()))

    elif isinstance(data, int):
        return dlina + data
    elif isinstance(data, float):
        return dlina + data
    elif isinstance(data, str):
        return dlina + len(data)

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]


print(calculate_structure_sum(data_structure))