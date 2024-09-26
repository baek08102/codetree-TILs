a,b=map(str,input().split())
x,y=map(str,input().split())

if ((int(a)>=19) and (b=='M')) or ((int(x)>=19) and (y=='M')):
    print(1)
else:
    print(0)