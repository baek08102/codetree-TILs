n=int(input())

cnt=0

while True:
    if n!=1:
        if(n%2)==0:
            n/=2
            cnt+=1

        elif(n%2)!=0:
            n=(3*n)+1
            cnt+=1
    elif n==1:
        print(cnt)
        break