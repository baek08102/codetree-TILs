sum=0
cnt=0

while True:
    n=int(input())

    if cnt==0:
        sum=n
        cnt=1

    else:
        if(n//10)!=2:
            print(f'{(sum/cnt):.2f}')
            break
        else:
            sum+=n
            cnt+=1