n=int(input())

for i in range (1, n+1):
    for j in range (n):
        print((n * i) - (i * j), end= " ")
    print("")