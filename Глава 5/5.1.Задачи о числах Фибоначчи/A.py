import sys
n = int(sys.stdin.readline().strip())
n1 = 0
n2 = 1
if n == 0:
    print(0)
else:
    for _ in range(n-1):
        n1, n2 = n2, n1 + n2
    print(n2)

# Вычисление через цикл