n=int(input())

sum=0
avg=0

for _ in range(n):
    i=int(input())

    sum+=i

print(f'{sum} {(sum/n):.1f} ')