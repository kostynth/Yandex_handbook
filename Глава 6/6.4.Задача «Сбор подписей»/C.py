n, k = list(map(int, input().split()))
l = list(map(int, input().split()))
# Если у нас отрезков больше равно исходных точек - просто берем нужное количество нулевых по длине отрезков(покрывающих одну точку)
if n <= k:
    print(0)
else: #Ответ на задачу - последовательность отрезков на данных точках. Между точками существуют
    #расстояния. Не трудно догадаться, что для К отрезков между ними будет К-1 "дыр" (без покрытия каким-либо отрезком),
    # которые не включены в итоговую сумму. Соответственно, чтобы максимально уменьшить эту сумму, нужно исключить самые
    #большие расстояния - сделать их "дырами"
    l.sort()
    dist = []
    for i in range(n - 1):
        dist.append(l[i + 1] - l[i])
    dist.sort(reverse=True)

    print(sum(dist[k-1:]))
