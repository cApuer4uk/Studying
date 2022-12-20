num = int(input())
b = num % 10
flag = True
while flag is True and num != 0:
    last_digit = num % 10
    if last_digit >= b:
        b = last_digit
        flag = True
    else:
        flag = False
    num = num // 10
if flag == True:
    print("YES")
else:
    print('NO')
