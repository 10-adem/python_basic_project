def chars_count(sentence = input("Enter a sentence : ")):
    chars_dict = {}
    for i in sentence:
        if i in chars_dict :
            chars_dict[i] += 1
        else:
            chars_dict[i] = 1
    return chars_dict

chars_count()

Enter a sentence : enter a sentence
{' ': 2, 'a': 1, 'c': 1, 'e': 5, 'n': 3, 'r': 1, 's': 1, 't': 2}
