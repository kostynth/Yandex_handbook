n, m = (int(i) for i in input().split())
n1, m1 = n, m
while n != 0 and m != 0:
    if n > m:
        n, m = n % m, m
    else:
        n,m = n, m % n
l =  n if n != 0 else m
print(n1 // l * m1 // l * l)
# Сначала находим НОД, затем добавляем уникальные для обоих чисел множители