ab, ac, bc = int(input()), int(input()), int(input())
x = ab + ac
y = ab + bc
z = ac + bc
if ab > z:
    print('NO')
elif ac > y:
    print('NO')
elif bc > x:
    print('NO')
else:
    print("YEEEES")