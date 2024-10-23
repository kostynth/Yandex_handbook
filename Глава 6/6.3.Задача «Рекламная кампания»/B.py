n, k, w = map(int, input().split())
l = []
for i in range(k):
    l.append(list(map(int, input().split())))
#Сортируем по убыванию цены
l.sort(reverse=True, key=lambda x:x[0])
# Заполняем недели. Для каждой недели (цикл) берем n (по количеству билбордов) самых дорогих предложений, при условии что
# у данных предложений еще остались недели
ans = 0
for week in range(w):
    now=0
    for bilboard in range(n):
        while now<k and l[now][1]==0:
            now+=1
        if now==k:
            break
        ans+=l[now][0]
        l[now][1]-=1

print(ans)