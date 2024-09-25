a,b,c=map(int,input().split())

if a<b and a<c:
    print(1, end=" ")
elif b<c and a==b:
    print(1, end=" ")
elif c<b and a==c:
    print(1, end=" ")
else:
    print(0, end=" ")

if a==b and b==c:
    print(1)
else:
    print(0)