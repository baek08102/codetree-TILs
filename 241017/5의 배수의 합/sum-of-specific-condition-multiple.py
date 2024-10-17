a,b=map(int,input().split())

sum=0
if a<=b:
    for a in range(a,b+1):
        if (a%5)==0:
            sum+=a

if a>b:
    for b in range(b,a+1):
        if (b%5) ==0:
            sum+=b
print(sum)