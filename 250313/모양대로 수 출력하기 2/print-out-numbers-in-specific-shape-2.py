n=int(input())

cnt=1

for i in range(n):
    for j in range(n):
        if (cnt < 4):
            print(cnt * 2,end=" ")
            cnt += 1
        else :
            print(cnt * 2,end=" ")
            cnt = 1
    print("")