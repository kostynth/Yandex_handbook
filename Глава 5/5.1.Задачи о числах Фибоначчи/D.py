n = int(input())
if n ==0:
    print(0)
elif n ==1:
    print(1)
elif n ==2:
    print(2)
elif n == 3:
    print(4)
elif n == 4:
    print(7)
else:
    n1 = 0
    n2 = 1
    for i in range((n + 1) % 60):
        n1, n2 = n2, (n1 + n2) % 10

    print((n2 - 1 ) % 10)
    # Сумма n-чисел Фибоначчи - ((n + 2)-тое число Фибоначчи) -1