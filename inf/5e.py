n=int(input())
a = [int(i) for i in input().split()]
count=0
for i in range (0,len(a)+1):
    if a[i]*a[i+1]>0:
        print("YES")
        break
    else:
        print("NO")
        break