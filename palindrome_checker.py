word = input("Enter a word: ")
word_lower = word.lower()
print(word_lower)
if word_lower == word_lower[::-1]:
    print(f"The word {word} is a palindrome")
else:
    print(f"The word is not a palindrome!!!")