def search4letters(phrase:str, letters:str='aeiou') -> set:
    """Return a set of the 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))
search4letters('hitch-hiker')
search4letters(phrase = 'galaxy', letters= 'xyz')
search4letters('life, the universe, and everything', 'o')

import random
random.randint(0, 255)