# Quarter : 25, Nikel : 5, Dime : 10, Penny : 1

def coin_count(cents):
    coins = [25,10,5,1]
    count = 0
    for coin in coins:
        count += ( cents // coin )
        cents = cents % coin
        if cents == 0:
            break
    return count

print(coin_count(56))
