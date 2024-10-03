from itertools import count

calls = 0

def count_calls():
    global calls
    calls+=1

def string_info(string):
    count_calls()
    string = (len(string), string.upper(), string.lower())
    return string

def is_contains(string, list_to_search):
    count_calls()
    for i in list_to_search:
        string1 = string.lower() == i.lower()

    return string1


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)