import re

def clean_up(token):
    # Return words without their punctuation if it's come at the end of the word.
    # Disregard everything else

    useless_beginning = '"'
    we_want = '[а-я]+\-?[а-я]*'
    useless_ending = ',|.|!|\?|:|;|"'

    word_pattern = f'^({useless_beginning})?({we_want})({useless_ending})?$'
    token = token.lower()

    try:
        punctuated = re.search(word_pattern, token).groups()
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
