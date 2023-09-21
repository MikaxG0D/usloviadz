a, b, c = int(input()), int(input()), int(input())
if a > b:
    if a > c:
        print(a)
elif b > c:
    if b > a:
        print(b)
elif c > b:
    if c > a:
        print(c)