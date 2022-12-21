mx = - 10 ** 6
total = 0
for i in range(10):
    num = int(input())
    if num < 0:
        total += num
    if num > mx and num < 0:
        mx = num
if total == 0:
    print('NO')
else:
    print(total)
    print(mx)
