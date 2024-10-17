n=int(input())

i=n
sum=0
for n in range(1,i):
    if(i%n)==0:
        sum+=n
    
if sum==i:
    print('P')
else:
    print('N')