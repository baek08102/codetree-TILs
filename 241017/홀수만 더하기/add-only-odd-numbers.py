n=int(input())

sum=0
for _ in range(n):
    i=int(input())
    
    if(i%2)!=0 and (i%3)==0:
        sum+=i

print(sum)