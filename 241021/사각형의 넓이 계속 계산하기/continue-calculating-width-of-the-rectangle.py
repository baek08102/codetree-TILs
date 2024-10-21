cnt=0

while True:
    arr=input()
    w,h,s=arr.split()
    
    print(int(w)*int(h))

    if(s=='C'):
        break