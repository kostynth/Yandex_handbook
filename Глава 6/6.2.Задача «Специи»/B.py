n , w = (int(i) for i in input().split())
l = []
for i in range(n):
    l.append(int(input()))
l.sort()
s = 0
# "Покупаем " самые дешевые, пока есть деньги
for i in l:
    if w - i < 0:
        break
    else:
        w-=i
        s+=1
print(s)