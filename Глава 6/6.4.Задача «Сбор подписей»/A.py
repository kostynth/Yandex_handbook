#Считываем данные, сортируем
n = int(input())
l = []
for i in range(n):
    a = list(map(int, input().split()))

    l.append(a)
l.sort(key=lambda x: x[0])
# Если жилец один
if n == 1:
    print(l[0][0])
else:
    # Наша задача - выявить все "уникальные" промежутки времени
    # План действий - сравнить каждый промежуток с множеством "уникальных" промежутков (в нем сначала - только первый промежуток)
    # Если промежуток пересекается с каким-то из уникальный - модифицируем уникальный, если нет - добавляем в уникальные
    ans = [l[0]]
    c = 1

    for i in range(1, n):
        flag = True
        for j in range(c):
            if ans[j][0] <= l[i][0] <= ans[j][1] or ans[j][0] <= l[i][1] <= ans[j][1]:
                ans[j][0] = max(l[i][0], ans[j][0])
                ans[j][1] = min(l[i][1], ans[j][1])
                flag = False
        if flag:
            ans.append(l[i])
            c += 1

    print(c)
    ans = [i[1] for i in ans]
    print(*ans)