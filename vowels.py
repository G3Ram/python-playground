#  Eating vowels
word = input("Enter a word: ")
word = word.upper()
word_without_vowels = ""
for i in word:
    if i in ["A", "E", "I", "O", "U"]:
        continue
    else:
        word_without_vowels += i

print(word_without_vowels)
