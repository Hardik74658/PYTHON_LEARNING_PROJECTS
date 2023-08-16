
# 4. Use dictionary to store antonyms of words. E.g.- 'Right':'Left', 'Up':'Down', etc. Display all words and then ask user to enter a word and display antonym of it.
antonyms={'Right':'Left',
          'Up':'Down',
          "Front":"Behind",
          "On":"Off"}
print("Enter Any Word From Following To Know Their Antonym ")
for word in antonyms.keys() :
    print(f"=> {word}")
word = input("Enter Word : ").capitalize()
print(f"Antonym of {word} is : {antonyms.get(word)}")
