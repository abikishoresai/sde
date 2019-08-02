n,g=map(int,input().split())
p=n|g
o=bin(p)[2:]
print(o.count("1"))
