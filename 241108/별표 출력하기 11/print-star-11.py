n=int(input())

for i in range (1,2*n+2):
    if (i%2)!=0:
        for _ in range (2*n+1):
            print("*",end=" ")
    else:
        for j in range (1,2*n+2):
            if (j%2)!=0:
                print("*",end=" ")
            else:
                print(" ",end=" ")

    print()