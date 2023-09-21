a, b, c = int(input()), int(input()), int(input())
if a > b:
    if b > c:
        print(b)
elif b > a:
    if a > c:
        print(a)
elif a > c:
    if c > b:
        print(c)
elif a == b == c:
    print("ERROR")