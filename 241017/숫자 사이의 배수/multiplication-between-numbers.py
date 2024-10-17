a,b=map(int,input().split())

sum=0
cnt=0
for a in range(a,b+1):
    if(a%5)==0 or (a%7)==0:
        sum+=a
        cnt+=1

print(f'{sum} {(sum/cnt):.1f}')