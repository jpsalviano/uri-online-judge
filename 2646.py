def main():
    #num of translations in dict, num of word pairs to check
    m, n = [int(x) for x in input().split()]
    #creates dict that will store translations
    translation = dict()
    #store translations {str(key): list(values)}
    for _ in range(m):
        a, b = input().split()
        #adds key-value pair to dict translation
        #in case key already exists, only appends new value to [values]
        if a in translation:
            translation[a].append(b)
        else:
            translation[a] = [b]
    #checking word pairs
    for _ in range(n):
        word_a, word_b = input().split()
        check_translation(word_a, word_b, translation)


def check_translation(word_a, word_b, translation):
    #checks if word_a can be translated to word_b, directly corresponding
    #letter by letter, according to translation dict
    for letter_a, letter_b in zip(list(word_a), list(word_b)):
        if letter_a == letter_b:
            continue
        elif letter_a in translation:
            if letter_b in translation[letter_a]:
                continue
            else:
                checked = [] #for storing already checked translations
                if check_further(letter_a, letter_b, translation, checked):
                    continue
                else:
                    return print('no')
        else:
            return print('no')
    return print('yes')


def check_further(letter_a, letter_b, translation, checked):
    #checks if letter_a can be indirectly translated to letter_b,
    #according to translation dict - recursive function
    #avoids researching already checked translations
    to_check = [i for i in translation[letter_a] if i not in checked]
    #checks only if there's something to check, otherwise returns false
    if to_check:
        for t in to_check:
            if t in translation:
                if letter_b in translation[t]:
                    return True
                else:
                    checked.append(t)
                    [translation[letter_a].append(i) for i in translation[t]]
            else:
                checked.append(t)
        check_further(letter_a, letter_b, translation, checked)
    else:
        return False


main()
