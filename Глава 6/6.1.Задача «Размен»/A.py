final = []
cnt = 0
n = int(input())
# Простой перебор всех вариантов
for ten in range((n // 10) + 1):

    for five in range(((n - (10 * ten)) // 5) + 1):
        one = n - 10 * ten - 5 * five # Добираем единичками
        steps = str(ten + five + one)
        # Добавление в виде массива может вызвать Превышен лимит времени (TL)
        final.append((steps + ' ' + '10 ' * ten + '5 ' * five + '1 ' * one).rstrip())
        cnt += 1
print(cnt)
print(*final, sep='\n')