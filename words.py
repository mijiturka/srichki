import lexer

def unique_in_text(text):
    return set(lexer.words(text))

def prefixes():
    return {
        'н': ['на', 'над'],
        'п': ['по', 'пред', 'пре', 'при']
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

if __name__ == '__main__':
    text = 'Здрасти, свят! Това е чушко-пек. Да, наистина е така: това е чушкопек. Някои биха си помислили, че представката е чушка, а наставката е пек. Всъщност чушкопекът е сложно устройство, а думата "чушкопек" е съставна дума, съдържаща в себе си два корена.'

    for word in unique_in_text(text):
        print(split_at_prefix(word))
