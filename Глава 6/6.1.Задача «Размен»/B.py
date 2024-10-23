n = (int(input()))
print(n//50 + (n%50)//20 + ((n%50) % 20 )// 10 + (((n%50) % 20) % 10) // 5 + ((((n % 50) % 20) % 10) % 5))
while n:
    if n >= 50:
        print('50', end=' ')
        n -= 50
    elif n >= 20:
        print('20', end=' ')
        n -= 20
    elif n >= 10:
        print('10', end=' ')
        n -= 10
    elif n >= 5:
        print('5', end=' ')
        n -= 5
    else:
        print('1', end=' ')
        n -=1