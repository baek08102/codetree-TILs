n=int(input())

cnt=0
for i in range(1,n*2):

    if n<=1:
        print(cnt)
        break
    else:
        n/=i
        cnt+=1