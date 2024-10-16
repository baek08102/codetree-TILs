a,b=map(int,input().split())

i=a
for a in range(a,b+1):
    if a==i:
        if (i%2)==0:
            print(i,end=" ")
            i+=3
        else:
            print(i,end=" ")
            i*=2