n=int(input())

for n in range(1,n+1):

    a=(n//10) #a는 n의 10의자리 수
    b=(n%10) #b는 n의 1의자리 수

    if n<=10 or (n%10)==0:
        if (n%3)==0:
            print(0,end=" ")
        else:
            print(n,end=" ")
    else:        
        if ((a%3))==0 or (b%3)==0 or (n%3)==0:
            print(0,end=" ")
        else:
            print(n,end=" ")