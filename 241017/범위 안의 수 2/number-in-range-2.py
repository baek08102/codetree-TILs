sum=0
cnt=0

for _ in range(10):
    i=int(input())

    if (i>=0) and (i<=200):
        sum+=i
        cnt+=1
    
print(f'{sum} {(sum/cnt):.1f}')