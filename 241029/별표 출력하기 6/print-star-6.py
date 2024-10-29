n=int(input())

for i in range(n,1,-1):
    for _ in range(0,n-i):
        print(" ",end=" ")  
    for _ in range(1,(2*i)):
        print("*",end=" ")

    print()

for i in range(0,n):
    for _ in range(1,n-i):
        print(" ",end=" ")
    for _ in range(0,(2*i)+1):
        print("*",end=" ")

    print()