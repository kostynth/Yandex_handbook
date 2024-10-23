n, le = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
ans = 0
c = 1
now = l[0] + le
#Строим покрытие для первой точки (до какой точки покроет первый отрезок)
for i in range(1, n):
    #Если текущего покрытия не хватило для след точки - берем эту точку и строим покрытие уже от неё
    if l[i] > now:
        now = l[i] + le
        c+=1
print(c)