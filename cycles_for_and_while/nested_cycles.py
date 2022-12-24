n = int(input())
t = "*"
for j in range(1, (n // 2) + 2):
    print(j * t, end='')
    print()
for i in range((n // 2), 0, -1):
    print(i * t, end='')
    print()