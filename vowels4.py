vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels: ")
found = {}
print(found)
for char in word:
    if char in vowels:
        found.setdefault(char,0)
        found[char] += 1

for k,v in sorted(found.items()):
    print(k , 'was found' , v , 'number of times')


