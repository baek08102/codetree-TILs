a,b=map(int,input().split())

if a<b:
    for _ in range(b,a-1,-1):
        print(b,end=" ")
        b-=1
elif b<a:
    for _ in range(a,b-1,-1):
        print(a,end=" ")
        a-=1