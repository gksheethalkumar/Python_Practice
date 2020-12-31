def search4vowels(word:str):
    """ This search for Vowels """
    vowels = set('aeiou')
    return vowels.intersection(set(word))

def search4letters(phrase:str, letters:str='aeiou'):
    ''' This is to find letters in a given phrase'''
    return set(letters).intersection(set(phrase))

