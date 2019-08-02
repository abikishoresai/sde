z=input()
k=""
l=[]
for i in z:
	l.append(z.count(i))
min1=min(l)
for i in z:
	if z.count(i)==min1 and i!=" ":
		k=k+i.lower()+" "
print(k.strip())
