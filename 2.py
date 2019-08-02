s1,s2=map(str,input().split())
c=max(len(s1),len(s2))
m=0
for i in range(c):
	if s1[i]!=s2[i]:
		m=s+1
if m==1:
	print("yes")
else:
	print("no")
