import lexer

def unique_in_text(text):
    return set(lexer.words(text))

def find_prefix(word):
    pass
#     if word.startswith('')

if __name__ == '__main__':
    text = 'Здрасти, свят! Това е чушко-пек. Да, наистина е така: това е чушкопек. Някои биха си помислили, че представката е чушка, а наставката е пек. Всъщност чушкопекът е сложно устройство, а думата "чушкопек" е съставна дума, съдържаща в себе си два корена.'
    print(unique_in_text(text))
