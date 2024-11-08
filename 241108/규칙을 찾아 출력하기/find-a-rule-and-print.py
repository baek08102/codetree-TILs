n=int(input())

for i in range (1,n+1):
    if i==1 or i==n:
        for _ in range (n):
            print("*",end=" ")
    
    else:
        for j in range (1,n+1):
            if j!=n:
                if j<i:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            else:
                print("*",end="")
    
    print()