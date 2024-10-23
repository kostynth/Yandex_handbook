n = int(input())
n1 = list(map(int, input().split()))
n2 = list(map(int, input().split()))
n1.sort(reverse=True)
n2.sort(reverse=True)
s = 0
for i in range(n):
    s += n1[i] * n2[i]
print(s)
# Сортируем, последовательно перемножаем