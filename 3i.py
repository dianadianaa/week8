a= int(input())
i=2
count=0
for i in range (1,a+1):
	if(a%i==0):
		count=count+1	
		i=i+1
print(count)

