c,n=map(str,input().split())
n=int(n)
i=1

if c=='A':
    for n in range(1,n+1):
        print(i,end=" ")
        i+=1
elif c=='D':
    for n in range(n,0,-1):
        print(n,end=" ")