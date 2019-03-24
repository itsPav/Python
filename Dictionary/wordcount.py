# E.g. word_count("I do not like it Sam I Am") gets back a dictionary like:
# {'i': 2, 'do': 1, 'it': 1, 'sam': 1, 'like': 1, 'not': 1, 'am': 1}
# Lowercase the string to make it easier.

def word_count(string):
    
    stringDict = {}
    
    string = string.lower()
    string = string.split()
   
    for word in string:
        if word in stringDict:
            stringDict[word] += 1
        else:
            stringDict[word] = 1
    
    return stringDict

print(word_count("I do not like it Sam I Am"))