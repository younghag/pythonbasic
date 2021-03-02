def search4vowels(word):
    '''Return a boolean based on any vowels found'''
    vowels = set("aeiou")
    #word = input("Provide a word to search for vowels: ")
    return vowels.intersection(set(word))


search4vowels("young")