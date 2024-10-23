n, m = (int(i) for i in input().split())
while n != 0 and m != 0:
    if n > m:
        n, m = n % m, m
    else:
        n,m = n, m % n
print( n if n != 0 else m)
# Классический алгоритм вычисления НОД