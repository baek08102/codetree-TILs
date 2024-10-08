a,b,c=map(int,input().split())

if (a>b and b>c) or (a<b and b<c):
    print(b)
elif (b>a and a>c) or (c>a and a>b):
    print(a)
else:
    print(c)