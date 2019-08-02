s=int(input())
k=""
for i in range(1,s+1):
	for j in range(1,s+1):
		if i*j==s:
			if i%2==0:
				k=k+str(i)+" "
print(k.strip())
