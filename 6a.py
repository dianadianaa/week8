def min(x, y):
    if (x<y):
        return x
    elif(y<x):
        return y
    else:
    	return x

a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])
minimum = min(min(a[0], a[1]),min(a[2],a[3]))
print(minimum)