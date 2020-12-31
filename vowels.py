vowels = ['a','e','i','o','u']
#word = "Millliways"
word = input("Enter the word you need to check vowels for : ")
found = []
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)

for vowel in found:
    print(vowel)
