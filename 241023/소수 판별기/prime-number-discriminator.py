n=int(input())

k=False
for i in range (2,n):
    if (n%i)==0:
        k=True
    
if k==True:
    print('C')
else:
    print('P')