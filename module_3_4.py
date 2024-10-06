def single_root_words(root_word, *other_words):
    same_words = []
    for i in range(len(other_words)):
        same_words.append(i)
        semi_result = root_word.lower() == i.lower()

    return semi_result


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)