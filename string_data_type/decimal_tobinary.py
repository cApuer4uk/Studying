# put your python code here
n = int(input())
s = ''
while n != 0:
    o = n % 2
    n //= 2
    s += str(o)
for i in range(-1, -len(s) - 1, -1):
    print(s[i], end="")
