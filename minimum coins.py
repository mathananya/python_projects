
def minimum_coins(N):
    coins = 0
    amountLeft = N
    coin_list = [1000,500,100,50,20,10,5,2,1]
    for x in coin_list:
        while amountLeft >= x:
            amountLeft = amountLeft-x
            coins = coins+1
        if amountLeft == 0:
            return coins
            
a = int(input("write number: "))
print(minimum_coins(a))
