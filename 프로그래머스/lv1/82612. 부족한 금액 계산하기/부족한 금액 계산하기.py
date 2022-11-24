def solution(price, money, count):
    price = sum([price*x for x in range(count+1)])
    return 0 if money >= price else price-money