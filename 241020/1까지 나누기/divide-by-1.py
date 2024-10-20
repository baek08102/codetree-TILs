n=int(input())

for i in range(1,n*2):
    n/=i

    if n<=1:
        print(i)
        break