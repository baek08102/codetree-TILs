a,b=map(int,input().split())

sum=0
for a in range(a,b+1):
    if (a%2)==0:
        sum+=a

print(sum)