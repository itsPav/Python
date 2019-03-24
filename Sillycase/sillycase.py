def sillycase(word):
    half = round(len(word)/2)
    
    return word[0:half].lower() + word[half:].upper()

print(sillycase("Treehouse"))