a, b = int(input()), int(input())
total = 0
largest_total = 0
num = 0
for i in range(a, b + 1):
    for j in range(1, i + 1):
        if i % j == 0:
            total += j
    if total >= largest_total:
        largest_total = total
        num = i
        total = 0
    else:
        total = 0
print(num, largest_total)