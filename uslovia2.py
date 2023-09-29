a, b, c = int(input()), int(input()), int(input())
mid = x1
if a == b or b == c or a == c:
    midd = 'Error'
else:
    if (b > a and b < c) or (b < a and b > c):
        mid = b
    elif (c > a and c < b) or (c < a and c > b):
        mid = c
    elif (a > b and a < c) or (a < b and a > c)
        mid = a

print(f'Среднее число - {mid}')
