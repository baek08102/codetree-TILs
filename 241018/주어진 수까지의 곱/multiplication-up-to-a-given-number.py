a,b=map(int,input().split())

prod=1
for a in range(a,b+1):
    prod*=a

print(prod)