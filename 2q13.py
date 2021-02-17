l=[]
n=int(input("enter the number of elements:"))
for i in range(0,n):
	elements=int(input())
	l.append(elements)
print(l)
for i in l:
	if(i%2==0):
		l.remove(i)
		pass
print("list after removing even number:",l)