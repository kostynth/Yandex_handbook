n , w = (int(i) for i in input().split())
l = []
for i in range(n):
    p, wn = map(int, input().split())
    # Сразу не  добавляем предметы с нулевым весом или ценой
    if p == 0 or w == 0:
        continue
    l.append([p/wn, wn])
l.sort(reverse=True)
s = 0
i = 0
# Алгоритм Рюкзака : добавляем по убыванию цены предметы полностью, пока есть место. Затем добавляем последний предмет
# на оставшуюся ёмкость.
for pr, wn in l:

    if w > wn:

        s += wn * pr

        w -= wn
    else:

        s += w * pr
        break
print(s)