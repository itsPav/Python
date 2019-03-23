def disemvowel(word):
    
  vowels = list('aeiouAEIOU')
  
  word = list(word)
  
  for letter in word:
    if letter in vowels:
      print(letter)
      word.remove(letter)
  
  word = ''.join(word)
  
  return word

print(disemvowel("UZOOeMGAd"))