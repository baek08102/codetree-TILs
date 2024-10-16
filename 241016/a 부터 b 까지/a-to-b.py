a,b=map(int,input().split())

int i=a
for i in range(a,b+1):
    if (i%2)==0:
        print(i)
    i+=3
    elif (i%3)==0: