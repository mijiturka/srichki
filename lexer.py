import re

def clean_up(token):
    # Return words without their punctuation if it's come at the end of the word.
    # Disregard everything else

    we_want = '[а-я]+\-?[а-я]*'
    we_dont_want = ',|.|!|\?|:|;|"'

    word_pattern = f'^({we_want})({we_dont_want})?$'
    token = token.lower()

    try:
        punctuated = re.search(word_pattern, token)
        return (punctuated[1])
    except KeyError as e:
        return None

def split(text):
    return [clean_up(token) for token in text.split(' ')]

def words(text):
    return [word for word in split(text) if word is not None]

if __name__ == '__main__':
    text = 'Здрасти, свят! Това е чушко-пек. Да.'
    print(words(text))
