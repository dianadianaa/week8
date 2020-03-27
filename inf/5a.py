
a=[]
for i in range(int(input())):
	a.append(int(input()))
for i in range(0, len(a), 2):
    print(str(a[i]), end = " ")