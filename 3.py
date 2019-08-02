n=input()
c1=0
c2=0
for i in range(len(n)):
    if n[i]=="(":
        c1=c1+1
    if n[i]==")":
        c2=c2+1
if c1==c2:
    print("yes")
else:
    print("no")
© 2019 GitHub, Inc.
