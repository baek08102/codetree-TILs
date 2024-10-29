n=int(input())

for i in range(0,n):
    for _ in range(n-i):
        print("*",end="")
    for _ in range(0,2*i):
        print(" ",end="")
    for _ in range(n-i):
        print("*",end="")
    print()