a1,b1=map(str,input().split())
a2,b2=map(str,input().split())
a3,b3=map(str,input().split())

c1=int(0)


if a1=='Y' and int(b1)>=37:
    c1+=1
if a2=='Y' and int(b2)>=37:
    c1+=1
if a3=='Y' and int(b3)>=37:
    c1+=1

if c1>=2:
    print('E')
else:
    print('N')