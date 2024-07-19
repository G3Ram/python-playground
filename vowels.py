#  Eating vowels
word = input("Enter a word: ")
word = word.upper()

for i in word:
    if i in ["A", "E", "I", "O", "U"]:
        continue
    else:
        print(i)
