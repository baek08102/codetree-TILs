n=int(input())

starn=n
blankn=0

for i in range(1,n+1):
    
    for _ in range(0,blankn):
        print(" ",end=" ")
    for _ in range(starn*2,1,-1):
        print("*",end=" ")

    starn=starn-1
    blankn=blankn+1
    print()