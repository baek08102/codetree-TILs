a,b,c = map(int,input().split())
if a==b and a==c:
    print(a)
elif b == c:
    if a>b:
        print(a)
    else:
        print(b)
else:
    if a>b and a>c:
        print(a)
    elif b>c:
        print(b)
    else:
        print(c)