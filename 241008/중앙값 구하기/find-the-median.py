a,b,c=map(int,input().split())

if a>b:
    if a>c and b>c:
        print(b)
    else:
        print(a)
elif b>c:
    print(c)
else:
    print(b)