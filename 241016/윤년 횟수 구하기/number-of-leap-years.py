n=int(input())

i=1
cnt=0
for _ in range(n):

    if(i%4)==0:
        if((i%100)==0 and (i%400)!=0):
            i+=1
        else:
            cnt+=1
            i+=1
    else:
        i+=1

print(cnt)