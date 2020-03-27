a = int(input())
i = 1
c=0
while(i<=a):
    if(a==i):
        print("YES")
        break
    i=2**c
    c+=1
else:
    print("NO")