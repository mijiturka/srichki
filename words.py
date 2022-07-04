import lexer

def unique_in_text(text):
    return set(lexer.words(text))

def prefixes():
    return {
        'н': ['на', 'над'],
        'п': ['по', 'пред', 'пре', 'при']
    }

def suffixes():
    return {
        'а': ['ач', 'ар'],
        'и': ['ик', 'ица'],
        'к': ['ка'],
        'т': ['та', 'тел']
    }

def split_at_prefix(word):
    first_letter = word[0]

    if first_letter in prefixes():
        for prefix in prefixes()[first_letter]:
            if word.startswith(prefix):
                split = (prefix, word.replace(prefix, '', 1))
                if split == '':
                    # The whole world has matched with a prefix
                    return word
                return split
    return word

def split_at_suffix(word):
    try:
        penultimate_letter = word[-2]
    except IndexError as e:
        return word

    if penultimate_letter in suffixes():
        for suffix in suffixes()[penultimate_letter]:
            if word.endswith(suffix):
                split = word.rpartition(suffix)
                if split == '':
                    # The whole world has matched with a suffix
                    return word
                return split
    return word

def concat(a, b):
    if type(a) is tuple:
        if type(b) is tuple:
            return a + b
        else:
            return a + (b,)
    else:
        if type(b) is tuple:
            return (a,) + b
        return (a,) + (b,)

if __name__ == '__main__':
    text = 'Здрасти, свят! Това е чушко-пек. Да, наистина е така: това е чушкопек. Някои биха си помислили, че представката е чушка, а наставката е пек. Всъщност чушкопекът е сложно устройство, а думата "чушкопек" е съставна дума, съдържаща в себе си два корена.'

    for word in unique_in_text(text):
        first_split = split_at_prefix(word)

        if type(first_split) is tuple:
            second_split = concat(first_split[0], split_at_suffix(first_split[1]))
        else:
            second_split = split_at_suffix(first_split)

        print(second_split)
