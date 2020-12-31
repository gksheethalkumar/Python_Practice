word = "bottles"
for num in range(99,0,-1):
    print(num, word, "of beer on the wall")
    print(num, word, "of beer")
    print("take one down")
    print("pass it worund")
    if num == 1:
        print("no more bottles")
    else:
        num -= 1
        if num == 1:
            word = "bottle"
            print(num, word, " of beer on the wall")
    print()
