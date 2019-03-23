def disemvowel(word):
    
    new_word = ''

    vowels = 'aeiouAEIOU'

    for letter in word:
        if letter.lower() not in vowels:
            new_word += letter

    return new_word

print(disemvowel("UZOOeMGAd"))