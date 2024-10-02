from itertools import count

calls = 0


def count_calls(calls):
    def string_info(string):
        string = int(len(string)), str(string.upper()), str(string.lower())

        return string

    return count_calls
    print(string_info('capibara'))

    def is_contains(string, list_to_search):
        list_to_search = []
        for i in list(list_to_search):
            if i == str(string):
                is_contains = True
            else:
                is_contains = False

            return is_contains
        print(is_contains('urban', ['ban', 'banan', 'urban']))
        return count_calls

    calls = int(count(string_info())) + int(count(is_contains()))






print(string_info())
print(is_contains())
print(is_contains())
print(calls)