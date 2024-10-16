n=int(input())

for n in range(1,n+1):
    
    if (n%3)==0 or ((n%10)!=0 and ((n%10)%3)==0):
        print(0,end=" ")
    else:
        print(n,end=" ")