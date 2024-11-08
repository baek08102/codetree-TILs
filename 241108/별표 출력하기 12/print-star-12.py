n=int(input())

for i in range(1,n+1):
    if i==1:
        for _ in range (n):
            print("*",end=" ")
    else:
        for j in range (1,n+1):
            if j>=i and (j%2)==0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
    
    print()