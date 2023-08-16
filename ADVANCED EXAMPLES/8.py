# 8. Make a Python program to count letters of the word: MISSISSIPPI. Your program should store them in a dictionary as: {"M":1, "I":4, "S":4, "P":2}. Next, generalize this program for any word entered by user.


word = input("Enter Word : ").upper()
word_count={}
for letter in word:
    word_count[letter]=word.count(letter)
print(word_count)