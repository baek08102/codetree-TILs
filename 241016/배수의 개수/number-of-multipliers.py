cnt_a=0
cnt_b=0

for _ in range(10):
    n=int(input())

    if (n%3)==0:
        cnt_a+=1
    
    if (n%5)==0:
        cnt_b+=1

print(cnt_a, cnt_b)